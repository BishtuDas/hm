from django.contrib import admin

from .models import Customer, Company, Marketing, Website

admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Marketing)
admin.site.register(Website)
