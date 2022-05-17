from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class SignupPageView(generic.CreateView):
    form_class = UserCreationForm
    # For all generic class-based views the urls are not loaded when the file is imported, so we have to use the lazy
    # form of reverse to load them later when they're available.
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
