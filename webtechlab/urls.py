"""webtechlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),	
	url(r'^login/$', views.login, name='login'),
	url(r'^temp/$', views.temp, name='temp'),
	url(r'^loginCredentials/$', views.loginCredentials, name='loginCredentials'),
	url(r'^openProfile/$', views.openProfile),
	url(r'^openTest/$', views.openTest),
	url(r'^openCourses/$', views.openCourses),
	url(r'^addAssignment/$', views.addAssignment),

	url(r'^addAssignmentDetails/$', views.addAssignmentDetails, name='addAssignmentDetails'),
	url(r'^signUp/$', views.signUp, name='signUp'),
	url(r'^submitAnswer/$', views.submitAnswer),
	url(r'^openNotesList/$', views.openNotesList),
	url(r'^openNotes/$', views.openNotes),
	url(r'^openDashboard/$', views.openDashboard),
	url(r'^editProfile/$', views.editProfile),
	url(r'^saveEditProfile/$', views.saveEditProfile),
	

#	url(r'^dashBoard/$', views.dashBoard, name='dashBoard'),
			
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
