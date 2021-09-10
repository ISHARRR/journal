from datetime import datetime, date

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class contact(models.Model):


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name + " " + self.last_name + ": " + self.phone

    class Meta:
        order_with_respect_to = 'user'


class Stack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.language + ": " + self.description

    class Meta:
        order_with_respect_to = 'user'


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    # contact = models.CharField(max_length=11)
    contact = models.ManyToManyField(Contact)
    stack = models.ManyToManyField(Stack)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
