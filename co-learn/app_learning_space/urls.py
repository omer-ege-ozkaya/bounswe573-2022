from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index_url"),
    path("learning-space/<int:learning_space_id>", views.learning_space_view, name="learning_space_url"),
    path("learning-space/create", views.create_learning_space_view, name="create_learning_space_url"),
    path("learning-space/update", views.create_learning_space_view, name="update_learning_space_url"),
    path("learning-space/delete", views.create_learning_space_view, name="delete_learning_space_url"),
]

