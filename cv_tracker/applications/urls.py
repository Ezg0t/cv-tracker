from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('', views.application_list, name='list'),
    path('change-status/<int:pk>/', views.change_status, name='change_status'),
    path('delete/<int:pk>/', views.delete_application, name='delete'),
]