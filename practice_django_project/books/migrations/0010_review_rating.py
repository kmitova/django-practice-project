# Generated by Django 4.1.1 on 2022-10-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_rename_text_review_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('5', '5 stars'), ('4', '4 stars'), ('3', '3 stars'), ('2', '2 stars'), ('1', '1 star')], default='no rating', max_length=20),
        ),
    ]
