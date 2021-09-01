import csv
import random
from io import StringIO

from faker import Faker


def get_fake_cell_data(column):
    """Return fake value accourding to column type."""
    if column.typeof == 'integer':
        return random.randint(column.range_from, column.range_to)
    else:
        return getattr(Faker(), column.typeof)()


def fake_file_writer(schema, columns, rows):
    """Write file in memory and return it."""
    csv_io = StringIO()
    writer = csv.writer(
        csv_io, delimiter=schema.column_separator, quotechar=schema.string_character
    )

    writer.writerow(
        [column.name for column in columns]
    )
    writer.writerows(
        [
            [get_fake_cell_data(column) for column in columns] for row in range(rows)
        ]
    )
    return csv_io
