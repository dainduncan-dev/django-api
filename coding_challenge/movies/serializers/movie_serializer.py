from rest_framework import serializers
from django.db.models import Avg

from movies.models import Movie
from movies.serializers.review_serializer import ReviewSerializer

class MovieSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    reviewers = ReviewSerializer(many=True, read_only=True)
    runtime_formatted = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "release_date",
            "runtime",
            "runtime_formatted",
            "reviewers",
            "avg_rating",
        )

    def get_avg_rating(self, obj):
        average = obj.reviewers.aggregate(Avg('rating')).get('rating__avg')
        return average if average is not None else "No reviews"

    def get_runtime_formatted(self, obj):
        hours = obj.runtime // 60
        minutes = obj.runtime % 60
        return f"{hours}:{minutes:02}"
        
