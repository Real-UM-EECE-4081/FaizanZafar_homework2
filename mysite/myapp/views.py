from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def AboutView(request):
    return render(request, 'about.html')
