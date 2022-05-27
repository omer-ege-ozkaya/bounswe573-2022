from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import LearningSpace
from app_article.models import Article
from forms import LearningSpaceForm

def index_view(req):
    template = loader.get_template("app_learning_space/home_page.html")
    learning_spaces = LearningSpace.objects.all().order_by("name")
    context = {
        "learning_spaces": learning_spaces
    }
    return HttpResponse(template.render(context, req))


def learning_space_view(req, learning_space_id):
    template = loader.get_template("app_learning_space/learning_space.html")
    learning_space = LearningSpace.objects.get(id=learning_space_id)
    articles = Article.objects.filter(learning_space__id=learning_space_id).order_by("title")
    context = {
        "learning_space": learning_space,
        "articles": articles
    }
    return HttpResponse(template.render(context, req))


def create_learning_space_view(req):
    if req.method == "POST":
        form = LearningSpaceForm(req.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = LearningSpaceForm()

    template = loader.get_template("app_learning_space/create_learning_space.html")
    context = {
        "form": form
    }
    return HttpResponse(template.render(context, req))
