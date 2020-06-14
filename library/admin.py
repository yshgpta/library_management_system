from django.contrib import admin
from library.models import Book, Add_No,StudentProfile,Semester_Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Add_No)
admin.site.register(StudentProfile)
admin.site.register(Semester_Book)