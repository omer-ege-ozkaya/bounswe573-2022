from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import LearningSpace


# Create your views here.
def index(req):
    template = loader.get_template("app_learning_space/home_page.html")
    learning_spaces = LearningSpace.objects.all().values()
    context = {
        "learning_spaces": learning_spaces
    }
    return HttpResponse(template.render(context, req))
