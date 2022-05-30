from django.http import HttpResponse
from app_learning_space.models import LearningSpace
from app_article.models import Article
from app_posts.models import Post
from app_profile.models import Profile
from django.db.models import Q
from django.template import loader


def profile_view(req, profile_id=None):
    if profile_id is None:
        profile = Profile.objects.filter(user__id=req.user.id)[0]
    else:
        profile = Profile.objects.get(id=profile_id)
    context = {
        "profile": profile
    }
    template = loader.get_template("app_profile/profile_page.html")
    return HttpResponse(template.render(context, req))
