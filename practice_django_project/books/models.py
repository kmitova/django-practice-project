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

    # TODO: add review section (could be null and blank, make a review model first)

