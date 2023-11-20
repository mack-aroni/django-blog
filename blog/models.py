from django.db import models

class Category(models.Model):
  # stores the name of the category (30 char limit)
  name = models.CharField(max_length=30)
  # correctly formats Category names
  class Meta:
    verbose_name_plural = "categories"
  def __str__(self):
    return self.name

class Post(models.Model):
  # stores title of each post as shortstring
  title = models.CharField(max_length=255)
  # textfield to store post bodytext
  body = models.TextField()
  # stores datetime object for date created
  created_on = models.DateTimeField(auto_now_add=True)
  # stores datetime object for last edit
  last_modified = models.DateTimeField(auto_now=True)
  # links catagories to posts
  categories = models.ManyToManyField("Category", related_name="posts")
  # returns post title instead of object name
  def __str__(self):
    return self.title

class Comment(models.Model):
    # stores author as shortstring
    author = models.CharField(max_length=60)
    # textfield to store bodytext of comment
    body = models.TextField()
    # stores datetime object for date created
    created_on = models.DateTimeField(auto_now_add=True)
    # defines manyToOne relationship (many comments to one post)
    # also links comments to posts and deletes associated comments when a post is deleted
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    # correctly formats Comment author and Post
    def __str__(self):
      return f"{self.author} on '{self.post}'"