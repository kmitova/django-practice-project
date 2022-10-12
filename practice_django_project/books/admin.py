from django.contrib import admin

from practice_django_project.books.models import Book, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
