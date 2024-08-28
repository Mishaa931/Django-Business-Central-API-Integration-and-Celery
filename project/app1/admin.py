from django.contrib import admin
from .models import *
from django.apps import apps

from django.contrib import admin


app_models = apps.get_app_config('app1').get_models()
for model in app_models:
    class CustomAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]
        list_filter = [field.name for field in model._meta.fields]
        search_fields = [field.name for field in model._meta.fields]
    admin.site.register(model, CustomAdmin)
