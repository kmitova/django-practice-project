from django import forms

from practice_django_project.books.models import Review


class BaseReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book', 'rating', 'content',)
        widgets = {
            'book': forms.HiddenInput(),
            'content': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add review...',
                }
            )
        }
        labels = {
            'content': ''
        }


class BookReviewCreateForm(BaseReviewForm):
    pass


class BookReviewEditForm(BaseReviewForm):
    pass
