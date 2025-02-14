import datetime
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from django.db.models import Count

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from blog.models import BlogPost
from events.forms import CommentForm


class BlogPostList(ListView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_on')

        return queryset.filter(published=True)

@method_decorator(login_required, name="dispatch")
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "blog/blogpost_create.html"
    fields = ['title', 'thumbnail', 'tags', 'summary', 'content', 'published', 'is_featured', 'related_event', 'related_artists']

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            
        form.instance.created_on = datetime.datetime.now()
            
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "blog/blogpost_edit.html"
    context_object_name = "post"
    fields = ['title', 'thumbnail', 'tags', 'summary', 'content', 'published', 'is_featured', 'related_event', 'related_artists']

class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "blog/blogpost_detail.html"
    context_object_name = "post"

@login_required
def BlogPostCommentView(request, slug):
    if request.method == "POST":
        form = CommentForm(request.POST)
        post = get_object_or_404(BlogPost, slug=slug)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.comment = form.cleaned_data.get('comment')
            form.save()
            post.comments.add(new_comment)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()

@method_decorator(login_required, name="dispatch")
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("blog:list")