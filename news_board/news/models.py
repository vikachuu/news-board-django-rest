from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes_amount = models.PositiveIntegerField()
    author_name = models.CharField(max_length=255)


class Comment(models.Model):
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
