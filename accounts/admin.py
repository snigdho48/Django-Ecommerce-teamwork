from django.contrib import admin
from .models import Phone


# Register your models here.

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['New', "phone_num"]


admin.site.register(Phone, PhoneAdmin)
