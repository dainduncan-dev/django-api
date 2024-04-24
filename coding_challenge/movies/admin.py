from django.contrib import admin

from movies.models import Movie 

@admin.register(Movie)
class MovieAdminConsole(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "release_date",
        "runtime",
        "runtime_formatted",
        "reviewers",
        "avg_rating",
    )

