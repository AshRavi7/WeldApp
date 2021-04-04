from django.forms import fields
from .models import activity_inspection_action, drawing, gallery, heat_calc, project,location_discipline, weld, weld_action
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class projectForm(forms.ModelForm):
    class Meta:
        model = project
        fields=['project_number','report_number','data_perform']
        widgets = {
            'data_perform': DateInput(),
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = location_discipline
        fields=['location_name','discipline_name']

class DrawingForm(forms.ModelForm):
    class Meta:
        model = drawing
        fields=['drawing_number']
    
class WeldForm(forms.ModelForm):
    class Meta:
        model = weld
        fields=['weld_number']

class WeldActionForm(forms.ModelForm):
    class Meta:
        model = weld_action
        fields=['during_welding','before_welding','after_welding']

class ActInspectionForm(forms.ModelForm):
    class Meta:
        model = activity_inspection_action
        fields=['according','not_according','correction_action','comment','act_desp_action_descp']
    

class HeatForm(forms.ModelForm):
    class Meta:
        model = heat_calc
        fields=['current_A', 'voltage_V','time_SS','length_MM']

class GalleryForm(forms.ModelForm):
    class Meta:
        model = gallery
        fields=['photo']
