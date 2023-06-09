from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    phone_number = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "phone_number",
            "password"
        )

    def save(self, **kwargs):
        return User.objects.create_user(**self.validated_data)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "phone_number",
            "password"
        )


class SignInSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            msg = _("Unable to log in with provided credentials.")
            raise serializers.ValidationError(msg, code="authorization")

        if not user.is_active:
            msg = _("User account is disabled.")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
