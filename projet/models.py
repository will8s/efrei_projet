# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
"""
class Connexion(models.Model):
	
	user = models.OneToOneField(User)  # La liaison OneToOne vers le modèle User

	def __str__(self):
		return "Profil de {0}".format(self.user.username)
"""
class Connexion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
    	return "profile de {0}".format(self.user.username)
#pour acceder à la liste des utilisateur : Connexion.user.get_queryset()
@receiver(post_save, sender=User)
def update_user_Connexion(sender, instance, created, **kwargs):
    if created:
        Connexion.objects.create(user=instance)
    
