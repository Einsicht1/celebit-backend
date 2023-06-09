from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class JWTService:
    def get_tokens(self, user: User):
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


jwt_service = JWTService()
