from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    # create relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # add any additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username   # built-in attr of django.contrib.models.User
