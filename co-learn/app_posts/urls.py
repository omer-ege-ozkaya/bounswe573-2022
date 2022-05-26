from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home_page_url"),
    path("posts/", views.PostPageView.as_view(), name="post_page_url")
]