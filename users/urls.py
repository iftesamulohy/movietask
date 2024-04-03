from django.urls import path
from .views import CustomTokenObtainPairView, UserCreateView,UserViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'all-users',UserViewSet,basename="all-users")
urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserCreateView.as_view(), name='register'),
]
urlpatterns+= router.urls