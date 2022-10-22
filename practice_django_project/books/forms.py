from django import forms

from practice_django_project.books.models import Review


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book', 'rating', 'content',)

