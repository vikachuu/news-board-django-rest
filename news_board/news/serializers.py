from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    link = serializers.URLField()
    creation_date = serializers.DateTimeField()
    upvotes_amount = serializers.IntegerField()
    author_name = serializers.CharField(max_length=255)


class CommentSerializer(serializers.Serializer):
    author_name = serializers.CharField(max_length=255)
    content = serializers.CharField()
    creation_date = serializers.DateTimeField()
    post_id = serializers.IntegerField()
