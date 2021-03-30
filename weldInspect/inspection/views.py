from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
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
from .forms import projectForm,LocationForm,DrawingForm,WeldForm,WeldActionForm,ActInspectionForm,HeatForm,GalleryForm
# from django.urls import reverse

def home(request):
    return render(request, 'inspection/base.html')

def about(request):
    return render(request,'inspection/about.html')

def new(request):
    return render(request,'inspection/new_inspection.html')

# class ProjectCreateView(LoginRequiredMixin, CreateView):
#     model = project
#     fields=['project_number','report_number','data_perform']

#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         return super().form_valid(form)

# class LocationCreateView(LoginRequiredMixin, CreateView):
#     model = location_discipline
#     fields = ['location_name','discipline_name']
#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         obj=project.objects.filter(project_user_name=self.request.user).values('project_number')
#         form.instance.location_discipline_id=int(obj[0]['project_number'])
#         return super().form_valid(form)

# class DrawingCreateView(LoginRequiredMixin, CreateView):
#     model = drawing
#     fields = "__all__"

#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         return super().form_valid(form)

# class WeldCreateView(LoginRequiredMixin, CreateView):
#     model = weld
#     fields = "__all__"

#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         return super().form_valid(form)


# class WeldActionCreateView(LoginRequiredMixin, CreateView):
#     model = weld_action
#     fields = "__all__"

#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         return super().form_valid(form)



# class HeatCreateView(LoginRequiredMixin, CreateView):
#     model = heat_calc
#     fields=['current_A', 'voltage_V','time_SS','length_MM','heat_calc_id']

#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         obj=heat_calc
#         form.instance.heat_input=obj.activate_calculation(form.instance.current_A,form.instance.voltage_V,form.instance.time_SS,form.instance.length_MM)
#         return super().form_valid(form)
# class GalleryCreateView(LoginRequiredMixin, CreateView):
#     model = gallery
#     fields='__all__'
    
#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         return super().form_valid(form)

# class InspectionCreateView(LoginRequiredMixin, CreateView):
#     model = activity_inspection_action
#     fields='__all__'
    
#     def form_valid(self, form):
#         form.instance.project_user_name = self.request.user
#         return super().form_valid(form)


@login_required
def project_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = projectForm(request.POST)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.project_user_name= User.objects.get(pk=request.user.id)
                obj.save()
                return redirect(to='project-detail',pk=obj.pk)
    form = projectForm()
    return render(request, 'inspection/project_form.html', {'form': form})

class ProjectDetailView(DetailView):
    model = project
    template_name='inspection/project_detail.html'

@login_required
def location_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = LocationForm(request.POST)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.location_discipline_id=project.objects.filter(project_user_name_id=request.user.id).first()
                obj.save()
                return redirect('location-detail',pk=obj.pk)
    form = LocationForm()
    return render(request, 'inspection/location_discipline_form.html', {'form': form})

class LocationDetailView(DetailView):
    model = location_discipline
    template_name='inspection/location_discipline_detail.html'

@login_required
def drawing_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = DrawingForm(request.POST)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.drawing_id=project.objects.filter(project_user_name_id=request.user.id).first()
                obj.save()
                return redirect('drawing-detail',pk=obj.pk)
    form = DrawingForm()
    return render(request, 'inspection/drawing_form.html', {'form': form})

class DrawingDetailView(DetailView):
    model = drawing
    template_name='inspection/drawing_detail.html'

@login_required
def weld_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = WeldForm(request.POST)
            if form.is_valid():
                obj=form.save(commit=False)
                data=project.objects.filter(project_user_name_id=request.user.id).first()
                obj.weld_id=drawing.objects.filter(drawing_id=data).first()
                obj.save()
                return redirect('weld-detail',pk=obj.pk)
    form = WeldForm()
    return render(request, 'inspection/weld_form.html', {'form': form})

class WeldDetailView(DetailView):
    model = weld
    template_name='inspection/weld_detail.html'

@login_required
def weldaction_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = WeldActionForm(request.POST)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.weld_action_project_id=project.objects.filter(project_user_name_id=request.user.id).first()
                obj.save()
                return redirect('weldAction-detail',pk=obj.pk)
    form = WeldActionForm()
    return render(request, 'inspection/weld_action_form.html', {'form': form})

class WeldActionDetailView(DetailView):
    model = weld_action
    template_name='inspection/weld_action_detail.html'

@login_required
def actinspection_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ActInspectionForm(request.POST)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.inspection_id=project.objects.filter(project_user_name_id=request.user.id).first()
                obj.save()
                return redirect('inspection-detail',pk=obj.pk)
    form = ActInspectionForm()
    return render(request, 'inspection/activity_inspection_action_form.html', {'form': form})

class InspectionDetailView(DetailView):
    model = activity_inspection_action
    template_name='inspection/activity_inspection_action_detail.html'

@login_required
def heat_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = HeatForm(request.POST)
            if form.is_valid():
                obj=form.save(commit=False)
                call=heat_calc
                form.instance.heat_input=call.activate_calculation(form.instance.current_A,form.instance.voltage_V,form.instance.time_SS,form.instance.length_MM)
                obj.heat_calc_id=project.objects.filter(project_user_name_id=request.user.id).first()
                obj.save()
                return redirect('heat-detail',pk=obj.pk)
    form = HeatForm()
    return render(request, 'inspection/heat_calc_form.html', {'form': form})

class HeatDetailView(DetailView):
    model = heat_calc
    template_name='inspection/heat_calc_detail.html'

@login_required
def gallery_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = GalleryForm(request.POST)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.photo_report_id=project.objects.filter(project_user_name_id=request.user.id).first()
                obj.save()
                return redirect('gallery-detail',pk=obj.pk)
    form = GalleryForm()
    return render(request, 'inspection/gallery_form.html', {'form': form})

class GalleryDetailView(DetailView):
    model = gallery
    template_name='inspection/gallery_detail.html'