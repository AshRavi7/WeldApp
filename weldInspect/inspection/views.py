from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import activity_inspection_action, heat_calc, location_discipline, project,drawing,weld,weld_action,gallery
from django.contrib.auth.decorators import login_required
# from .forms import projectForm

def home(request):
    return render(request, 'inspection/base.html')

def about(request):
    return render(request,'inspection/about.html')

def new(request):
    return render(request,'inspection/new_inspection.html')

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = project
    fields = "__all__"

    def form_valid(self, form):
        form.instance.project_user_name = self.request.user
        return super().form_valid(form)

class ProjectDetailView(DetailView):
     model = project

class LocationCreateView(LoginRequiredMixin, CreateView):
    model = location_discipline
    fields = "__all__"

    def form_valid(self, form):
        form.instance.project_user_name = self.request.user
        return super().form_valid(form)

class LocationDetailView(DetailView):
     model = location_discipline

class DrawingCreateView(LoginRequiredMixin, CreateView):
    model = drawing
    fields = "__all__"

    def form_valid(self, form):
        form.instance.project_user_name = self.request.user
        return super().form_valid(form)

class DrawingDetailView(DetailView):
    model = drawing

class WeldCreateView(LoginRequiredMixin, CreateView):
    model = weld
    fields = "__all__"

    def form_valid(self, form):
        form.instance.project_user_name = self.request.user
        return super().form_valid(form)

class WeldDetailView(DetailView):
    model = weld

class WeldActionCreateView(LoginRequiredMixin, CreateView):
    model = weld_action
    fields = "__all__"

    def form_valid(self, form):
        form.instance.project_user_name = self.request.user
        return super().form_valid(form)

class WeldActionDetailView(DetailView):
    model = weld_action

class HeatCreateView(LoginRequiredMixin, CreateView):
    model = heat_calc
    fields=['current_A', 'voltage_V','time_SS','length_MM','heat_calc_id','heat_input']

    def form_valid(self, form):
        form.instance.project_user_name = self.request.user
        return super().form_valid(form)

class HeatDetailView(DetailView):
    model = heat_calc

class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = gallery
    fields='__all__'
    
    def form_valid(self, form):
        form.instance.project_user_name = self.request.user
        return super().form_valid(form)

class GalleryDetailView(DetailView):
    model = gallery

class InspectionCreateView(LoginRequiredMixin, CreateView):
    model = activity_inspection_action
    fields='__all__'
    
    def form_valid(self, form):
        form.instance.project_user_name = self.request.user
        return super().form_valid(form)

class InspectionDetailView(DetailView):
    model = activity_inspection_action


# @login_required
# def project_view(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated():
#             user_id = request.user
#             form = projectForm(user_name=user_id)
#             if form.is_valid():
#                 form.save()
#                 return redirect('inspection-new')
#     else:
#         form = projectForm()
#     return render(request, 'inspection/project_form.html', {'form': form})