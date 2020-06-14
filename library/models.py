from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    isbn = models.CharField('ISBN', max_length=13,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class StudentProfile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)

    book1 = models.CharField(blank=True,max_length=10)
    book2 = models.CharField(blank=True,max_length=10)
    book3 = models.CharField(blank=True,max_length=10)
    book4 = models.CharField(blank=True,max_length=10)

    def __str__(self):
        return self.user.username

class Add_No(models.Model):
    AVAILABILITY = (
        ('I','Issued'),
        ('A','Available'),
    )
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(StudentProfile,null=True,blank=True,on_delete=models.SET_NULL)
    book_no = models.CharField(max_length=10)
    shelf_no = models.CharField(max_length=5)
    availability = models.CharField(max_length=2,choices=AVAILABILITY,default='A')
    issued_on = models.DateField(auto_now=True)
    reissue_cycle = models.IntegerField(default=1)

    def __str__(self):
        return self.book_no

class Semester_Book(models.Model):
    SEMESTER = (
        ('Semester-1','Semester-1'),
        ('Semester-2','Semester-2'),
        ('Semester-3','Semester-3'),
        ('Semester-4','Semester-4'),
        ('Semester-5','Semester-5'),
        ('Semester-6','Semester-6'),
        ('Semester-7','Semester-7'),
        ('Semester-8','Semester-8'),
    )
    semester = models.CharField(max_length=10,choices=SEMESTER,default=None)
    book1_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book2_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book3_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book4_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book5_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book6_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book7_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book8_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book9_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book10_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book11_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book12_isbn = models.CharField(max_length=13,default=None,blank=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    def __str__(self):
        return self.semester