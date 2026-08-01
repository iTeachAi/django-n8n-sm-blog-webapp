
from django.urls import path
from .views import HomeView, CreatePostView, DeletePostView, DetailedPostView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('delete/<int:id>/', DeletePostView.as_view(), name='delete_post'),
    path('detail/<int:id>/', DetailedPostView.as_view(), name='post_details'),
]
