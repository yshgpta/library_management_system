# Generated by Django 3.0.3 on 2020-03-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_add_no_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_no',
            name='issued_on',
            field=models.DateField(auto_now=True),
        ),
    ]