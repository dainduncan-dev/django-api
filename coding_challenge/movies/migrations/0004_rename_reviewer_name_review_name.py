# Generated by Django 4.2.11 on 2024-04-24 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="reviewer_name",
            new_name="name",
        ),
    ]
