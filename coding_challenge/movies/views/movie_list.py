from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned movies by filtering against
        a `min_runtime` and `max_runtime` query parameter in the URL.
        """
        queryset = Movie.objects.all()
        min_runtime = self.request.query_params.get('min_runtime', None)
        max_runtime = self.request.query_params.get('max_runtime', None)

        if min_runtime is not None:
            queryset = queryset.filter(runtime__gte=min_runtime)
        if max_runtime is not None:
            queryset = queryset.filter(runtime__lte=max_runtime)

        return queryset.order_by("id")