from django.db import models
from django.forms import ModelForm
from admin_app.models import *
from web_app.models import *

# Create your models here.
class sliders(models.Model):
    title = models.CharField(max_length=150)
    meta = models.CharField(max_length=500)
    image = models.FileField(upload_to='media/')

class obj_slider(ModelForm):
    class Meta:
        model = sliders
        fields = ["title","meta","image"]


class web_user(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class web_user_form(ModelForm):
    class Meta:
        model = web_user
        fields = ["username","email","password"]

class cart(models.Model):
    user_id = models.ForeignKey(web_user,on_delete=models.CASCADE)
    product_id = models.ForeignKey(product_data,on_delete=models.CASCADE)
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.IntegerField(max_length=10,default=0)

class cart_form(ModelForm):
    class Meta:
        model = cart
        fields = ["user_id","product_id","qty","price","amount"]

class checkout(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    pro_name = models.CharField(max_length=100)

class checkout_form(ModelForm):
    class Meta:
        model = checkout
        fields = ["name","email","contact","address","pin","pro_name"]