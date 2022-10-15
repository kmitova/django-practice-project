from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from practice_django_project.books.models import Review


def login_user(request):
    return render(request, 'account/login-page.html')


def register_user(request):
    return render(request, 'account/register-page.html')


def details_user(request, pk):
    reviews = Review.objects.all()
    p = Paginator(reviews, 3)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {
        'reviews': page
    }

    return render(request, 'account/profile-details-page.html', context)
