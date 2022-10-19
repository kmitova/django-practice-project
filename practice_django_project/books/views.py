from django.db.models import Q
from django.shortcuts import render

from practice_django_project.books.models import Book
from practice_django_project.core.utils import get_random_book_object


def add_random_book_to_tbr(request, pk):
    book = Book.objects.get(pk=pk)
    book.status = 'TR'
    book.save()
    context = {
        'random_book': book
    }
    return render(request, 'books/show-books-page.html', context)

# TODO: move show random book to its own html page (like the search function)
def show_random_book(request):
    random_book = get_random_book_object()
    context = {
        'random_book': random_book
    }
    return render(request, 'books/show-books-page.html', context)


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