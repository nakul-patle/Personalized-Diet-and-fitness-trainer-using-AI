from django.db import models


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.manager import Manager
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email_confirmed=models.BooleanField(default=False,unique=False)

@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Product(models.Model):
    name=models.CharField(max_length=50)
    categorys=models.ForeignKey('Category',on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='products/')
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(categorys=category_id)
        else:
            return Product.get_all_products()
    @staticmethod
    def get_product_id(ids):
        return Product.objects.filter(id__in=ids)



class Category(models.Model):
    name=models.CharField(max_length=30)

    @staticmethod
    def get_all_category():
        return Category.objects.all()
    def __str__(self):
        return self.name

class Order(models.Model):
    name=models.CharField(max_length=50,default='')
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='orders/')    
    price=models.IntegerField()
    Address=models.CharField(max_length=255,default='')
    phone=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    payment_id=models.CharField(max_length=100,default='')
    status=models.BooleanField(default=False)
    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id)


class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=1000)
    objects=Manager()

class donar(models.Model):
    name=models.CharField(max_length=50)
    lname=models.CharField(max_length=60)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=300)
    Aadhaar=models.FileField(upload_to='media/')
    plant=models.CharField(max_length=100)
    countplants=models.CharField(max_length=10)
    plantsimage=models.ImageField(upload_to="mediasource/")
    objects=Manager()
    def __str__(self):
        return self.plant


    



    
    