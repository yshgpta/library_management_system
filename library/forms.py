from django import forms
from django.contrib.auth.models import User
from library.models import StudentProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter College email ID.')

    class Meta():
        model = User
        help_texts = {"username":"Required.Enter roll no in upper case"}
        labels = {"username":"Roll No"} 
        fields = ('username','first_name','last_name','email','password')

class StudentProfileForm(forms.ModelForm):
    class Meta():
        model = StudentProfile
        fields = ()