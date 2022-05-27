from django.urls import path
from . import views


urlpatterns = [
    path("article/<int:article_id>", views.article_view, name="article_url"),
    path("article/create/in/<int:learning_space_id>", views.create_article_view, name="create_article_url"),
    path("article/update/<int:article_id>", views.update_article_view, name="update_article_url"),
    path("article/delete/<int:article_id>", views.delete_article_view, name="delete_article_url"),
]
