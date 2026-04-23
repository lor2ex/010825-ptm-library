from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from library.models import User
from library.serializers import UserSerializer, RegisterUserSerializer
from library.permissions import IsSelfOrAdminProfilePermission
from library.serializers.users import UserLoginSerializer
from library.utils import clear_jwt_cookies, REFRESH_COOKIE_NAME, set_jwt_cookies


class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        data = request.data

        serializer = UserLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        try:
            response = Response(
                status=status.HTTP_200_OK,
            )

            set_jwt_cookies(response=response, user=user)

            # 6. вернуть ответ
            return response

        except Exception as e:
            # 6. вернуть ответ
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    "message": str(e)
                }
            )


class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, *args, **kwargs) -> Response:
        try:
            refresh_token = request.COOKIES.get(REFRESH_COOKIE_NAME)

            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()

        except TokenError:
            pass

        except Exception as e:
            return Response(
                data={
                    "message": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        response = Response(
            status=status.HTTP_200_OK,
        )

        clear_jwt_cookies(response=response)

        return response


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

        return response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrAdminProfilePermission]

    @action(detail=False, methods=['get'], url_path='get-me')
    def get_me(self, request: Request, *args, **kwargs) -> Response:
        obj = get_object_or_404(User, pk=request.user.pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
