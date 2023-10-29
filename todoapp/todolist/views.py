from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todo


def index(request):
    todos = Todo.objects.all()
    print({'todo_list': todos, 'title': 'main page'})
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'main page'})

@require_http_methods(["POST"])
def add(request):
    user = request.POST['user']
    todo = Todo(user=user)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

