
from django.db import models
from datetime import datetime
# Create your models here.
   

class Contact(models.Model):
    
   
    name= models.CharField(blank=True,max_length=20)
    email= models.CharField(blank=True,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    message= models.TextField(blank=True,max_length=255)    
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    updated_at=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name
    
    
    
class Bookapp(models.Model):
    fname= models.CharField(blank=True,max_length=20)
    lname= models.CharField(blank=True,max_length=20)
    
    def __str__(self):
        return self.fname
    