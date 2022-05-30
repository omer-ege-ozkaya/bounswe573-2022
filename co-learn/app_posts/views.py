from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from app_posts.models import Post
from django.forms.models import model_to_dict
from app_posts.forms import PostForm


def update_post_view(req, post_id):
    post_model = Post.objects.get(id=post_id)
    article_id = post_model.article.id
    if req.method == "POST":
        form = PostForm(req.POST, instance=post_model)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/article/{article_id}")
    else:
        post_as_dict = model_to_dict(post_model)
        form = PostForm(initial=post_as_dict)

    template = loader.get_template("app_posts/post_update.html")
    context = {
        "form": form,
        "article_id": article_id
    }
    return HttpResponse(template.render(context, req))


def delete_post_view(req, post_id):
    post = Post.objects.get(id=post_id)
    article_id = post.article.id
    post.delete()
    return HttpResponseRedirect(f"/article/{article_id}")
