from django.db.models import Q
from django.shortcuts import render, redirect

from practice_django_project.books.forms import BookReviewCreateForm, BookReviewEditForm
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


def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        "book": book

    }
    return render(request, 'books/book-details-page.html', context)


def book_review_create(request, slug):
    book = Book.objects.filter(slug=slug).get()
    review = Review.objects.filter(book__slug=slug).first()
    if not review:
        print('has review')

        if request.method == "GET":
            form = BookReviewCreateForm(initial={"book": book})

        else:
            form = BookReviewCreateForm(request.POST, initial={"book": book})
            if form.is_valid():
                form.save()
                return redirect('index')
        has_review = False
        context = {
            'form': form,
            'slug': slug,
            'book': book,
            'has_review': has_review
        }
    else:
        if request.method == "GET":
            form = BookReviewEditForm(initial={"book": review.book, 'content': review.content}, instance=review)
        else:
            form = BookReviewEditForm(request.POST, initial={"book": review.book, 'content': review.content},
                                      instance=review)
            if form.is_valid():
                form.save()
                return redirect('index')
        has_review = True
        context = {
            'form': form,
            'slug': slug,
            'review': review,
            'book': book,
            'has_review': has_review
        }

    print(has_review)
    return render(request, 'books/review-book-page.html', context)


# def book_review_edit(request, slug):
#     book = Book.objects.filter(slug=slug).get()
#     review = Review.objects.filter(book__slug=slug).first()
#     if review:
#         print('has review')
#
#     if request.method == "GET":
#         form = BookReviewEditForm(initial={"book": review.book, 'content': review.content}, instance=review)
#     else:
#         form = BookReviewEditForm(request.POST, initial={"book": review.book, 'content': review.content}, instance=review)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     has_review = True
#     context = {
#         'form': form,
#         'slug': slug,
#         'review': review,
#         'book': book,
#         'has_review': has_review
#     }
#     print(has_review)
#     return render(request, 'books/review-book-page.html', context)

