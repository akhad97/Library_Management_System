from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User

class AdminForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}),required=True, max_length=50)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),required=True, max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),required=True, max_length=50)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}),required=True,max_length=30)

    class Meta:
        model = User
        fields = ('name', 'email',  'username', 'password1', 'password2')

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password != confirm_password:
            raise forms.ValidationError('Password Mismatch')
        return confirm_password

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password != confirm_password:
            raise forms.ValidationError('Password Mismatch')
        return confirm_password

class UserLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),required=True,max_length=50)
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),required=True,max_length=50)
    

class BookForm(forms.ModelForm):  
    class Meta:
        model = Book
        fields = ('__all__')

class StudentRegisterForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}),required=True, max_length=50)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}),required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),required=True,max_length=50)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile'}),required=True,max_length=50)
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Branch'}),required=True,max_length=50)
    studentID = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'StudentID'}),required=True,max_length=50)
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'email','mobile','branch','studentID')


class IssuedBookForm(forms.ModelForm):   
    class Meta:
        model = IssuedBook
        exclude = ['issuedate', 'authorname', 'expirydate']
    
class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        exclude = ['returndate', 'studentname','bookname']
