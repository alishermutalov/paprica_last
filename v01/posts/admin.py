from django.contrib import admin

# Register your models here.

from .models import News, Contact

# Register your models here.

admin.site.register(News)
admin.site.register(Contact)