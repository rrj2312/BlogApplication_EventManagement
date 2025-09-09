from django.db import models
from django.utils import timezone
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def total_registrations(self):
        return self.registrations.count()

    @property
    def total_attendance(self):
        return self.registrations.filter(attendance__isnull=False).count()

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    registration_id = models.CharField(max_length=20, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.registration_id:
            self.registration_id = self.generate_registration_id()
        
        super().save(*args, **kwargs)
        
        if not self.qr_code:
            self.generate_qr_code()
            super().save(update_fields=['qr_code'])

    def generate_registration_id(self):
        return f"REG{str(uuid.uuid4())[:8].upper()}"

    def generate_qr_code(self):
        qr_data = f"{self.registration_id}|{self.event.id}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        
        filename = f'qr_code_{self.registration_id}.png'
        self.qr_code.save(filename, File(buffer), save=False)

    def __str__(self):
        return f"{self.name} - {self.event.name}"

    @property
    def is_attended(self):
        return hasattr(self, 'attendance')

class Attendance(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE, related_name='attendance')
    timestamp = models.DateTimeField(auto_now_add=True)
    scanned_by = models.CharField(max_length=100, blank=True)  # Can be admin username or system

    def __str__(self):
        return f"{self.registration.name} - {self.registration.event.name} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']