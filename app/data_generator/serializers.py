from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Schema, Column, DataSet


class SchemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = ('id', 'name', 'modified',)


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('name', 'typeof', 'order', 'range_from', 'range_to')


class DataSetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = ('id', 'created', 'status', 'num_row')


class SchemaCreateSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True)

    class Meta:
        model = Schema
        fields = ('name', 'column_separator', 'string_character', 'columns')

    def create(self, validated_data):
        columns = validated_data.pop('columns')
        new_schema = Schema.objects.create(**validated_data)
        Column.objects.bulk_create(
            [
                Column(**column, schema=new_schema) for column in columns
            ]
        )
        return new_schema

