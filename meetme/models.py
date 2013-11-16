from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractUser):
    phone = PhoneNumberField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='account_images')
    tagline = models.TextField(blank=True)


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
