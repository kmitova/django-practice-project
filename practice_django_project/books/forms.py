from django import forms

from practice_django_project.books.models import Review


class BookReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book', 'rating', 'content',)
        # widgets = {
        #     'book': forms.TextInput(
        #         attrs={
        #             'readonly': 'readonly',
        #         }
        #     ),}

class BookReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book', 'rating', 'content',)
        # widgets = {
        #     'book': forms.TextInput(
        #         attrs={
        #             'readonly': 'readonly',
        #         }
        #     ),}
