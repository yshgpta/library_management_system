# Generated by Django 3.0.3 on 2020-04-05 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_auto_20200405_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_no',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.StudentProfile'),
        ),
    ]