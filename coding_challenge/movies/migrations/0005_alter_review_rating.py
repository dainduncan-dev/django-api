# Generated by Django 4.2.11 on 2024-04-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_rename_reviewer_name_review_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.PositiveSmallIntegerField(),
        ),
    ]
