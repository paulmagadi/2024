from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Product

@receiver(post_save, sender=Product)
def update_is_new(sender, instance, **kwargs):
    """
    Signal handler function to update the 'is_new' field of the Product model after 7 days.
    """
    if instance.created_at >= timezone.now() - timezone.timedelta(days=7):
        instance.is_new = True
        instance.save()
    else:
        instance.is_new = False
        instance.save()
