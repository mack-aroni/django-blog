from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

# index that displays all posts
def blog_index(request):
  # ordered by earliest date created
  posts = Post.objects.all().order_by("-created_on")
  context = {
    "posts": posts,
  }
  return render(request, "blog/index.html", context)

# takes a category and returns posts with that category
def blog_category(request, category):
  # filter posts by a certain category/order by date created
  posts = Post.objects.filter(
    categories__name__contains=category
  ).order_by("-created_on")
  context = {
    "category": category,
    "posts": posts,
  }
  return render(request, "blog/category.html", context)

# takes a key value and returns posts with the key value
def blog_detail(request, pk):
  # retrieves post and commments that are result of pk
  post = Post.objects.get(pk=pk)
  # logic for comments
  form = CommentForm()
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = Comment(
        author=form.cleaned_data["author"],
        body=form.cleaned_data["body"],
        post=post,
      )
      comment.save()
      return HttpResponseRedirect(request.path_info)
  comments = Comment.objects.filter(post=post)
  context = {
    "post": post,
    "comments": comments,
    "form": CommentForm(),
  }
  return render(request, "blog/detail.html", context)