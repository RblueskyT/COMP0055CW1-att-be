from django.contrib import admin

# Register your models here.
from .models import StolenToken
admin.site.register(StolenToken)
