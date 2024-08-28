from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'item-sale-price', ItemSalePriceViewSet, basename='Item Sale Price')
router.register(r'item', ItemViewSet, basename='Item')
router.register(r'user', UserViewSet, basename='user-detail')
# router.register(r'emailValidation', EmailValidationViewSet, basename='email-validation')
# router.register(r'login', LoginViewSet, basename='login')
urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='customer-login'),
    path('validate-email/', EmailValidationView.as_view(), name='validate-email'),
    # path('auth/', include('dj_rest_auth.urls')),
    # path('auth/registration/', include('dj_rest_auth.registration.urls')),
]

