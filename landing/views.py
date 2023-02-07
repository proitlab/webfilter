from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

# Create your views here.
def landing_index(reques):
    template = get_template('landing/index.html')
    return HttpResponse(template.render())
