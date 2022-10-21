from django.urls import path

from practice_django_project.books.views import show_books, search_view, book_details, show_random_book, \
    add_book_to_tbr, book_review

urlpatterns = (
    path('', show_books, name='show books'),
    path('search-book/', search_view, name='search view'),
    path('<slug:slug>/', book_details, name='book details'),
    path('random-book', show_random_book, name='show random book'),
    path('add-book-to-tbr/<int:pk>/', add_book_to_tbr, name='add book to tbr'),
    path('book-review/<int:pk>/', book_review, name='book review')

)