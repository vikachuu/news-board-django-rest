from django.urls import path

from .views import PostView, CommentView
 
urlpatterns = [
    path('posts/', PostView.as_view()),
    path('comments/', CommentView.as_view()),
]