from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


class Phone(models.Model):
    phone_num = models.CharField(max_length=11, default=None)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __self__(self):
        return self.phone



