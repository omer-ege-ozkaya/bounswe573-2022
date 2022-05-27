from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(req):
    template = loader.get_template("app_learning_space/home_page.html")
    return HttpResponse(template.render())
