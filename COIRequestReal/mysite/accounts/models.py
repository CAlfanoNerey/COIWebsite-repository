from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

TITLE_STATES = [
    ('1','Alabama'), ('2','Alaska'), ('3','American Samoa'), ('4','Arizona'), ('5','Arkansas'), ('6','California'), ('7','Colorado'), ('8','Connecticut'), ('9','Delaware'),
    ('10','District of Columbia'), ('11','Florida'), ('12','Georgia'), ('13','Guam'), ('14','Hawaii'), ('15','Idaho'), ('16','Illinois'), ('17','Indiana'), ('18','Iowa'), ('19','Kansas'),
    ('20','Kentucky'), ('21','Louisiana'), ('22','Maine'), ('23','Maryland'), ('24','Massachusetts'), ('25','Michigan'), ('26','Minnesota'), ('27','Minor Outlying Islands'),
    ('28','Mississippi'), ('29','Missouri'), ('30','Montana'), ('31','Nebraska'), ('32','Nevada'), ('33','New Hampshire'), ('34','New Jersey'), ('35','New Mexico'), ('36','New York'),
    ('37','North Carolina'), ('38','North Dakota'), ('39','Northern Mariana Islands'), ('40','Ohio'), ('41','Oklahoma'), ('42','Oregon'), ('43','Pennsylvania'), ('44','Puerto Rico'),
    ('45','Rhode Island'), ('46','South Carolina'), ('47','South Dakota'), ('49','Tennessee'), ('50','Texas'), ('51','U.S. Virgin Islands'), ('52','Utah'), ('53','Vermont'), ('54','Virginia'),
    ('55','Washington'), ('56','West Virginia'), ('57','Wisconsin'), ('58','Wyoming'),

]

class Requesters(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, default='')

    address_line1 = models.CharField(max_length=200, default='')
    address_line2 = models.CharField(blank=True, null=True, max_length=200, default='')
    # state = models.ForeignKey('States', null=True, blank=True)
    city = models.CharField(default='', max_length=200)
    state_or_territory = models.CharField(max_length=40, choices=TITLE_STATES, default='')
    zipcode = models.PositiveIntegerField(blank =True, null=True, validators=[MaxValueValidator(99999)])
    fax = models.IntegerField(blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(max_length=100, default='')
    phone = models.IntegerField(default=0)


class Recipient(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address_line1 = models.CharField(blank=True, null=True,max_length=200)
    address_line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state_or_territory = models.CharField(max_length=40, choices=TITLE_STATES)
    zipcode = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    email = models.CharField(max_length=200)
    fax = models.IntegerField(blank=True, null=True)


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
