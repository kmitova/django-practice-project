from django.contrib import admin

from practice_django_project.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
