# Generated by Django 5.0.6 on 2024-10-21 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_cart_cartitem'),
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
