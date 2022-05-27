from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_view, name="index"),
    path("learning-space/<int:id>", views.learning_space_view, name="learning_space")
]
