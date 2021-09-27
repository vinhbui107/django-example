from rest_framework.views import APIView
from rest_framework.exceptions import status
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.serializers import (
    UserInfoSerializer,
    LoginSerializer,
    RegisterSerializer,
    UpdateUserSerializer,
    DeleteUserSerializer,
)
from apps.common.model_loaders import get_user_model
from apps.common.helpers import validate_data
from apps.common.responses import (
    ApiSuccessResponse,
    ApiSuccessMessageResponse,
)


class LoginAPI(TokenObtainPairView):
    serializer_class = LoginSerializer


class RegisterAPI(APIView):
    def post(self, request):
        User = get_user_model()

        data = validate_data(RegisterSerializer, request.data)

        new_user = User.objects.create_user(**data)
        new_user.save()

        return ApiSuccessMessageResponse(
            message=("Create user successfully"),
            status=status.HTTP_201_CREATED,
        )


class UserAPI(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):

        user = request.user
        user_serializer = UserInfoSerializer(user, context={"request": request})
        return ApiSuccessResponse(data=user_serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        data = validate_data(UpdateUserSerializer, request.data)

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        user = request.user
        user.update(username=username, password=password, email=email)

        user_serializer = UserInfoSerializer(user, context={"request": request})
        return ApiSuccessResponse(data=user_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        data = validate_data(DeleteUserSerializer, request.data)

        password = data.get("password")

        user = request.user
        user.delete_with_password(password)

        return ApiSuccessMessageResponse(message="Goodbye 😔", status=status.HTTP_200_OK)
