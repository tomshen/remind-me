from django.core.management.base import NoArgsCommand

from reminders.models import Reminder
from datetime import date

class Command(NoArgsCommand):
	help = 'Checks if any reminders need to be sent'

	def handle_noargs(self, **options):
		for reminder in Reminder.objects.all().order_by('date'):
			today = date.today()
			if reminder.date == today and not reminder.sent:
				reminder.send()
			if reminder.date > today:
				break