from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/delete', views.delete_todo, name='delete_todo'),
]
