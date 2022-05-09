from django.shortcuts import render
from django.views.generic import ListView
from . import models


class PostPageView(ListView):
    model = models.Post
    template_name = "post_page.html"
