from django.urls import path
from . import views

urlpatterns = [
    # Rotas HTML
    path('', views.course_list, name='course_list'),
    path('create/', views.course_create, name='course_create'),
    path('edit/<int:id>/', views.course_edit, name='course_edit'),
    path('delete/<int:id>/', views.course_delete, name='course_delete'),

    # Rotas API
    path('api/', views.CourseListCreateAPI.as_view(), name='course_api_list'),
    path('api/<int:pk>/', views.CourseRetrieveUpdateDeleteAPI.as_view(), name='course_api_detail'),
    path('api/stats/', views.CourseStatsAPI.as_view(), name='course_api_stats'),
    path('api/relatorio-sql/', views.SQLRawReportAPI.as_view(), name='course_sql_report'),
]
