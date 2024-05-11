from django.db import models

# Create your models here.
class MobileBanner(models.Model):
    image = models.ImageField(upload_to='uploadsbanners/', verbose_name="Image")
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name="Caption")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.caption