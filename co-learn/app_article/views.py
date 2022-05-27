from django.http import HttpResponse
from django.template import loader
from .models import LearningSpace
from app_article.models import Article
from app_posts.models import Post


def article_view(req, article_id):
    template = loader.get_template("app_article/article.html")
    article = Article.objects.get(id=article_id)
    posts = Post.objects.filter(article__id=article_id).order_by("created_at")
    context = {
        "article": article,
        "posts": posts
    }
    return HttpResponse(template.render(context, req))
