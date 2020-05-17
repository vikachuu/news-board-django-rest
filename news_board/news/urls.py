from django.urls import path

from .views import PostView, PostDetailView, CommentView, CommentDetailView
 
urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]