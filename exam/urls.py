from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/<int:pk>/', views.group_detail, name='group_detail'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('students/<int:student_id>/marks/create/', views.mark_create, name='student_mark_create'),
    path('marks/', views.mark_list, name='mark_list'),
    path('marks/create/', views.mark_create, name='mark_create'),
    path('marks/<int:pk>/update/', views.mark_update, name='mark_update'),
    path('marks/<int:pk>/delete/', views.mark_delete, name='mark_delete'),
]
