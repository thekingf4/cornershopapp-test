from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import password_validation
from order_system.users.models import User


class UserSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    pais = serializers.CharField(max_length=100)
    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, attrs):
        """Verify passwords match"""
        passwd = attrs['password']
        passwd_conf = attrs['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Password don't match")
        password_validation.validate_password(passwd)
        return attrs
