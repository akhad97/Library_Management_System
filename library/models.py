from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)


class Book(models.Model):
    CATEGORY = (
        ('Education', 'Education'),
        ('Computer', 'COMPUTER'),
        ('Electronics', 'Electronics'),
        ('Civil', 'Civil'),
        ('Business', 'Business'),
        ('Miscolleneous', 'Miscolleneous'),
        ('Historical', 'Historical'),
        ('Literatura', 'Literatura'),
        ('Detective and Mystery', 'Detective and Mystery')
    )
    bookname = models.CharField(max_length=50)
    authorname = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True, default='Education')
    bar_code = models.CharField(max_length=50, unique=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def __str__(self):
        return self.bar_code

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    studentID = models.CharField(max_length=50)

    def __str__(self):
        return self.studentID


def get_expiry():
    return datetime.today() + timedelta(days=15)

class IssuedBook(models.Model):
    barcode = models.CharField(max_length=30, blank=True, null=True)
    studentname = models.CharField(max_length=50, null=True)
    authorname = models.CharField(max_length=50, null=True)
    bookname = models.CharField(max_length=50, null=True)
    studentID = models.CharField(max_length=30)
    issuedate = models.DateField(auto_now_add=True)
    expirydate = models.DateField(default=get_expiry)

    def __str__(self):
        return self.studentID
    
    def __str__(self):
        return self.barcode

class Return(models.Model):
    returndate = models.DateField(auto_now=True)
    studentID = models.CharField(max_length=50)
    studentname = models.CharField(max_length=50)
    bookname = models.CharField(max_length=50)
    bar_code = models.CharField(max_length=50)

    def __str__(self):
        return self.bookname