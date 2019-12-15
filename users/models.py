from django.contrib.auth.models import User, AbstractBaseUser
from django.db import models
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _
# from positions.models import Global, Local

class User(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=150, blank=True)
    password = models.CharField(_('password'), max_length=128)
    image = models.ImageField(blank=True)
    years_old = models.CharField(max_length=30, blank=True)
    phone = models.CharField(blank=True, max_length=30, help_text='Contact phone number')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # global_position = models.ForeignKey(Global,blank=True, on_delete=models.CASCADE)
    # local_position = models.ForeignKey(Local,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return " %s  %s" % (self.id, self.username)