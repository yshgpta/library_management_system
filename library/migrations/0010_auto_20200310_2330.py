# Generated by Django 3.0.3 on 2020-03-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_add_no_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='b_count',
            field=models.IntegerField(default=0),
        ),
    ]
