from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *
from django.http import *
from django.contrib import messages
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from datetime import date, datetime
import re
from django.db.models import Q
from .filter import *

def index(request):
    return render(request, 'library/index.html')

def admin_signup(request):
    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form_user = form.save(commit=False)
            form_user.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'library/admin_signup.html', context)

def loginPage(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                return render(request, 'library/inactive_account.html')
    
    context = {'form':form}
    return render(request, 'library/login.html', context)

def admin_dashboard(request):
    return render(request, 'library/admin_dashboard.html')


def book(request):
    return render(request, 'library/book.html')

def add_book(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
        return render(request, 'library/add_book.html', {'form':form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book')

def view_book(request):
    book_list = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=book_list)
    context = {'view_book': Book.objects.all(), 'filter':book_filter}
    return render(request, 'library/view_book.html', context)

def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('view_book')

def update_book(request, pk):
    books = Book.objects.get(id=pk)
    form = BookForm(instance=books)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('view_book')
    context = {'form':form}
    return render(request, 'library/update_book.html', context)

def issue_new_book(request):
    form = IssuedBookForm()
    if request.method == 'POST':
        form = IssuedBookForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['barcode']
            name = form.cleaned_data['studentID']
            form.save(commit=True)
            books = Book.objects.get(bar_code=book)
            studentID = Student.objects.get(studentID=name)
            return redirect('view_issue_book')        
    return render(request, 'library/issue_new_book.html', {'form':form})

def view_issue_book(request):  
    # issuedbooks = IssuedBook.objects.all()
    # li = []

    # for ib in issuedbooks:
    #     issdate = str(ib.issuedate.day)+'-'+ str(ib.issuedate.month)+'-'+ str(ib.issuedate.year)
    #     expdate = str(ib.expirydate.day)+'-'+ str(ib.expirydate.month)+'-'+ str(ib.expirydate.year)

    #     days=(date.today()-ib.issuedate)
    #     d=days.days

    #     fine = 0
    #     if d>1:
    #         day = d-1
    #         fine=day*10

    #     books = list(Book.objects.filter(bar_code=ib.barcode))
    #     students = list(Student.objects.filter(studentID=ib.studentID))

    #     i=0

    #     for l in books:
    #         t=(fine)
    #         i=i+1
    #         li.append(t) 

    issuedbook_list = IssuedBook.objects.all()
    issuedbook_filter = IssuedBookFilter(request.GET, queryset=issuedbook_list)  
    issues = IssuedBook.objects.order_by('studentID', 'issuedate')
    return render(request, 'library/view_issue_book.html', {'issues':issues, 'filter':issuedbook_filter})

def issue_book(request):
    return render(request, 'library/issue_book.html')

def return_book(request):
    form = ReturnForm()
    if request.method == 'POST':
        form = ReturnForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            book = form.cleaned_data['bar_code']
            books = Book.objects.get(bar_code=book)
            name = form.cleaned_data['studentID']
            
            studentid = Student.objects.get(studentID=name)
            IssuedBook.objects.filter(studentID=name, barcode=book).delete()
            return redirect('view_issue_book')
    context = {'form':form}
    return render(request, 'library/book_return.html', context)


def student(request):
    return render(request, 'library/student.html')

def register_new_student(request):
    form = StudentRegisterForm()
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('student')
    return render(request, 'library/register_new_student.html', {'form':form})

def view_new_student(request):
    student_list = Student.objects.all()
    student_filter = StudentFilter(request.GET, queryset=student_list)
    context = {'view_new_student': Student.objects.all(), 'filter':student_filter}
    return render(request, 'library/view_new_student.html', context)

def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('view_new_student')

def update_student(request, pk):
    students = Student.objects.get(id=pk)
    form = StudentRegisterForm(instance=students)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST, instance=students)
        if form.is_valid():
            form.save()
            return redirect('view_new_student')
    context = {'form':form}
    return render(request, 'library/update_student.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def about_view(request):
    return render(request, 'library/about.html')

def contact_view(request):
    return render(request, 'library/contact.html')
