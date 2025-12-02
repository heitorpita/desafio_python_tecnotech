from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', include('students.urls')),
    path('cursos/', include('courses.urls')),
    path('matriculas/', include('enrollments.urls')),
]
