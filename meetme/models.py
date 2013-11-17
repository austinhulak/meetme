from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.db import models
from django.template import Context, loader

from phonenumber_field.modelfields import PhoneNumberField

from utils.twillio import send_text


class Account(AbstractUser):
    phone = PhoneNumberField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='account_images')
    image_url = models.TextField(blank=True)
    tagline = models.TextField(blank=True)
    category = models.ForeignKey('Category', null=True)
    available = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode("{} {}".format(self.first_name, self.last_name))


class Review(models.Model):
    rating = models.IntegerField()
    headline = models.TextField(blank=True)
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
	reservation = instance
	context = Context({
	    'reservation': reservation,
	    'site': Site.objects.get(pk=settings.SITE_ID),
	})

        if kwargs['created']:
		phone_number = reservation.local.phone.raw_input
		template = 'meetme/text/request.sms'
	else:
		phone_number = reservation.visitor.phone.raw_input
		template = 'meetme/text/response.sms'

	rendered = loader.render_to_string(
	    template,
	    context_instance=context
	)

        send_text(rendered, phone_number)

models.signals.post_save.connect(Reservation.post_save, sender=Reservation)
