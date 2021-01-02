
from django.contrib import admin
from django.urls import path ,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),


]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)