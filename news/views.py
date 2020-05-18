from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """Methods for /posts/ endpoint: create and get all.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


class PostDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """Methods for /posts/<:id>/ endpoint: get, put, delete.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """Methods for /comments/ endpoint: create and get all.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """Methods for /posts/<:id>/ endpoint: get, put, delete.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
