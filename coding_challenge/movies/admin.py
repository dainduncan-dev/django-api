from django.contrib import admin

from movies.models import Movie, Review

@admin.register(Movie)
class MovieAdminConsole(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "release_date",
        "runtime"
    )

@admin.register(Review)
class ReviewAdminConsole(admin.ModelAdmin):
    list_display = (
        "name",
        "movie",
        "rating"
    )