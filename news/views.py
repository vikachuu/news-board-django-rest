from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostView(APIView):
    """Methods for /posts/ endpoint: create and get all.
    """

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpvote(APIView):
    """Endpoint to upvote post (+1). Use POST method to follow the idempotence REST rule.
    """

    def post(self, request, pk: int):
        try:
            post = Post.objects.get(pk=pk)
            update_data: dict = {"upvotes_amount": post.upvotes_amount + 1}

            serializer = PostSerializer(post, data=update_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Post.DoesNotExist:
            raise Http404


class PostDetailView(APIView):
    """Methods for /posts/<:id>/ endpoint: get, put, delete.
    """

    def get(self, request, pk: int):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)

        except Post.DoesNotExist:
            raise Http404

    def put(self, request, pk: int):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Post.DoesNotExist:
            raise Http404

    def delete(self, request, pk: int):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist:
            raise Http404


class CommentView(APIView):
    """Methods for /comments/ endpoint: create and get all.
    """

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    """Methods for /posts/<:id>/ endpoint: get, put, delete.
    """

    def get(self, request, pk: int):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)

        except Comment.DoesNotExist:
            raise Http404

    def put(self, request, pk: int):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Comment.DoesNotExist:
            raise Http404

    def delete(self, request, pk: int):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Comment.DoesNotExist:
            raise Http404
