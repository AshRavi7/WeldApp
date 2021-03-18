from django.urls import path

from . import views 


app_name = 'projectReport'
urlpatterns = [
    path('',views.home, name='projectReport-base'),
    path('signup/',views.register_request,name='projectReport-signup'),
    path('profile/',views.profile,name='projectReport-profile'),
    path("login/", views.login_request, name='projectReport-login'),
    path("logout/", views.logout_request, name='projectReport-logout'),
    # path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    # # ex: /polls/5/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]