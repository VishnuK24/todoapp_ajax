"""todo views"""
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import TaskForm
from .models import Task


class TodoListView(View):
    """Todo list view for listing all tast and adding tasks."""

    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'todo/todo-list.html', context={'form': form, 'tasks': tasks})

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            return JsonResponse({'task': model_to_dict(task)}, status=200)
        else:
            return redirect('todo:todo-list')

class TodoCompleteView(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.completed = True
        task.save()
        return JsonResponse({'task': model_to_dict(task)}, status=200) 

class TodoDeletedView(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'result': 'ok'}, status=200)
