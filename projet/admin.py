# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.text import Truncator
from django.contrib import admin
from models import Connexion

# Register your models here.

class ConnexionAdmin(admin.ModelAdmin):
	ordering = ("username",)
	search_fields = ("username",)
	list_display = ("usename","email","password",)

admin.site.register(Connexion)