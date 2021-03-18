# """weldInspection URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path('',include('projectReport.urls')),
#     path('admin/', admin.site.urls)
# ]

# from django.contrib import admin
# from django.urls import path, include
# # from projectReport import views 
# from django.contrib.auth import views as auth

# urlpatterns = [

# 	path('admin/', admin.site.urls),
# 	path('', include('projectReport.urls')),
# 	path('login/', views.Login, name ='login'),
# 	path('logout/', auth.LogoutView.as_view(template_name ='projectReport/index.html'), name ='logout'),
# 	path('register/', views.register, name ='register'),

# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # <-- added
    path('', include("projectReport.urls"))
]