from django.views.generic import TemplateView


# Create your views here.
class ProfilePageView(TemplateView):
    template_name = "profile_page.html"
