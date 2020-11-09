from django.urls import path, include
from . import views
from django.conf.urls import url



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('book', views.book, name='book'),
    path('add_book/', views.add_book, name='add_book'),
    path('view_book/', views.view_book, name='view_book'),
    path('book_delete/<int:pk>', views.book_delete, name='book_delete'),
    path('update_book/<str:pk>/', views.update_book, name='update_book'),
    path('issue_book/', views.issue_book, name='issue_book'),
    path('issue_new_book/', views.issue_new_book, name='issue_new_book'),
    path('view_issue_book/', views.view_issue_book, name='view_issue_book'),
    path('student/', views.student, name='student'),
    path('register_new_student/', views.register_new_student, name='register_new_student'),
    path('student_delete/<int:pk>', views.student_delete, name='student_delete'),
    path('update_student/<str:pk>/', views.update_student, name='update_student'),
    path('view_new_student/', views.view_new_student, name='view_new_student'),
    path('return_book/', views.return_book, name='return_book'),
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

]

