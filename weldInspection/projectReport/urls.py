from django.urls import path

from . import views 


app_name = 'projectReport'
urlpatterns = [
    path('',views.home, name='projectReport-base'),
    path('signup/',views.register_request,name='projectReport-signup'),
    path('profile/',views.profile,name='projectReport-profile'),
    path("login/", views.login_request, name='projectReport-login'),
    path("logout/", views.logout_request, name='projectReport-logout'),
    path("new/", views.new_inspect, name='projectReport-new'),
    path("overview/", views.overview, name='projectReport-overview'),
    path("new/proj/", views.proj, name='projectReport-proj'),
    path("new/loc/", views.loc, name='projectReport-loc'),
    path("new/weldact/", views.weld_action, name='projectReport-weldact'),
    path("new/drawing/", views.drawing, name='projectReport-drawing'),
    path("new/weld/", views.weld, name='projectReport-weld'),
    path("new/act/", views.act, name='projectReport-act'),
    path("new/heat/", views.heat, name='projectReport-heat'),
    path("new/gallery/", views.gallery, name='projectReport-gallery'),

    # path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    # # ex: /polls/5/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]