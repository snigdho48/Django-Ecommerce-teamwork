from django.contrib import admin
from .models import *


# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['user', "phone_num"]


admin.site.register(Phone, PhoneAdmin)


class UserprofileAdmin(admin.ModelAdmin):
    list_display = ['user', "phone", "Address", "date_created"]


admin.site.register(Userprofile, UserprofileAdmin)
