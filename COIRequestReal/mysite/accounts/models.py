from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class Requesters(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default='')

    address_line1 = models.CharField(max_length=200,default='')
    address_line2 = models.CharField(blank=True, null=True, max_length=200,default='' )
    # state = models.ForeignKey('States', null=True, blank=True)
    city = models.CharField(default='', max_length=200)
    zipcode = models.PositiveIntegerField(validators=[MaxValueValidator(99999)],default=0)
    fax = models.IntegerField(blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(max_length=100, default='')
    phone = models.IntegerField(default=0)


# this method is mainly to create new users inside of the django admin


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        user = Requesters.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

# class States(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=96)
#     state_abbr = models.CharField(max_length=24, blank=True)
#
#     # Define the __unicode__ method, which is used by related models by default.
#     def __unicode__(self):
#         return self.state_abbr
