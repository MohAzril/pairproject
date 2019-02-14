from django.contrib import admin
from .models import Mall,Park


# Register your models here.
my_model = [Mall,Park]
admin.site.register(my_model)