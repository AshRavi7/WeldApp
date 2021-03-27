from django.urls import path
from .views import (
    ProjectCreateView,
    ProjectDetailView,
    LocationDetailView,
    LocationCreateView,
    DrawingDetailView,
    DrawingCreateView,
    WeldDetailView,
    WeldCreateView,
    WeldActionDetailView,
    WeldActionCreateView,
    HeatCreateView,
    HeatDetailView,
    GalleryCreateView,
    GalleryDetailView,
    InspectionDetailView,
    InspectionCreateView
)
from . import views

urlpatterns = [
    path('', views.home, name='inspection-home'),
    path('about/',views.about,name='inspection-about'),
    path('new/',views.new,name='inspection-new'),
    path('new/proj/<int:pk>/',ProjectDetailView.as_view(),name='project-detail'),
    path('new/proj',ProjectCreateView.as_view(),name='inspection-project'),
    path('new/loc/<int:pk>/',LocationDetailView.as_view(),name='loc-detail'),
    path('new/loc',LocationCreateView.as_view(),name='inspection-location'),
    path('new/draw/<int:pk>/',DrawingDetailView.as_view(),name='draw-detail'),
    path('new/draw',DrawingCreateView.as_view(),name='inspection-drawing'),
    path('new/weld/<int:pk>/',WeldDetailView.as_view(),name='weld-detail'),
    path('new/weld',WeldCreateView.as_view(),name='inspection-weld'),
    path('new/weldAct/<int:pk>/',WeldActionDetailView.as_view(),name='weldAction-detail'),
    path('new/weldAct',WeldActionCreateView.as_view(),name='inspection-weldAction'),
    path('new/heat/<int:pk>/',HeatDetailView.as_view(),name='heat-detail'),
    path('new/heat',HeatCreateView.as_view(),name='inspection-heat'),
    path('new/gallery/<int:pk>/',GalleryDetailView.as_view(),name='gallery-detail'),
    path('new/gallery',GalleryCreateView.as_view(),name='inspection-gallery'),
    path('new/inspection/<int:pk>/',InspectionDetailView.as_view(),name='inspection-detail'),
    path('new/inspection',InspectionCreateView.as_view(),name='inspection-inspection'),
    
    ]