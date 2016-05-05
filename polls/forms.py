from django import forms

from .models import ToDo

class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ('title',
        	'priority',
        	'progress',
        	'description',
        	'name',
        	'deadline_day',
        	'deadline_month',
        	'deadline_year')
