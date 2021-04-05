from typing import List
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
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
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from .filters import ProjectFilter

def home(request):
    return render(request, 'inspection/base.html')

def about(request):
    return render(request,'inspection/about.html')

def new(request):
    return render(request,'inspection/new_inspection.html')


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
                obj.location_discipline_id=project.objects.filter(project_user_name_id=request.user.id).latest('project_number')
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
                obj.drawing_id=project.objects.filter(project_user_name_id=request.user.id).latest('project_number')
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
                data=project.objects.filter(project_user_name_id=request.user.id).latest('project_number')
                obj.weld_id=drawing.objects.filter(drawing_id=data).latest('drawing_number')
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
                obj.weld_action_project_id=project.objects.filter(project_user_name_id=request.user.id).latest('project_number')
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
                obj.inspection_id=project.objects.filter(project_user_name_id=request.user.id).latest('project_number')
                obj.save()
                return redirect('inspection-detail',pk=obj.inspection_id)
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
                obj.heat_calc_id=project.objects.filter(project_user_name_id=request.user.id).latest('project_number')
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
                obj.photo_report_id=project.objects.filter(project_user_name_id=request.user.id).latest('project_number')
                obj.save()
                return redirect('gallery-detail',pk=obj.pk)
    form = GalleryForm()
    return render(request, 'inspection/gallery_form.html', {'form': form})

class GalleryDetailView(DetailView):
    model = gallery
    template_name='inspection/gallery_detail.html'

@login_required
def overview(request):
      return render(request,'inspection/overview.html')

class projectListView(ListView):
    model=project
    template_name='inspection/project_list.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=ProjectFilter(self.request.GET,queryset=self.get_queryset())
        return context


@login_required
def overall_view(request,proj_value):
    loc_obj=location_discipline.objects.select_related('location_discipline_id').get(location_discipline_id_id=proj_value)
    weld_action_obj=weld_action.objects.select_related('weld_action_project_id').get(weld_action_project_id_id=proj_value)
    drawing_obj=drawing.objects.select_related('drawing_id').get(drawing_id_id=proj_value)
    value=drawing_obj.drawing_number
    weld_obj=weld.objects.select_related('weld_id').get(weld_id_id=value)
    inspection_obj=activity_inspection_action.objects.select_related('inspection_id').filter(inspection_id_id=proj_value)
    heat_obj=heat_calc.objects.select_related('heat_calc_id').get(heat_calc_id_id=proj_value)
    gallery_obj=gallery.objects.select_related('photo_report_id').get(photo_report_id_id=proj_value)
    context={'location':loc_obj,'weld_action':weld_action_obj,'drawing':drawing_obj,'weld':weld_obj,'inspection':inspection_obj,'heat':heat_obj,'gallery':gallery_obj}
    return render(request, 'inspection/overall.html', context)
        
    #         form = GalleryForm(request.POST)
    #         if form.is_valid():
    #             obj=form.save(commit=False)
    #             obj.photo_report_id=project.objects.filter(project_user_name_id=request.user.id).first()
    #             obj.save()
    #             return redirect('gallery-detail',pk=obj.pk)
    # form = GalleryForm()
    # return render(request, 'inspection/gallery_form.html', {'form': form})
# @login_required
# def proj_overview(request):
#     data=project.objects.filter(project_user_name_id=request.user.id)
#     return render(request,"inspection/proj_overview.html",{'data':data})

# @login_required
# def loc_overview(request):
#     # user=project.objects.filter(project_user_name_id=request.user.id).values_list('project_number', flat=True)
#     number = project.objects.filter(project_user_name_id=request.user.id)
#     data=location_discipline.objects.filter(location_discipline_id=number)
#     return render(request,"inspection/loc_overview.html",{'data':data})

# @login_required
# def weldact_overview(request):
#     data=weld_action.objects.all()
#     return render(request,"inspection/proj_overview.html",{'data':data})




# @login_required
# def draw_overview(request):
#     data=project.objects.filter(project_user_name_id=request.user.id)
#     return render(request,"inspection/proj_overview.html",{'data':data})









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
        # return super().form_valid(form) 