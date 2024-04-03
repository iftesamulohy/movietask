from django.urls import path
from .views import MovieViewSet,RatingViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'movies',MovieViewSet,basename="movies")
router.register(r'ratings',RatingViewSet,basename="ratings")
urlpatterns = [
    
]
urlpatterns+= router.urls