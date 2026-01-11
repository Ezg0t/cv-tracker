from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import JobApplication, StatusHistory


@receiver(pre_save, sender=JobApplication)
def track_status_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    old = JobApplication.objects.get(pk=instance.pk)
    if old.status != instance.status:
        StatusHistory.objects.create(
            application=instance,
            old_status=old.status,
            new_status=instance.status
        )
