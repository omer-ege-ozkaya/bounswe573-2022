from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import LearningSpace
from app_article.models import Article
from .forms import LearningSpaceForm
from app_profile.models import Profile
from django.forms.models import model_to_dict


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
        form = LearningSpaceForm(req.POST, req.FILES)
        if form.is_valid():
            profile = Profile.objects.filter(user__id=req.user.id)
            learning_space_model = form.save()
            learning_space_model.colearners.set(profile)
            learning_space_model.save()
            return HttpResponseRedirect(f"/learning-space/{learning_space_model.id}")
    else:
        form = LearningSpaceForm()

    template = loader.get_template("app_learning_space/learning_space_create.html")
    context = {
        "form": form
    }
    return HttpResponse(template.render(context, req))


def update_learning_space_view(req, learning_space_id):
    learning_space_model = LearningSpace.objects.get(id=learning_space_id)
    if req.method == "POST":
        form = LearningSpaceForm(req.POST, instance=learning_space_model)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/learning-space/{learning_space_model.id}")
    else:
        learning_space_as_dict = model_to_dict(learning_space_model)
        form = LearningSpaceForm(initial=learning_space_as_dict)

    template = loader.get_template("app_learning_space/learning_space_update.html")
    context = {
        "form": form
    }
    return HttpResponse(template.render(context, req))


def delete_learning_space_view(req, learning_space_id):
    learning_space = LearningSpace.objects.get(id=learning_space_id)
    learning_space.delete()
    return HttpResponseRedirect("/")
