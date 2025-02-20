from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from artists.models import Artist
from blog.models import BlogPost
from comments.forms import CommentForm
from events.models import Event


# Create your views here.
@login_required
def CommentView(request, slug, type):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if type == "event": model = get_object_or_404(Event, slug=slug)
        elif type == "artist": model = get_object_or_404(Artist, slug=slug)
        elif type == "blogpost": model = get_object_or_404(BlogPost, slug=slug)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.model = model
            new_comment.comment = form.cleaned_data.get('comment')
            form.save()
            model.comments.add(new_comment)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()