from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ Maintains delivery information and order history """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_address_line1 = models.CharField(
        max_length=100, null=True, blank=True)
    default_address_line2 = models.CharField(
        max_length=100, null=True, blank=True)
    default_city_or_town = models.CharField(
        max_length=50, null=True, blank=True)
    default_county_or_state = models.CharField(
        max_length=50, null=True, blank=True)
    default_postcode_or_zip = models.CharField(
        max_length=15, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)
    default_telephone_number = models.CharField(
        max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """ Creates/updates a user profile """
    if created:
        UserProfile.objects.create(user=instance)
    # For existing user this will just save their profile
    instance.userprofile.save()
