from django.forms import ModelForm, ValidationError
from reminders.models import Reminder
from datetime import date

class ReminderForm(ModelForm):
    class Meta:
        model = Reminder
        exclude = ('sent', )
    def clean_date(self):
        data = self.cleaned_data
        if data['date'] < date.today():
            raise ValidationError("Even we don't have access to time travel!")
        return data['date']