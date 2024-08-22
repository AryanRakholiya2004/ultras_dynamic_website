from django.db import models
from django.forms import ModelForm

# Create your models here.

class user_data(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class userForm(ModelForm):
    class Meta:
        model = user_data
        fields = ("username","email","password")

class user_register(models.Model):
    added_by = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    image = models.FileField(upload_to='media/user_data/',default='')

class user_register_form(ModelForm):
    class Meta:
        model = user_register
        fields = ("added_by","name","email","contact","gender","city","image")


class categories_data(models.Model):
    category = models.CharField(max_length=100)
    image = models.FileField(upload_to='media/categories/')

class categories_form(ModelForm):
    class Meta:
        model = categories_data
        fields = ("category","image")

class subcategories_data(models.Model):
    subcate = models.CharField(max_length=100)
    image = models.FileField(upload_to='media/subcate/')
    category = models.ForeignKey(categories_data,on_delete= models.CASCADE)

class subcate_form(ModelForm):
    class Meta:
        model = subcategories_data
        fields = ("subcate","image","category")

class petacategories_data(models.Model):
    petacate = models.CharField(max_length=100)
    category = models.ForeignKey(categories_data,on_delete=models.CASCADE)
    subcate = models.ForeignKey(subcategories_data,on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/petacate/')

class petacate_form(ModelForm):
    class Meta:
        model = petacategories_data
        fields = ("petacate","category","subcate","image")

class product_data(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=5000)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.FileField(upload_to='media/products/')
    category = models.ForeignKey(categories_data,on_delete=models.CASCADE)
    subcate = models.ForeignKey(subcategories_data,on_delete=models.CASCADE)
    petacate = models.ForeignKey(petacategories_data,on_delete=models.CASCADE)

class product_form(ModelForm):
    class Meta:
        model = product_data
        fields = ("name","desc","price","quantity","image","category","subcate","petacate")