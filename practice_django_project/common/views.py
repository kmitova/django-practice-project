from django.shortcuts import render


def index(request):
    return render(request, 'common/index.html')


def about(request):
    return render(request, 'common/about.html')


def team(request):
    return render(request, 'common/team.html')


def t_and_c(request):
    return render(request, 'common/t-and-c.html')


def delivery(request):
    return render(request, 'common/delivery.html')


def faq(request):
    return render(request, 'common/faq.html')