from django.db import models
from django.core.mail import send_mail

class Reminder(models.Model):
	email = models.EmailField('email address', max_length = 254)
	date = models.DateField('reminder date')
	message = models.TextField(max_length = 250)
	sent = models.BooleanField()

	def __unicode__(self):
		return 'reminder for ' + self.email + ' on ' + self.date.isoformat()

	def send(self):
		try:
			send_mail('Scheduled reminder', self.message, 'Remind Me! reminders@app9864910.mailgun.org', [self.email])
			self.sent = True
			self.save()
			print 'reminder sent: ' + self.email + ' on ' + self.date.isoformat()
		except:
			print 'reminder failed: ' + self.email + ' on ' + self.date.isoformat()