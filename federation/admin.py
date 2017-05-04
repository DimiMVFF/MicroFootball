# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from federation.models import Nation, Confederation, Match

# Register your models here.

admin.site.register(Nation)
admin.site.register(Confederation)
admin.site.register(Match)