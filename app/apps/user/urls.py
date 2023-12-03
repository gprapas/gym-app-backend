from rest_framework import routers
from django.urls import path
from .views import CustomAuthToken
from rest_framework import routers
from .views import UsersViewSet, UserProfile, RegisterUser

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')



urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('user_profile/', UserProfile.as_view(), name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),
]

urlpatterns += router.urls