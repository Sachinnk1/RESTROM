# Generated by Django 5.0.6 on 2024-09-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Name')),
                ('Price', models.IntegerField(verbose_name='Price')),
                ('Category', models.CharField(max_length=100, verbose_name='Category')),
                ('Image', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('Quantity', models.CharField(max_length=100, verbose_name='Quantity')),
                ('Description', models.CharField(max_length=1000, verbose_name='Description')),
            ],
        ),
    ]
