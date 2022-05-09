from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home_page.html"

class AboutPageView(TemplateView):
    template_name = "about_page.html"

def home_page_view(request):
    return HttpResponse("Hello World!")
