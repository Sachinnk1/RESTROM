# Generated by Django 5.0.6 on 2024-10-23 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
