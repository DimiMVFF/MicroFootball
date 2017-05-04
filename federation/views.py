# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from federation.models import Nation, Confederation, Match

# Create your views here.
def index(request):
    return render_to_response('index.html', {
        'nation': Nation.objects.all(),

    })