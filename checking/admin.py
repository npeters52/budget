from django.contrib import admin
from .models import Debit, Credit

# Register your models here.

admin.site.register(Debit)
admin.site.register(Credit)