# Generated by Django 4.1.1 on 2022-10-12 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_pages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('id',)},
        ),
    ]
