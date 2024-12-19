from django.db import models


# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255)
    keywoards = models.CharField(max_length=255)
    description = models.TextField(max_length=550)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    smpt_server= models.CharField(max_length=255)
    smpt_email= models.CharField(max_length=255)
    smpt_password= models.CharField(max_length=255)
    smpt_port= models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    icon = models.ImageField(null=False, upload_to='images/')
    aboutus = models.TextField(max_length=550)
    contact = models.CharField(max_length=255)
