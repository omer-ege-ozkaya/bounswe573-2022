from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import LearningSpace
from app_article.models import Article
from app_posts.models import Post
from app_profile.models import Profile
from .forms import ArticleForm
from django.forms.models import model_to_dict


def article_view(req, article_id):
    template = loader.get_template("app_article/article.html")
    article = Article.objects.get(id=article_id)
    posts = Post.objects.filter(article__id=article_id).order_by("created_at")
    context = {
        "article": article,
        "posts": posts
    }
    return HttpResponse(template.render(context, req))


def create_article_view(req, learning_space_id):
    if req.method == "POST":
        form = ArticleForm(req.POST)
        if form.is_valid():
            profile = Profile.objects.filter(user__id=req.user.id)[0]
            article_model = Article(
                author=profile,
                learning_space=LearningSpace.objects.get(id=learning_space_id),
                **form.cleaned_data
            )
            article_model.save()
            return HttpResponseRedirect(f"/article/{article_model.id}")
    else:
        form = ArticleForm()

    template = loader.get_template("app_article/article_create.html")
    context = {
        "form": form,
        "learning_space_id": learning_space_id
    }
    return HttpResponse(template.render(context, req))


def update_article_view(req, article_id):
    article_model = Article.objects.get(id=article_id)
    if req.method == "POST":
        form = ArticleForm(req.POST, instance=article_model)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/article/{article_model.id}")
    else:
        article_as_dict = model_to_dict(article_model)
        form = ArticleForm(initial=article_as_dict)

    template = loader.get_template("app_article/article_update.html")
    context = {
        "form": form
    }
    return HttpResponse(template.render(context, req))


# def delete_article_view(req, article_id):
#     article = LearningSpace.objects.get(id=article_id)
#     article.delete()
#     return HttpResponseRedirect("/")
