# from django.forms import fields
# from .models import project
# from django import forms

# class projectForm(forms.ModelForm):
#     class Meta:
#         model = project
#         fields="__all__"
#     def __init__(self, *args, **kwargs):
#         user_id = kwargs.pop('user_id', None)
#         super(projectForm, self).__init__(*args, **kwargs)
#         if user_id is not None:
#             self.fields['project_user_name'].queryset = project.objects.filter(user=user_id)
#         else:
#             self.fields['project_user_name'].queryset = project.objects.none()