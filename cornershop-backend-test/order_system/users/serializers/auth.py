from django.conf import settings
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import password_validation
from order_system.users.models import User
from order_system.utils.choice import USER_TYPE
from jwt import decode, ExpiredSignatureError, PyJWTError


class RegisterSerializer(serializers.Serializer):
    """User Register serializers"""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    pais = serializers.CharField(max_length=100)
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)

    type = serializers.ChoiceField(USER_TYPE, allow_blank=False, allow_null=False)

    def validate(self, attrs):
        passwd = attrs['password']
        passwd_conf = attrs['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError('Password not coincident')
        password_validation.validate_password(passwd)

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirmation')

        user = User.objects.create_user(**validated_data)

        if validated_data["type"] == USER_TYPE.employees:
            Group.objects.get(name="employees").user_set.add(user)

        return user


class ChangePasswordSerializer(serializers.Serializer):
    """Change password serializers"""
    email = serializers.EmailField()
    old_password = serializers.CharField(min_length=8, max_length=64)
    new_password = serializers.CharField(min_length=8, max_length=64)
    new_password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])

            if not user.check_password(data['old_password']):
                raise serializers.ValidationError("Password is incorrect")

            if data['new_password'] != data['new_password_confirmation']:
                raise serializers.ValidationError("Password does not match")

            password_validation.validate_password(data['new_password'])

            self.context['user'] = user
            self.context['password'] = data['new_password']
        except User.DoesNotExist:
            raise serializers.ValidationError("Username does not exist")

        return data

    def save(self):
        user = self.context["user"]
        user.set_password(self.context['password'])
        user.save()


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8, max_length=64)
    new_password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        try:
            payload = decode(data['token'], settings.SECRET_KEY, algorithms=['HS256'])
        except ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired')
        except PyJWTError:
            raise serializers.ValidationError('Invalid Token')

        if payload['type'] != 'password_reset':
            raise serializers.ValidationError('Invalid Token')

        if data['new_password'] != data['new_password_confirmation']:
            raise serializers.ValidationError('Password does not match')

        password_validation.validate_password(data['new_password'])

        self.context['payload'] = payload
        self.context['password'] = data['new_password']

        return data

    def save(self):
        payload = self.context['payload']
        user = User.objects.get(email=payload['email'])
        user.set_password(self.context['password'])
        user.save()


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('codename',)


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True, many=True)
    class Meta:
        model = Group
        fields = ['name', 'permissions']


class UserSerializer(serializers.Serializer):
    """User serializers"""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    pais = serializers.CharField(max_length=100)
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)
    groups = GroupSerializer(read_only=True, many=True)


class ResponseLoginSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserSerializer(read_only=True)

