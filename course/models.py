from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    keywoards = models.CharField(max_length=255)
    description = models.TextField(max_length=550)
    image = models.ImageField(null=False, upload_to='images/')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    subject_tutor = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField(max_length=550)
    image = models.ImageField(null=False, upload_to='images/')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)

    def __str__(self):
        return self.name


class Tutor(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)

    def __str__(self):
        return self.name
