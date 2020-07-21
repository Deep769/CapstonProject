from django.db import models
from phone_field import PhoneField


class Payment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=6)
    name_on_card = models.CharField(max_length=100)
    card_num = models.CharField(max_length=16)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)


class Application(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    date = models.DateField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    file = models.FileField(upload_to='files')
    deposit = models.DecimalField(max_digits=6, decimal_places=2)
    house = models.CharField(max_length=100)
