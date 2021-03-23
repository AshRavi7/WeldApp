from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import project,location_discipline,heat_calc,drawing,weld,weld_action,activity_description,activity_inspection_action,gallery

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class projectForm(forms.ModelForm):
	 class Meta:
		 model = project
		 fields = "__all__"

class locationForm(forms.ModelForm):
	 class Meta:
		 model = location_discipline
		 fields = "__all__"

class weldActionForm(forms.ModelForm):
	 class Meta:
		 model = weld_action
		 fields = "__all__"

class heatForm(forms.ModelForm):
	 class Meta:
		 model = heat_calc
		 fields = "__all__"

class drawingForm(forms.ModelForm):
	 class Meta:
		 model = drawing
		 fields = "__all__"

class weldForm(forms.ModelForm):
	 class Meta:
		 model = weld
		 fields = "__all__"

class galleryForm(forms.ModelForm):
	 class Meta:
		 model = gallery
		 fields = "__all__"

class activitydescriptionForm(forms.ModelForm):
	 class Meta:
		 model = activity_description
		 fields = "__all__"

class activityinspectionForm(forms.ModelForm):
	 class Meta:
		 model = activity_inspection_action
		 fields = "__all__"