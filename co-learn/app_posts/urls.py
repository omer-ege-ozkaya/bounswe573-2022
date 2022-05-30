from django.urls import path
from . import views


urlpatterns = [
    path("post/update/<int:post_id>", views.update_post_view, name="update_post_url"),
    path("post/delete/<int:post_id>", views.delete_post_view, name="delete_post_url"),
]
