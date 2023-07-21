from django.contrib import admin
from .models import *
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=['name','description','price','categorys','image']

# admin.site.register(Product,AdminProduct)

class AdminCategory(admin.ModelAdmin):
    list_display=['name']
# class AdminOrder(admin.ModelAdmin):
#     list_display=['customer']

class AdminContact(admin.ModelAdmin):
    list_display=['name','email','subject','message']


# admin.site.register(Category,AdminCategory)
# admin.site.register(Order)
admin.site.register(donar)
admin.site.register(Contact,AdminContact)
