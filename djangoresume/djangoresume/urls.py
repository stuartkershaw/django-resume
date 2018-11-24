"""djangoresume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework import routers
from resume import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'websites', views.WebsiteViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'positions', views.PositionViewSet)
router.register(r'schools', views.SchoolViewSet)
router.register(r'programs', views.ProgramViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'institutions', views.InstitutionViewSet)
router.register(r'certifications', views.CertificationViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/<str:username>/',
         views.resume_page_view, name='resume_detail'),
    path('', views.home_page_view, name='resume_home'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
