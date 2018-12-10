# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse

from forms import ConnexionForm
from models import Connexion
from django.contrib.auth import authenticate,login,logout 

from django.contrib.auth.decorators import login_required
############ API ###########
import json
import httplib
############ API ###########
# Create your views here.

def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
  			user = form.save()
  			user.refresh_from_db()
  			user.birth_date = form.cleaned_data.get("birth_date")
  			username = form.cleaned_data.get("username")
  			password = form.cleaned_data.get("password")
  			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes	
  			if user:  # Si l'objet renvoye n'est pas Non
  				user.save()
  				login(request, user)  # nous connectons l'utilisateur
  				#redirect("base")
  			else: # sinon une erreur sera affichée
  				error = True
  			print error
    else:
    	form = ConnexionForm()
    return render(request, "connexion.html", locals())

def deconnexion(request):
	logout(request)
	return redirect(reverse(connexion))

@login_required
def compte_profil(request):
	if request.user.is_authenticated():
		return render(request,"compte_profil.html",locals())

def data_api(request):
	connection = httplib.HTTPConnection('api.football-data.org')
	headers = { 'X-Auth-Token': 'd0a58b30d5e14ff8acbc45093b9e4f53' }
	connection.request('GET', '/v2/competitions/CL/matches', None, headers )
	response = json.loads(connection.getresponse().read())

	
	hometeam, awayteam, game_date, winner, score,matches = [],[],[],[],[],[]
	conteneur = ()
	nb_match = 10
	for i in range(nb_match):
		hometeam = response["matches"][i]["homeTeam"]["name"]
		awayteam = response["matches"][i]["awayTeam"]["name"]
		game_date = response["matches"][i]["utcDate"]
		winner = response["matches"][i]["score"]["winner"]
		score = response["matches"][i]["score"]["fullTime"]
		conteneur = (hometeam,awayteam,game_date,winner,score,)

		matches.append(conteneur)
		conteneur = ()
	
	"""
	for i in range(5):

		donnees[i].hometeam = matches[i]["homeTeam"]["name"]
		donnees[i].awayteam = matches[i]["awayTeam"]["name"]
		donnees[i].date = matches[i]["utcDate"]
		donnees[i].winner = matches[i]["score"]["winner"]
		donnees[i].score = matches[i]["score"]["fullTime"]
		
		match[i].append(response["matches"][i]["homeTeam"]["name"])
		match[i].append(response["matches"][i]["awayTeam"]["name"])
		match[i].append(response["matches"][i]["utcDate"])
		match[i].append(response["matches"][i]["score"]["winner"])
		match[i].append(response["matches"][i]["score"]["fullTime"])"""

	return render(request,"proto_page_accueil.html",locals())


