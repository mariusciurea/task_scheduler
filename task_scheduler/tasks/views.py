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
    print(form)
    if request.method == 'POST':
        Tasks.objects.create(
            task_name=request.POST.get('task'),
            date_deadline=request.POST.get('task-deadline')
        )
        return redirect('home')
    # print(tasks)
    context = {'main_tasks': tasks, 'form': form}
    return render(request, 'tasks/home.html', context)


def delete(request, pk):
    tsk = Tasks.objects.get(pk=int(pk))
    tsk.delete()
    return redirect('home')


def about(request):
    # return HttpResponse("""<h1>About my app</h1>""")
    return render(request, 'tasks/about.html')