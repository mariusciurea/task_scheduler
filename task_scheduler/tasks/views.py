from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import TaskForm


# dummy_tasks = [
#     {'id': 1,
#      'name': 'de sunat la revizie',
#      'date': '2023-10-10'
#      },
#     {'id': 2,
#      'name': 'cumparaturi',
#      'date': '2023-10-11'
#      },
#     {
#      'id': 3,
#      'name': 'de terminat programul in python',
#      'date': '2023-11-11'
#      },
#     {
#      'id': 4,
#      'name': 'sport',
#      'date': '2023-11-12'
#      }
# ]


def home(request):
    # return HttpResponse("""<h1>Welcome to my Task Scheduler App</h1>""")
    # tasks = Tasks.objects.filter(task_name__contains='masina')
    tasks = Tasks.objects.all()
    form = TaskForm()
    # print(form)
    if request.method == 'POST':  # if request.POST
        Tasks.objects.create(
            task_name=request.POST['task_name'],
            date_deadline=request.POST.get('date_deadline')
        )
        return redirect('home')
    # print(tasks)
    context = {'main_tasks': tasks, 'form': form}
    return render(request, 'tasks/home.html', context)


def task_update(request, pk):
    tsk = Tasks.objects.get(pk=pk)
    form = TaskForm(instance=tsk)
    context = {'form': form}

    if request.method == 'POST':
        tsk.task_name = request.POST['task_name']
        tsk.date_deadline = request.POST.get('date_deadline')
        tsk.save()
        return redirect('home')

    return render(request, 'tasks/task_update.html', context)


def delete(request, pk):
    tsk = Tasks.objects.get(pk=int(pk))
    tsk.delete()
    return redirect('home')


def about(request):
    # return HttpResponse("""<h1>About my app</h1>""")
    return render(request, 'tasks/about.html')