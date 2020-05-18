from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "link",
            "creation_date",
            "upvotes_amount",
            "author_name",
        ]


class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ["id", "author_name", "content", "creation_date", "post_id"]
