import random

from django.core.paginator import Paginator, EmptyPage

from practice_django_project.books.models import Book


# PAGINATION OF DB OBJECTS FUNCTION WITH PAGINATOR CLASS
def get_pagination_of_reviews(request, items):
    p = Paginator(items, 3)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return page

def get_random_book_object():
    books = list(Book.objects.filter(status='NR'))
    books = random.sample(books, 1)
    return books[0]

