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
    # books = random.sample(books, 1)
    print(len(books))
    try:
        book = random.choice(books)
        print(book.pk)
        # print(random_element)
        return book
    except IndexError:
        print('The sequence is empty')


def get_books_by_status(status):
    return Book.objects.filter(status=status)
