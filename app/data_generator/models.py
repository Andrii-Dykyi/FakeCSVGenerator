import os
from django.db import models


class Schema(models.Model):
    """Class to represent schema model in db."""
    SEPARATORS = [
        (',', 'Comma (,)',),
        ('.', 'Dot (.)',),
    ]
    CHARACTERS = [
        ('"', 'Double-quote (")',),
        ("'", "Single-quote (')", )
    ]
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    column_separator = models.CharField(max_length=25, choices=SEPARATORS)
    string_character = models.CharField(max_length=25, choices=CHARACTERS)
    name = models.CharField(max_length=124)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['pk']


class Column(models.Model):
    """Class to represent schema column in db."""
    TYPES_OF = (
        ('name', 'Full name',),
        ('company', 'Company name',),
        ('job', 'Job'),
        ('integer', 'Integer'),
        ('phone_number', 'Phone number'),
        ('address', 'Address'),
        ('email', 'Email'),
        ('domain_name', 'Domain name')
    )
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='columns')
    name = models.CharField(max_length=124)
    typeof = models.CharField(max_length=48, choices=TYPES_OF)
    order = models.SmallIntegerField()
    range_from = models.PositiveIntegerField(null=True, default=0)
    range_to = models.PositiveIntegerField(null=True, default=1)

    def __str__(self):
        return f'{self.name} {self.typeof}'

    class Meta:
        ordering = ['order']


class DataSet(models.Model):
    """Class to represent schema dataset model in db."""
    STATUS = (
        ('Processing', 'Processing'),
        ('Ready', 'Ready')
    )
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, null=True, related_name='datasets')
    num_row = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=10, default='Processing', choices=STATUS)
    created = models.DateField(auto_now_add=True)
    csv_file = models.FileField(upload_to='data_sets/', null=True)

    def __str__(self):
        return f'{self.schema} - {self.num_row}'
    
    def delete(self):
        try:
            os.remove(self.csv_file.path)
        except:
            pass
        finally:
            super().delete()
