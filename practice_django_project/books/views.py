from django.db.models import Q
from django.shortcuts import render, redirect

from practice_django_project.books.forms import BookReviewForm
from practice_django_project.books.models import Book, Review
from practice_django_project.core.utils import get_random_book_object


def add_book_to_tbr(request, pk):
    book = Book.objects.get(pk=pk)
    book.status = 'TR'
    book.save()
    # context = {
    #     'random_book': book
    # }
    # return render(request, 'books/show-books-page.html', context)
    return render(request, 'common/index.html')

def show_random_book(request):
    random_book = get_random_book_object()
    context = {
        'book': random_book
    }
    return render(request, 'books/random-book-page.html', context)


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

# TODO: style details page, add to read or review btn
#  (to read if not read, review if finished, complete if started, start if tbr'd)

def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        "book": book

    }
    return render(request, 'books/book-details-page.html', context)


def book_review(request, slug):
    # book = Book.objects.filter(slug=book_slug).get()
    Book.objects.filter()
    review = Review.objects.filter(book__slug=slug).get()
    print(f'Review: {review}')

    # review = book.review_set.filter()
    # print(review.content)
    if request.method == "GET":
        form = BookReviewForm(initial={"book": review.book, 'content': review.content}, instance=review)
    else:
        form = BookReviewForm(request.POST, initial={"book": review.book, 'content': review.content}, instance=review)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        # 'book': book,
        # 'username': username,
        'slug': slug,
        'review': review
    }
    return render(request, 'books/review-book-page.html', context)

'''
pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == "GET":
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details user', pk=1)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }

    return render(request, 'pets/pet-delete-page.html', context)

'''