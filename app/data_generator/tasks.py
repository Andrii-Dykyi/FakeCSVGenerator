from django.core.files.base import ContentFile

from fake_data_project import celery_app
from .models import Column, DataSet, Schema
from .service import fake_file_writer


@celery_app.task
def data_generator_task(schema_id, dataset_id):
    """
    Generate csv file with fake data according to schema column types.
    """
    data_set = DataSet.objects.get(pk=dataset_id)
    schema = Schema.objects.prefetch_related('columns').get(pk=schema_id)
    columns = schema.columns.all()

    csv_io = fake_file_writer(schema, columns, data_set.num_row)

    file_name = f'fake_data{schema_id}{dataset_id}.csv'
    data_set.csv_file.save(file_name, ContentFile(csv_io.getvalue()), save=False)
    data_set.status = 'Ready'
    data_set.save()
