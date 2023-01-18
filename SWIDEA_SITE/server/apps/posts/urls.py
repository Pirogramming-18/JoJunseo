from django.urls import path
from . import views

app_name = "posts"

urlpatterns= [
    path("", views.ideas_list , name="ideaslist"),
    path("toolslist", views.tools_list, name="toolslist"),
    path("tools/create", views.tools_create, name="toolscreate"),
    path("ideas/create", views.ideas_create, name="ideascreate"),
    path("ideas/<int:pk>", views.ideas_retrieve, name="ideas_retrieve"),
    path("tools/<int:pk>", views.tools_retrieve, name="tools_retrieve"),
    path("ideas/<int:pk>/update", views.ideas_update, name="ideasupdate"),
    path("tools/<int:pk>/update", views.tools_update, name="toolsupdate"),
    path("ideas/<int:pk>/delete", views.ideas_delete, name="ideasdelete"),
    path("tools/<int:pk>/delete", views.tools_delete, name="toolsdelete"),
]