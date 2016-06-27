from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.db.models import signals

COLUMBIA = 'Columbia'
GREENVILLE = 'Greenville'
SPARTANBURG = 'Spartanburg'
CITY_CHOICES = ((COLUMBIA, 'Columbia'), (GREENVILLE, 'Greenville'), (SPARTANBURG, 'Spartanburg'))

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    city = models.CharField(max_length=30, choices=CITY_CHOICES, default=GREENVILLE)

    def __str__(self):
        return self.user


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name="subcategories")
    subcategory_name = models.CharField(max_length=30)

    def __str__(self):
        return self.subcategory_name


class Listing(models.Model):
    listing_category = models.ForeignKey(Category)
    listing_subcategory = models.ForeignKey(SubCategory)
    city = models.CharField(max_length=30, choices=CITY_CHOICES, default=GREENVILLE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    value = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="listing_photos", null=True, blank=True, verbose_name="Listing Photo")

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url

    def __str__(self):
        return self.title


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")

    if created:
        Profile.objects.create(user=instance)
