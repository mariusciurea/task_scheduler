from django.shortcuts import render
from django.http import HttpResponse


dummy_tasks = [
    {'id': 1,
     'name': 'de sunat la revizie',
     'date': '2023-10-10'
     },
    {'id': 2,
     'name': 'cumparaturi',
     'date': '2023-10-11'
     },
    {
     'id': 3,
     'name': 'de terminat programul in python',
     'date': '2023-11-11'
     },
    {
     'id': 4,
     'name': 'sport',
     'date': '2023-11-12'
     }
]


def home(request):
    # return HttpResponse("""<h1>Welcome to my Task Scheduler App</h1>""")
    context = {'main_tasks': dummy_tasks}
    return render(request, 'tasks/home.html', context)


def about(request):
    # return HttpResponse("""<h1>About my app</h1>""")
    return render(request, 'tasks/about.html')