from django.shortcuts import render
from rest_framework import viewsets

from movies.filters import MovieFilter
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Avg
from django.http import Http404
from rest_framework import status
from django_filters import rest_framework as django_filters
class MovieViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = MovieFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def retrieve(self, request, pk=None):
        movie = self.get_object()
        ratings = Rating.objects.filter(movie_id=movie.id) 
        average_rating = ratings.aggregate(avg_rating=Avg('rating'))['avg_rating']
        serializer = MovieSerializer(movie)
        data = serializer.data
        data['average_rating'] = average_rating if average_rating is not None else 0
        return Response({"data": data, "message": "Movie retrieved successfully"})

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Movie deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({"message": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data, "message": "Movie updated successfully"})

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"data": serializer.data, "message": "Movie patched successfully"})

    def get_object(self):
        try:
            return super().get_object()
        except Movie.DoesNotExist:
            raise Http404

class RatingViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
