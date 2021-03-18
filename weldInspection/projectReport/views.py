from django.contrib.auth import login,authenticate,logout
from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm 

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
