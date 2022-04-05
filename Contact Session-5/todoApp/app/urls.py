from os import name
from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.index, name="index"),
    path("createtodo/", views.createtodo, name="Ctodo"),
    path("createlist/<str:todo>", views.createlist, name="createlist"),
    path("addlist/", views.addlist, name="addlist"),
    path("deletelist/<str:todoName>/<int:id>", views.deletelist, name="deletelist"),
    path("deletetodo/<str:todoName>", views.deletetodo, name="deletetodo")
]   