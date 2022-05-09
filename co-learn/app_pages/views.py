from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home_page.html"


class AboutPageView(TemplateView):
    template_name = "about_page.html"

