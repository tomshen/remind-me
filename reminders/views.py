from django.template import Context, loader
from reminders.models import Reminder
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from reminders.forms import ReminderForm

def home(request):
	if request.method == 'POST':
		form = ReminderForm(request.POST)
		if form.is_valid():
			reminder = form.save(commit=False)
			reminder.sent = False
			reminder.save()
			return render(request, 'reminders/index.html', {'scheduled': True})
	else:
		form = ReminderForm()
	return render(request, 'reminders/index.html', {'form': form, 'scheduled': False})