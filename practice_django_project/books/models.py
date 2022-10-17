# books/models.py
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.text import slugify

from practice_django_project.core.model_mixins import StrFromFieldsMixin

"""

Book item: 
- has title:
- has author:
- has number of pages
- boolean: 
    - is finished
    - is to read
    - is currently read

- has slug (id-title)
- has a review (one to many - one book can have many reviews)

"""


class Book(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'title', 'author', 'status')
    MAX_TITLE_LENGTH = 200
    MAX_AUTHOR_LENGTH = 100
    MAX_NUMBER_OF_PAGES = 10000
    MAX_DESCRIPTION_LENGTH = 10000

    NOT_READ = 'NR'
    CURRENTLY_READING = 'CR'
    TO_READ = 'TR'
    FINISHED = 'FN'

    BOOK_STATUS_CHOICES = [
        (NOT_READ, 'Not yet read'),
        (CURRENTLY_READING, 'Currently reading'),
        (TO_READ, 'To read'),
        (FINISHED, 'Finished')
    ]

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )

    author = models.CharField(
        max_length=MAX_AUTHOR_LENGTH,
        null=False,
        blank=False,
    )

    pages = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(MAX_NUMBER_OF_PAGES),
            ],
        null=False,
        blank=False,
    )

    status = models.CharField(
        max_length=20,
        choices=BOOK_STATUS_CHOICES,
        default=NOT_READ
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
    )

    publication_year = models.DateField(
        null=True,
        blank=True
    )

    cover_image = models.URLField(
        null=False,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            title_slug_list = self.title.split(" ")
            title_slug = "-".join(title_slug_list)

            self.slug = slugify(f'{self.id}-{title_slug}')

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('id',)


class Review(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'book', 'updated_at')

    STARS5 = '5'
    STARS4 = '4'
    STARS3 = '3'
    STARS2 = '2'
    STARS1 = '1'

    RATING_CHOICES = [
        (STARS5, '5 stars'),
        (STARS4, '4 stars'),
        (STARS3, '3 stars'),
        (STARS2, '2 stars'),
        (STARS1, '1 star')
    ]

    book = models.ForeignKey(
        # TODO: filter by finished book in the views file later so that only finished books can be reviewed
        Book, on_delete=models.RESTRICT, blank=False, null=False
    )

    content = models.TextField(
        null=False,
        blank=False,
        unique=True,
        editable=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    rating = models.CharField(
        max_length=20,
        choices=RATING_CHOICES,
        default='no rating',
        null=False,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=False,
        blank=True,
    )

    # TODO: associate the review with a user when available

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            title_slug_list = self.book.title.split(" ")
            title_slug = "-".join(title_slug_list)

            self.slug = slugify(f'review-of-{self.id}-{title_slug}')

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ('-updated_at',)
