from django.urls import path

from practice_django_project.books.views import show_books, search_view, book_details

urlpatterns = (
    path('', show_books, name='show books'),
    path('search-book/', search_view, name='search view'),
    path('<slug:slug>/', book_details, name='book details'),

)