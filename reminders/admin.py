from reminders.models import Reminder
from django.contrib import admin

class ReminderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['email', 'date', 'message', 'sent']}),
    ]
    list_display = ('email', 'date', 'message', 'sent')
    list_filter = ['date']
    search_fields = ['email', 'message']
    date_hierarchy = 'date'

admin.site.register(Reminder, ReminderAdmin)