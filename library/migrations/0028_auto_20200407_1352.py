# Generated by Django 3.0.3 on 2020-04-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0027_auto_20200407_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester_book',
            name='semester',
            field=models.CharField(choices=[('Semester-1', 'Semester-1'), ('Semester-1', 'Semester-2'), ('Semester-3', 'Semester-3'), ('Semester-4', 'Semester-4'), ('Semester-5', 'Semester-5'), ('Semester-6', 'Semester-6'), ('Semester-7', 'Semester-7')], default=None, max_length=10),
        ),
    ]
