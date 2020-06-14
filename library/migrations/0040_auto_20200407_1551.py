# Generated by Django 3.0.3 on 2020-04-07 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0039_semester_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester_Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('Semester-1', 'Semester-1'), ('Semester-2', 'Semester-2'), ('Semester-3', 'Semester-3'), ('Semester-4', 'Semester-4'), ('Semester-5', 'Semester-5'), ('Semester-6', 'Semester-6'), ('Semester-7', 'Semester-7'), ('Semester-8', 'Semester-8')], default=None, max_length=10)),
                ('book1_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book2_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book3_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book4_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book5_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book6_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book7_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book8_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book9_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book10_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book11_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
                ('book12_isbn', models.CharField(blank=True, default=None, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13)),
            ],
        ),
        migrations.DeleteModel(
            name='Semester_Book',
        ),
    ]
