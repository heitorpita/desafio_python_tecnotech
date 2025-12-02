from django.urls import path
from . import views

urlpatterns = [
    # html
    path('', views.enrollment_list, name='enrollment_list'),
    path('nova/', views.enrollment_create, name='enrollment_create'),
    path('financeiro/', views.financial_dashboard, name='financial_dashboard'),
    path('relatorio/aluno/<int:student_id>/', views.student_history, name='student_history'),
    path('dashboard/', views.general_dashboard, name='general_dashboard'),

    # api - matriculas
    path('api/', views.EnrollmentListCreateAPI.as_view(), name='enrollment_api_list'),
    path('api/<int:pk>/', views.EnrollmentRetrieveUpdateDeleteAPI.as_view(), name='enrollment_api_detail'),
    
    # api - pagar matricula
    path('api/<int:pk>/pagar/', views.MarkAsPaidAPI.as_view(), name='enrollment_mark_paid'),

    #api financeiro
    path('api/financeiro/totais/', views.FinancialReportAPI.as_view(), name='financial_api_totals'),

    path('api/financeiro/global/', views.GlobalFinanceAPI.as_view(), name='financial_api_global'),
]
