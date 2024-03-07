from django.urls import path
from .views import PaymentListAPIView, UserListCreateAPIView, UserRegisterAPIView, UserRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-retrieve-update-destroy'),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
]
