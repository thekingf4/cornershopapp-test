from django.urls import path, include
from order_system.users.views import UsersAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UsersAPIView)

urlpatterns = [
    path('', include(router.urls))
]
