from django.urls import path, include
from order_system.users.views import AuthAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('auth', AuthAPIView)

urlpatterns = [
    path('', include(router.urls))
]
