from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostPageView.as_view(), name="post_page_url")
]