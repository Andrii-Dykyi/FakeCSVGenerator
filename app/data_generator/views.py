from celery.result import AsyncResult
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataSet, Schema
from .serializers import (DataSetListSerializer, SchemaCreateSerializer,
                          SchemaListSerializer)
from .tasks import data_generator_task


# View to handle browser requests
def index(request):
    """Entry point of app."""
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'index.html')


def login_reserve(request):
    """Reserve view to handle login."""
    return render(request, 'index.html')


# AUTH views handles AJAX calls from frontend
class LoginView(APIView):
    """Handle user's login."""
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request: Request):
        """Check if user exists and login if yes."""
        if not (user := authenticate(**request.data)):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({'username': user.username}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """Handle user's logout."""
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """Logout current user."""
        logout(request)
        return Response(status=status.HTTP_200_OK)


# API views handles AJAX calls from frontend
class SchemaListCreateView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Return user's all schemas."""
        schemas = Schema.objects.only('name', 'modified').filter(owner=request.user)
        serializer = SchemaListSerializer(schemas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create schema and related columns."""
        serializer = SchemaCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SchemaDeleteView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            schema = Schema.objects.get(id=pk)
        except Schema.DoesNotExist:
            raise Http404

        schema.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DataSetListCreateView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, schema_pk):
        """Return all datasets related to specific schema."""
        try:
            schema = (
                Schema.objects
                .prefetch_related('datasets')
                .get(id=schema_pk, owner=request.user)
            )
        except Schema.DoesNotExist:
            raise Http404

        serializer = DataSetListSerializer(schema.datasets.only('created', 'status'), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, schema_pk):
        """Create data set for specific schema."""
        schema = get_object_or_404(Schema, pk=schema_pk)

        serializer = DataSetListSerializer(data=request.data)
        if serializer.is_valid():
            new_data_set = serializer.save(schema_id=schema_pk)

            task = data_generator_task.delay(schema_pk, new_data_set.id)

            response_data = {
                'taskID': task.id,
                'dataSet': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataSetCSVView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, dataset_id):
        """Return CSV file of specific data set."""
        dataset = get_object_or_404(DataSet, pk=dataset_id, schema__owner=request.user)
        return FileResponse(open(dataset.csv_file.path, 'rb'))


class TaskStatusView(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, task_id):
        """Return task status by ID."""
        task_result = AsyncResult(task_id)
        response = {
            "taskID": task_id,
            "taskStatus": task_result.status
        }
        return Response(response, status=status.HTTP_200_OK)
