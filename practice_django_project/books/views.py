from django.db.models import Q
from django.shortcuts import render, redirect

from practice_django_project.books.models import Book


def show_books(request):
    tbr_books = Book.objects.filter(
        status='TR'
    )
    context = {
        'tbr_books': tbr_books

    }

    return render(request, 'books/show-books-page.html', context)


def search_view(request):
    title_or_author_query = request.GET.get('title_or_author')
    queryset = Book.objects.all()
    query_made = False

    if title_or_author_query != '' and title_or_author_query is not None:
        queryset = queryset.filter(Q(title__icontains=title_or_author_query) |
                                   Q(author__icontains=title_or_author_query)) \
            .distinct()
        query_made = True

    context = {
        'queryset': queryset,
        "query_made": query_made
    }

    print(queryset)

    return render(request, 'books/search-books-page.html', context)


def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        "book": book

    }
    return render(request, 'books/book-details-page.html', context)