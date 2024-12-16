from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    keywoards = models.CharField(max_length = 255)
    description = models.TextField(max_length=550)
    image = models.ImageField(null = False, upload_to='images/')
    slug = models.SlugField(null = False, unique = True)