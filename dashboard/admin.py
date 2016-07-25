from django.contrib import admin
from dashboard.models import Room, Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'is_read', 'created_at')

# registering models
admin.site.register(Room)
admin.site.register(Message, MessageAdmin)
