from django.shortcuts import render

from practice_django_project.books.models import Review
from practice_django_project.core.utils import get_pagination_of_reviews


def login_user(request):
    return render(request, 'account/login-page.html')


def register_user(request):
    return render(request, 'account/register-page.html')


def details_user(request, pk):
    reviews = Review.objects.all()
    context = {
        'reviews': get_pagination_of_reviews(request, reviews)
    }

    return render(request, 'account/profile-details-page.html', context)
