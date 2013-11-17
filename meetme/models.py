from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Account(AbstractUser):
    phone = PhoneNumberField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='account_images')
    image_url = models.TextField(blank=True)
    tagline = models.TextField(blank=True)
    category = models.ForeignKey('Category', null=True)
    available = models.BooleanField(default=False)


class Review(models.Model):
    rating = models.IntegerField()
    author = models.ForeignKey(Account, related_name='review_author')
    account = models.ForeignKey(Account)
    comment = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='category_images', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)


class Reservation(models.Model):
    local = models.ForeignKey(Account, related_name='local')
    visitor = models.ForeignKey(Account, related_name='visitor')
    day = models.IntegerField()
    time_range = models.IntegerField()
    local_response = models.TextField(blank=True)

    @classmethod
    def post_save(cls, sender, instance, **kwargs):
        if not kwargs['created']:
            return

        print 'send text!'
models.signals.post_save.connect(Reservation.post_save, sender=Reservation)
