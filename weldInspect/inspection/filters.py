# from django.forms import widgets
from django import forms
from .models import *
import django_filters

class DateInput(forms.DateInput):
    input_type = 'date'

class ProjectFilter(django_filters.FilterSet):
    #django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    data_perform = django_filters.DateFilter(
        widget=DateInput(
            attrs={
                'class': 'datepicker'
            }
        )
    )
    class Meta:
        model=project
        fields=['project_number','data_perform','project_user_name']
        