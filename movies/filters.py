from rest_framework import filters
from django_filters import rest_framework as django_filters
from movies.models import Movie
class MovieFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['name']


