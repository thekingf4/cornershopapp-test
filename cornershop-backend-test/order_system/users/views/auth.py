from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.permissions import AllowAny, IsAuthenticated
from order_system.users.models import User
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework.decorators import action
from order_system.users.serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer, \
    ResetPasswordSerializer, ResponseLoginSerializer
from order_system.users.permissions.users import IsAccountOwner

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class AuthAPIView(GenericViewSet):
    """Auth view

    view class used to generate the login, register and
    change_password, and extend from the GenericViewSet class
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """Permission validate user


        Class method used to validate the permissions that the user
        has on the different methods

        Returns a list of permissions
        """

        permissions = [AllowAny, ]
        if self.action in ["change_password", "logout", ]:
            permissions = [IsAuthenticated, IsAccountOwner]

        return [p() for p in permissions]

    def get_serializer_class(self):
        if self.action == "login":
            serializer_class = JSONWebTokenSerializer
        elif self.action == "register":
            serializer_class = RegisterSerializer
        elif self.action == "change_password":
            serializer_class = ChangePasswordSerializer
        elif self.action == "reset_password":
            serializer_class = ResetPasswordSerializer
        elif self.action == "logout":
            serializer_class = "BlackListTokenSerializer"

        return serializer_class

    @swagger_auto_schema(
        tags=['Auth'],
        query_serializer=JSONWebTokenSerializer,
        responses={HTTP_200_OK: ResponseLoginSerializer, 400: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "token": openapi.Schema(type=openapi.TYPE_STRING, description='string')
            }
        )},
    )
    @action(detail=False, methods=['POST'])
    def login(self, request):
        """Metodo login

        utilizado para realizar la autentication a la aplicación

        devuelve un JSON con los siguientes atributos:

        token: JSON Web Token that can be used to authenticate later calls
        user: Información del usuario
        """
        serializer = JSONWebTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            "token": serializer.validated_data["token"],
            "user": UserSerializer(serializer.validated_data["user"]).data,
        }
        return Response(response, status=HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response({
            "message": "User register ok",
            "user": UserSerializer(data).data
        }, status=HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def change_password(self, request):
        request.data.update({"email": request.user.email})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response({
            "message": "Change password ok"
        }, status=HTTP_200_OK)
