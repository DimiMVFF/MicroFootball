# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Confederation(models.Model):
    confName = models.CharField(max_length=100, unique=True)
    confAcronym = models.CharField(max_length=8, unique=True)
    logo = models.CharField(max_length=250, unique=True)
    confStrength = models.FloatField(null=True, blank=True, default=0.0)

class Nation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    score = models.FloatField(null=True, blank=True, default=0.0)
    confederationMembership = models.ForeignKey('federation.Confederation')
    flag = models.CharField(max_length=250, unique=True)
    worldRanking = models.BooleanField(default=False)

class Match(models.Model):
    home = models.CharField(max_length=100, unique=True)
    away = models.CharField(max_length=100, unique=True)
    homeScore = models.IntegerField()
    awayScore = models.IntegerField()
    matchImportance = models.CharField(max_length=25)
