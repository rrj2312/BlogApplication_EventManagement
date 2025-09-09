
from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Registration, Attendance

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location', 'total_registrations', 'total_attendance', 'is_active']
    list_filter = ['is_active', 'date']
    search_fields = ['name', 'location']
    readonly_fields = ['created_at']
    
    def total_registrations(self, obj):
        return obj.registrations.count()
    total_registrations.short_description = 'Registrations'
    
    def total_attendance(self, obj):
        return obj.registrations.filter(attendance__isnull=False).count()
    total_attendance.short_description = 'Attendance'

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'registration_id', 'event', 'is_attended', 'created_at']
    list_filter = ['event', 'created_at']
    search_fields = ['name', 'email', 'registration_id']
    readonly_fields = ['registration_id', 'qr_code_display', 'created_at']
    
    def qr_code_display(self, obj):
        if obj.qr_code:
            return format_html('<img src="{}" width="150" height="150" />', obj.qr_code.url)
        return "No QR Code"
    qr_code_display.short_description = 'QR Code'
    
    def is_attended(self, obj):
        return hasattr(obj, 'attendance')
    is_attended.boolean = True
    is_attended.short_description = 'Attended'

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['registration_name', 'registration_email', 'event_name', 'timestamp', 'scanned_by']
    list_filter = ['timestamp', 'registration__event']
    search_fields = ['registration__name', 'registration__email']
    readonly_fields = ['timestamp']
    
    def registration_name(self, obj):
        return obj.registration.name
    registration_name.short_description = 'Name'
    
    def registration_email(self, obj):
        return obj.registration.email
    registration_email.short_description = 'Email'
    
    def event_name(self, obj):
        return obj.registration.event.name
    event_name.short_description = 'Event'