# Generated by Django 3.0.3 on 2020-03-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20200310_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_no',
            name='availability',
            field=models.CharField(choices=[('I', 'Issued'), ('A', 'Available')], default='A', max_length=10),
        ),
    ]