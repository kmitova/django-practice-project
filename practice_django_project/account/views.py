from django.shortcuts import render

from practice_django_project.books.models import Review


def login_user(request):
    return render(request, 'account/login-page.html')


def register_user(request):
    return render(request, 'account/register-page.html')


def details_user(request, pk):
    context = {
        'reviews': Review.objects.all()
    }

    return render(request, 'account/profile-details-page.html', context)
