from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media/')

    def __str__(self):
        return str(self.user)


class Author(models.Model):
    pass
