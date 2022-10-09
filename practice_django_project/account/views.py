from django.shortcuts import render


def login_user(request):
    return render(request, 'account/login-page.html')


def register_user(request):
    return render(request, 'account/register-page.html')


def details_user(request, pk):
    return render(request, 'account/profile-details-page.html')
