from django.urls import path

from practice_django_project.books.views import show_books

urlpatterns = (
    path('', show_books, name='show books'),
)