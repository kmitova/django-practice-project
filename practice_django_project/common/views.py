from django.shortcuts import render

from practice_django_project.books.models import Book


def finish_book(request, pk):
    tbr_books = Book.objects.filter(
        status='TR'
    )[::-1][:5]

    finished_books = Book.objects.filter(
        status='FN'
    )[::-1][:5]

    current_books = Book.objects.filter(
        status='CR'
    )[::-1][:5]
    book = Book.objects.get(pk=pk)
    book.status = 'FN'
    book.save()
    context = {
        'book': book,
        'tbr_books': tbr_books,
        'finished_books': finished_books,
        'current_books': current_books
    }

    return render(request, 'common/index.html', context)


def start_book(request, pk):
    tbr_books = Book.objects.filter(
        status='TR'
    )[::-1][:5]

    finished_books = Book.objects.filter(
        status='FN'
    )[::-1][:5]

    current_books = Book.objects.filter(
        status='CR'
    )[::-1][:5]
    book = Book.objects.get(pk=pk)
    book.status = 'CR'
    book.save()
    context = {
        'book': book,
        'tbr_books': tbr_books,
        'finished_books': finished_books,
        'current_books': current_books
    }

    return render(request, 'common/index.html', context)



def index(request):
    tbr_books = Book.objects.filter(
        status='TR'
    )[::-1][:5]

    finished_books = Book.objects.filter(
        status='FN'
    )[::-1][:5]

    current_books = Book.objects.filter(
        status='CR'
    )[::-1][:5]

    context = {
        'tbr_books': tbr_books,
        'finished_books': finished_books,
        'current_books': current_books

    }
    return render(request, 'common/index.html', context)


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