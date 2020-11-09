import django_filters
from .models import *

class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Book
        fields = ('bookname', 'bar_code')


class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student
        exclude = ['lastname', 'email', 'mobile', 'brach']

class IssuedBookFilter(django_filters.FilterSet):

    class Meta:
        model = IssuedBook
        exclude = ['studentname', 'authorname', 'bookname', 'issuedate', 'expirydate']