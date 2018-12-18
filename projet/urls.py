from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView,ListView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name = 'main/base.html'), name = 'base'),
	url(r'^accueil$', views.data_api, name = 'accueil'),
	url(r'^accueil/classement$', TemplateView.as_view(template_name = 'proto_classement.html'), name = 'proto_classement'),
	url(r'^accueil/calendar$', TemplateView.as_view(template_name = 'proto_calendar.html'), name = 'proto_calendar'),
	url(r'^accueil/paris$', TemplateView.as_view(template_name = 'proto_paris.html'), name = 'proto_paris'),

	#url(r'^connexion/$', views.connexion, name = 'connexion'),
	#url(r'^deconnexion/$', views.deconnexion, name = 'deconnexion'),
    #url(r'^login/$', auth_views.login, name='login'),
    #rl(r'^logout/$', auth_views.logout, name='logout'),
	#url(r'^compte_profil/$', views.compte_profil, name = 'compte_profil'),
]