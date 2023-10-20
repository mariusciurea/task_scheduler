from django.forms import ModelForm
from django import forms
from .models import Tasks
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_name', 'date_deadline']
        widgets = {
            "date_deadline": DateTimePickerInput,
        }


# class TaskForm(forms.Form):
#     task_name = forms.CharField(label="task", max_length=100)
#     date_deadline = forms.DateTimeField(label='task-deadline')
