from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    usertype=models.CharField(max_length=50)
    

class Chef(models.Model):
    chef_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100,verbose_name='Name')
    Place=models.CharField(max_length=100,verbose_name='Position')
    Contact=models.BigIntegerField(verbose_name='Contact')
    Salary=models.IntegerField(verbose_name='Salary')
    Qualification=models.CharField(max_length=100,verbose_name='Qualification')
    Experiance=models.CharField(max_length=100,verbose_name='Experiance')


class Customers(models.Model):
    customers_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100,verbose_name='Name')
    Phone=models.BigIntegerField(verbose_name='Phone')
    Address=models.CharField(max_length=1000,verbose_name='Address')
    Status=models.IntegerField(verbose_name='Status',default=0)





class Menu1(models.Model):
    Name = models.CharField(max_length=100, verbose_name='Name')
    Price = models.IntegerField(verbose_name='Price')
    Category = models.CharField(max_length=100, verbose_name='Category')
    Image = models.ImageField(verbose_name='Image', upload_to='images/')  # ImageField for image upload
    Quantity = models.CharField(max_length=100, verbose_name='Quantity')
    Description = models.CharField(max_length=1000, verbose_name='Description')

    def __str__(self):
        return self.Name




class Booking(models.Model):
    booking_id=models.ForeignKey(Customers,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100,verbose_name='Name')
    Phone=models.BigIntegerField(verbose_name='Phone')
    Email=models.EmailField(verbose_name='Email')
    Persons=models.IntegerField(verbose_name='Person')
    Date=models.DateField(verbose_name='Date')
    Status=models.IntegerField(verbose_name='Status',default=0)












class CartItem(models.Model):
    cust_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu1, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.menu_item.Name}"

    def get_total_price(self):
        return self.menu_item.Price * self.quantity
    

    