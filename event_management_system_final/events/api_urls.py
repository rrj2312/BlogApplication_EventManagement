from django.urls import path
from . import views

urlpatterns = [
    path('scan-qr/', views.scan_qr, name='api_scan_qr'),
    path('live-attendance/<int:event_id>/', views.get_live_attendance, name='api_live_attendance'),
]