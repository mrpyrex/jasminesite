from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display    = ('first_name', 'last_name', 'email', 'phone', 'message', 'date')
    search_fields   = ('first_name', 'last_name', 'email', 'phone',)
admin.site.register(Contact, ContactAdmin)
