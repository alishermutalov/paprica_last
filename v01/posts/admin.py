from django.contrib import admin

# Register your models here.

from .models import News, Contact, Case , Service

# Register your models here.

admin.site.register(News)
admin.site.register(Contact)
admin.site.register(Case)
admin.site.register(Service)