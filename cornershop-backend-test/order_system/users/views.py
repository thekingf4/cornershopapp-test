from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from order_system.users.models import User
from order_system.users.serializers import UserSerializer
# Create your views here.


class UsersAPIView(ModelViewSet):
    """User view"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
