from django.contrib import admin

# Register your models here.

from .models import Date, Entry

admin.site.register(Date)
admin.site.register(Entry)