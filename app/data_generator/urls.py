from django.urls import path, re_path

from .views import (DataSetCSVView, DataSetListCreateView, LoginView,
                    LogoutView, SchemaDeleteView, SchemaListCreateView,
                    TaskStatusView, index, login_reserve)


app_name = 'data_generator'
urlpatterns = [
    # Entry point
    path('', index, name='index'),
    path('login/', login_reserve, name='login'),

    # Auth
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),

    # Api
    path('api/my-schemas/', SchemaListCreateView.as_view(), name='my_schemas'),
    path('api/delete-schema/<int:pk>/', SchemaDeleteView.as_view(), name='schema'),
    path('api/schema/<int:schema_pk>/data-sets/', DataSetListCreateView.as_view(), name='schema_data_sets'),

    # Task Status
    path('api/schema/status/<str:task_id>/', TaskStatusView.as_view(), name='task_status'),

    # File Download
    path('api/dataset/<int:dataset_id>/file/', DataSetCSVView.as_view(), name='dataset_file'),

    # Serve SPA router
    re_path('', index, name='index')
]
