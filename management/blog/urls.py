
from django.urls import path
from .views import (
    BlogHomeView, 
    CreateTopicView, 
    SelectTopicView, 
    DeleteTopicView, 
    BlogQuestionsView, 
    GenerateBlogView,
    BlogDetailView,
    BlogListView,
)
from . import views


app_name = 'blog'

urlpatterns = [
    path(
        '', 
        BlogHomeView.as_view(), 
        name='home'
        ),

    path('create/', 
         CreateTopicView.as_view(), 
         name='create_topic'
         ),

    path('topics/<int:id>/select/',
         SelectTopicView.as_view(),
         name='select_topic',
         ),

    path('questions/<int:id>/', 
         BlogQuestionsView.as_view(), 
         name='answer_questions'
         ),

    path('questions/<int:id>/generate/',
         GenerateBlogView.as_view(),
         name='generate_blog',
         ),

    path('post/<int:id>/',
         BlogDetailView.as_view(),
         name='blog_detail',
         ),

    path('topics/<int:id>/delete', 
         DeleteTopicView.as_view(), 
         name='delete_topic',
         ),
    path('blog-list/',
         BlogListView.as_view(),
         name='blog_list',
         ),
]
