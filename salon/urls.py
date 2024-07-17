from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index') ,
    path('about/', views.about, name='about'), 
    path('services/', views.services, name='services'), 
    path('booking/', views.booking, name='booking'),
    path('terms_and_conditions/', views.terms, name='terms'),
    path('privacy_policy/', views.privacy, name='privacy'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('pending_bookings/', views.pending_bookings, name='pending_bookings'),
    path('accepted_bookings/', views.accepted_bookings, name='accepted_bookings'),
    path('rejected_bookings/', views.rejected_bookings, name='rejected_bookings'),
    path('contact_review/', views.contact_review, name='contact_review'),
    

]