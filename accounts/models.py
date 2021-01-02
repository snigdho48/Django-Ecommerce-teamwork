from django.db import models
from django.contrib.auth.models import User, auth, AbstractBaseUser, UserManager


class Phone(models.Model):
    phone_num = models.CharField(max_length=11, default=None)
    New = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __self__(self):
        return self.phone




