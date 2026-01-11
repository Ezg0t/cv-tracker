from django.db import models
from django.contrib.auth.models import User

STATUS_SEQUENCE = ['sent', 'review', 'interview', 'offer', 'rejected']

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Wysłane'),
        ('review', 'W trakcie przeglądu'),
        ('interview', 'Rozmowa'),
        ('offer', 'Oferta'),
        ('rejected', 'Odrzucone'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='sent'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} – {self.position}"
    
    def get_status_display_name(self):
        return self.get_status_display()
    
    def get_next_status(self):
        idx = STATUS_SEQUENCE.index(self.status)
        if idx < len(STATUS_SEQUENCE) - 1:
            return STATUS_SEQUENCE[idx + 1]
        return self.status

    def get_prev_status(self):
        idx = STATUS_SEQUENCE.index(self.status)
        if idx > 0:
            return STATUS_SEQUENCE[idx - 1]
        return self.status

    def get_next_status_display(self):
        status_map = dict(self.STATUS_CHOICES)
        return status_map[self.get_next_status()]

    def get_prev_status_display(self):
        status_map = dict(self.STATUS_CHOICES)
        return status_map[self.get_prev_status()]


class StatusHistory(models.Model):
    application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name='history'
    )
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_at = models.DateTimeField(auto_now_add=True)
