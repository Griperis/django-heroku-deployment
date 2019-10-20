from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from .models import Todo

def index(request):
    if request.POST:
        new_title = request.POST.get('title')
        new_text = request.POST.get('text-detail')
        new_todo = Todo(title_text=new_title, detail=new_text)
        new_todo.save()
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return redirect('../')