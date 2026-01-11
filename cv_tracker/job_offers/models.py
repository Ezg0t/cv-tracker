from django.db import models

class JobOffer(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'NOWE'),
        ('CHECKED', 'SPRAWDZONE'),
        ('SENT', 'WYSŁANO CV'),
    ]
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    url = models.URLField(unique=True)
    posted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='NEW',
    )

    def __str__(self):
        return f"{self.title} @ {self.company_name} [{self.get_status_display()}]"
