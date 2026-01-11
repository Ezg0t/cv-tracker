from django.urls import path
from . import views

app_name = 'job_offers'

urlpatterns = [
    path('', views.job_offer_list, name='list'),
    path('change-status/<int:pk>/', views.change_status, name='change_status'),
    path('add-application/<int:pk>/', views.add_application, name='add_application')
]
