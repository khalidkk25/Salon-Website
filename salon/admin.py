from django.contrib import admin
from salon.models import *

admin.site.site_header = "SnipSnap | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message', 'added_on', ]

class PendingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'date', 'time', 'stylist', 'status']
    list_filter = ['status']
    search_fields = ['name', 'email', 'phone', 'date', 'time', 'stylist']

class AcceptedAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'date', 'time', 'stylist', 'status']

class RejectedAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'date', 'time', 'stylist', 'status']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Total, PendingAdmin)
admin.site.register(Accepted, AcceptedAdmin)
admin.site.register(Rejected, RejectedAdmin)

