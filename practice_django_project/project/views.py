from django.shortcuts import render


def index(request):
    context = {
        "title": 'Biblioteca'
    }
    return render(request, 'index.html', context)
