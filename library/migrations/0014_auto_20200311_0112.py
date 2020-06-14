# Generated by Django 3.0.3 on 2020-03-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20200310_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='B_no',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='books',
            field=models.ManyToManyField(to='library.B_no'),
        ),
    ]
