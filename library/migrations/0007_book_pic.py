# Generated by Django 3.0.3 on 2020-03-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20200306_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='book_image'),
        ),
    ]
