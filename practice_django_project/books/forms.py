from django import forms

from practice_django_project.books.models import Review


class BaseReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book', 'rating', 'content',)
        widgets = {
            'book': forms.HiddenInput()
        }


class BookReviewCreateForm(BaseReviewForm):
    pass


class BookReviewEditForm(BaseReviewForm):
    pass
