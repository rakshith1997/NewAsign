from django.conf import settings
from django.db import models
from multiselectfield import MultiSelectField


class Student(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Choices(models.Model):
    description = models.CharField(max_length=300)


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Student)


MY_CHOICES = ((1, Student.pk),
              (2, Student.name),
              (3, Student.email),
              (4, Student.website),
              (5, 'Value5'))


class MyModel(models.Model):
    my_field = MultiSelectField(choices=MY_CHOICES,
                                max_choices=10,
                                max_length=10)
