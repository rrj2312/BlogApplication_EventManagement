from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.register, name='register'),
    path('registration/success/<str:registration_id>/', views.registration_success, name='registration_success'),
    path('scanner/', views.qr_scanner, name='qr_scanner'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/event/<int:event_id>/attendance/', views.event_attendance_live, name='event_attendance_live'),
    path('admin/event/<int:event_id>/export/', views.export_attendance, name='export_attendance'),
]