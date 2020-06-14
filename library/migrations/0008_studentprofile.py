# Generated by Django 3.0.3 on 2020-03-10 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0007_book_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book1', models.CharField(blank=True, max_length=10)),
                ('book2', models.CharField(blank=True, max_length=10)),
                ('book3', models.CharField(blank=True, max_length=10)),
                ('book4', models.CharField(blank=True, max_length=10)),
                ('b_count', models.IntegerField(default=0, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
