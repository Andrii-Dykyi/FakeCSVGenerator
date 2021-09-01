from django.contrib import admin

from .models import Schema, Column, DataSet


class ColumnInline(admin.StackedInline):
    model = Column
    extra = 0


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    inlines = [ColumnInline]


admin.site.register(DataSet)