"""EnoteProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from EnoteApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^$',views.HomeView.as_view(),name='home'),
	url(r'^about/$',views.AboutView.as_view(),name='about'),
	url(r'^notes/list/$',views.NotesListView.as_view(),name='notes_list'),
	url(r'^notes/create/$',views.NotesCreateView.as_view(),name='notes_create'),
	url(r'^notes/(?P<pk>\d+)/$',views.NotesDetailView.as_view(),name='notes_detail'),
	url(r'^notes/update/(?P<pk>\d+)/$',views.NotesUpdateView.as_view(),name='notes_update'),
	url(r'^notes/delete/(?P<pk>\d+)/$',views.NotesDeleteView.as_view(),name='notes_delete'),
]
