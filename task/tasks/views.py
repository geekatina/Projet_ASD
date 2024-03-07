from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm
from django.utils import timezone

def task_list(request):
    context = {}
    
    # Récupérer toutes les tâches
    tasks = Task.objects.all().order_by('priority')
    
    # Créer une instance de formulaire pour l'ajout de tâches
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirige vers la même page après l'ajout de la tâche
    
    # Filtrer les tâches prioritaires avec une date limite proche
    tasks_near_deadline = Task.objects.filter(deadline__lte=timezone.now() + timezone.timedelta(days=7)).order_by('priority', 'deadline')
    
    # Ajouter les tâches et le formulaire au contexte
    context['tasks'] = tasks
    context['form'] = form
    context['tasks_near_deadline'] = tasks_near_deadline

    return render(request, 'tasks/task_list.html', context)


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    context = {
        'form': form,
        'categories': Category.objects.all(),
        'tasks': Task.objects.all()  # Ajouter toutes les tâches au contexte
    }
    return render(request, 'tasks/update_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        confirmation = request.POST.get('confirmation', '')
        if confirmation == 'SUPPRIMER':
            task.delete()
            return redirect('task_list')
        else:
            return redirect('task_list')  # Rediriger vers la page de liste des tâches
    
    return render(request, 'tasks/confirm_delete.html', {'task': task, 'categories': Category.objects.all()})


def prioritize_tasks(request):
    # Obtenir les tâches avec date limite proche, en priorisant celles dont la date limite est la plus proche
    tasks_near_deadline = Task.objects.filter(deadline__lte=timezone.now() + timezone.timedelta(days=7)).order_by('deadline')
    return render(request, 'tasks/prioritize_tasks.html', {'tasks_near_deadline': tasks_near_deadline})

def prioritize_tasks_by_priority(request):
    # Obtenir toutes les tâches triées par priorité
    tasks_by_priority = Task.objects.all().order_by('-priority')
    return render(request, 'tasks/prioritize_tasks_by_priority.html', {'tasks_by_priority': tasks_by_priority})