# from WeldApp.weldInspection import projectReport
from django.contrib.auth import login,authenticate,logout
from .forms import NewUserForm,projectForm,locationForm,weldActionForm,drawingForm,weldForm,activitydescriptionForm,activityinspectionForm,heatForm,galleryForm
from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import project,location_discipline,drawing,weld,weld_action,activity_inspection_action,activity_description,heat_calc,gallery

def home(request):
    return render(request, 'projectReport/dash_base.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("projectReport:projectReport-profile")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request,"projectReport/signup.html",{"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("projectReport:projectReport-profile")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"projectReport/login.html",{"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("projectReport:projectReport-base")

def profile(request):
    return render(request, 'projectReport/profile.html')

def new_inspect(request):
	return render(request,'projectReport/new_inspection.html')

def overview(request):
	return render(request,'projectReport/inspection_view.html')

# class ProjCreateView(LoginRequiredMixin, CreateView):
#     model = project
#     fields = "__all__"

#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         return super().form_valid(form)

def proj(request):
	if request.method == 'POST':
		form = projectForm(request.POST)
		if form.is_valid():
			form.save()   
	form = projectForm
	return render(request, 'projectReport/flow/project.html', {'form': form})

def loc(request):
	return render(request,'projectReport/flow/location.html')

def drawing(request):
	return render(request,'projectReport/flow/drawing.html')

def weld(request):
	return render(request,'projectReport/flow/weld.html')

def weld_action(request):
	return render(request,'projectReport/flow/weld_action.html')

def act(request):
	return render(request,'projectReport/flow/activity.html')

def heat(request):
	return render(request,'projectReport/flow/heat.html')

def gallery(request):
	return render(request,'projectReport/flow/gallery.html')