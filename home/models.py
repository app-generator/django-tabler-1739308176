# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Endpoints(models.Model):

    #__Endpoints_FIELDS__
    url = models.TextField(max_length=255, null=True, blank=True)
    root_name = models.TextField(max_length=255, null=True, blank=True)
    ip = models.TextField(max_length=255, null=True, blank=True)
    alive = models.BooleanField()
    cdn = models.BooleanField()
    response_code = models.IntegerField(null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=255, null=True, blank=True)
    origin = models.TextField(max_length=255, null=True, blank=True)

    #__Endpoints_FIELDS__END

    class Meta:
        verbose_name        = _("Endpoints")
        verbose_name_plural = _("Endpoints")



#__MODELS__END
