from django.urls import path
from . import views
from enrollments.views import StudentEnrollmentsAPI 

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('edit/<int:id>/', views.student_edit, name='student_edit'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    
    #api
    path('api/', views.StudentListCreateAPI.as_view(), name='student_api_list'),
    path('api/<int:pk>/', views.StudentRetrieveUpdateDeleteAPI.as_view(), name='student_api_detail'),
    path('api/alunos/<int:student_id>/matriculas/', StudentEnrollmentsAPI.as_view(), name='student_enrollments_api'),
]
