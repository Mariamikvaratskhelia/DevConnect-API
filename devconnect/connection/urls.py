from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    
    path('profiles/', ProfileListView.as_view()),

    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),

    path('follow/', FollowCreateView.as_view()),
    path('my-follows/', FollowListView.as_view()),

    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]