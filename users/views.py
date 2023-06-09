from django.conf import settings
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from users.models import User
from users.serializers import SignUpSerializer, UserListSerializer, SignInSerializer
from users.services.JWTService import jwt_service


class SignUpAPIView(GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()


class SignInAPIView(GenericAPIView):
    throttle_classes = ()
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        jwt_token = jwt_service.get_tokens(user)
        response = Response(user.email)
        response.set_cookie(
            "access_token",
            jwt_token["access"],
            httponly=True,
            max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
            secure=True,
            domain="bamm.kr",  # TODO: 도메인 변경되면 수정
        )
        return response


class UserListAPIVIew(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

