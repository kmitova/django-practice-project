# Generated by Django 4.1.1 on 2022-10-12 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_review_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='content',
        ),
    ]
