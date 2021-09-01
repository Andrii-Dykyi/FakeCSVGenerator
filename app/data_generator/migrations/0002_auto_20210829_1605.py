# Generated by Django 3.2.6 on 2021-08-29 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='column_separator',
            field=models.CharField(choices=[(',', 'Comma (,)'), ('.', 'Dot (.)')], max_length=25),
        ),
        migrations.AlterField(
            model_name='schema',
            name='string_character',
            field=models.CharField(choices=[('"', 'Double-quote (")'), ("'", "Single-quote (')")], max_length=25),
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('typeof', models.CharField(max_length=48)),
                ('order', models.SmallIntegerField()),
                ('range_from', models.PositiveIntegerField(default=0, null=True)),
                ('range_to', models.PositiveIntegerField(default=1, null=True)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_generator.schema')),
            ],
        ),
    ]