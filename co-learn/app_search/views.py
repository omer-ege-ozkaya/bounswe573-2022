from django.http import HttpResponse
from app_learning_space.models import LearningSpace
from app_article.models import Article
from app_posts.models import Post
from app_profile.models import Profile
from django.db.models import Q
from django.template import loader


def search_view(req):
    search_query = req.GET.get("q")
    learning_spaces = LearningSpace.objects.filter(
        Q(name__icontains=search_query)
        | Q(description__icontains=search_query)
    )
    articles = Article.objects.filter(
        Q(title__icontains=search_query)
        | Q(body__icontains=search_query)
    )
    posts = Post.objects.filter(body__icontains=search_query)
    profiles = Profile.objects.filter(user__username__icontains=search_query)
    context = {
        "learning_spaces": learning_spaces,
        "articles": articles,
        "posts": posts,
        "profiles": profiles,
        "q": search_query
    }
    template = loader.get_template("app_search/search_page.html")
    return HttpResponse(template.render(context, req))
