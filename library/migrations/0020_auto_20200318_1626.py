# Generated by Django 3.0.3 on 2020-03-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_add_no_reissue_cycle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_no',
            name='reissue_cycle',
            field=models.IntegerField(default=1),
        ),
    ]
