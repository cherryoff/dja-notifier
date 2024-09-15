from django.contrib import admin

from .models import Tag, Recipient, NotificationTemplate, Check

admin.site.register(Recipient)
admin.site.register(Check)
admin.site.register(NotificationTemplate)
admin.site.register(Tag)
