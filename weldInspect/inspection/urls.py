from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.about, name='inspection-home'),
    # path('about/',views.about,name='inspection-about'),
    # path('new/',views.new,name='inspection-new'),
    path('new/proj/<int:pk>/',ProjectDetailView.as_view(),name='project-detail'),
    path('new/proj',views.project_view,name='inspection-project'),
    path('new/loc/<str:pk>/',LocationDetailView.as_view(),name='location-detail'),
    path('new/loc',views.location_view,name='inspection-location'),
    path('new/draw/<str:pk>/',DrawingDetailView.as_view(),name='drawing-detail'),
    path('new/draw',views.drawing_view,name='inspection-drawing'),
    path('new/weld/<int:pk>/',WeldDetailView.as_view(),name='weld-detail'),
    path('new/weld',views.weld_view,name='inspection-weld'),
    path('new/weldAct/<int:pk>/',WeldActionDetailView.as_view(),name='weldAction-detail'),
    path('new/weldAct',views.weldaction_view,name='inspection-weldAction'),
    path('new/heat/<int:pk>/',HeatDetailView.as_view(),name='heat-detail'),
    path('new/heat',views.heat_view,name='inspection-heat'),
    path('new/gallery/<int:pk>/',GalleryDetailView.as_view(),name='gallery-detail'),
    path('new/gallery',views.gallery_view,name='inspection-gallery'),
    path('new/inspection/<int:pk>/',InspectionDetailView.as_view(),name='inspection-detail'),
    path('new/inspection',views.actinspection_view,name='inspection-inspection'),
    path('overview/proj',projectListView.as_view(),name='inspection-project_view'),
    path('overall/<int:proj_value>/',views.overall_view,name='inspection-overall'),
    ]