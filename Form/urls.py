from django.contrib import admin
from django.urls import path
from regform.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',form),
    path('StolenData',showdata)
]
