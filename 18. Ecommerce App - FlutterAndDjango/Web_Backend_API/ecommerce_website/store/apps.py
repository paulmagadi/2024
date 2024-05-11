from django.apps import AppConfig
from django.db.models.signals import post_save



class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        # Import the signal handler function here to avoid import loop issues
        from .signals import update_is_new
        
        # Connect the signal handler function to the post_save signal of the Product model
        Product = self.get_model('Product')
        post_save.connect(update_is_new, sender=Product)
