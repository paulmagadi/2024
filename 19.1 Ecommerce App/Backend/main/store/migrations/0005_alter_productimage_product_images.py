# Generated by Django 5.0.6 on 2024-05-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_productimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product_images',
            field=models.ImageField(null=True, upload_to='uploads/products', verbose_name='Image'),
        ),
    ]