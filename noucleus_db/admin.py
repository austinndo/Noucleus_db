from django.contrib import admin
from .models import Gene, User, Guide

# Register your models here.
admin.site.register(Gene)
admin.site.register(User)
admin.site.register(Guide)
