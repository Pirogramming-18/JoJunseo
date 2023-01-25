from django.urls import path
from . import views

app_name = "games"

urlpatterns= [
    path("", views.post, name="post"),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('post_comment/', views.post_comment, name='post_comment'),
    path('comment_delete/', views.comment_delete, name='comment_delete'),
]