from django.shortcuts import render
from django.template import loader
from .models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})