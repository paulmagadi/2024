# Generated by Django 5.0.2 on 2024-03-10 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]