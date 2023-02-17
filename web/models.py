from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class Post(models.Model):
    internTitle = models.CharField(max_length=100)
    companyAddress = models.CharField(max_length=200)
    internshipDescription = models.CharField(max_length=500)
    comName = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    tPhone = models.CharField(max_length=20)
