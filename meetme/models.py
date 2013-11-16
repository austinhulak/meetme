from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractUser):
    phone = PhoneNumberField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='account_images')
    tagline = models.TextField()


class Review(models.Model):
    rating = models.IntegerField()
    author = models.ForeignKey(Account, related_name='review_author')
    account = models.ForeignKey(Account)
    comment = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='category_images')


class Activity(models.Model):
    account = models.ForeignKey(Account)
    tagline = models.CharField(max_length=140)
    description = models.TextField()
    category = models.ForeignKey(Category)
