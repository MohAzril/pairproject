from django.contrib import admin
from .models import Mall

my_model = [Mall]
admin.site.register(my_model)

# Register your models here.
