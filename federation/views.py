from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404

from .models import Nation

# Create your views here.
def index(request):
    return render(request, 'federation/index.html', {})

def nations(request):
    micronation = Nation.objects.all()
    return render(request, 'federation/nations.html', {'micronation': micronation})

def rankings(request):
    ranking = Nation.objects.all().order_by('-score')
    return render(request, 'federation/rankings.html', {'ranking': ranking})