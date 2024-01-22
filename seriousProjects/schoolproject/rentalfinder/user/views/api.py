from user.models import UserModel
from rest_framework import generics, permissions, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user.serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.models import Token


class CreateUser(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.AllowAny,

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:
            user = UserModel.objects.get(email=request.data['email'])
            token = Token.objects.create(user=user)
            data = {'user': response.data, 'token': str(token)}
            return Response(data, status=status.HTTP_201_CREATED)
        return response


class LoginUser(views.APIView):
    permission_classes = permissions.AllowAny,

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data, context={'request': self.request})  # type: ignore
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']  # type: ignore
        token, created = Token.objects.get_or_create(user=user)
        # data = {'user': request.data['email'], 'token': token.key, 'created': created}
        data = {'user': user.username, 'token': token.key, 'created': created}
        return Response(data, status=status.HTTP_202_ACCEPTED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class LogoutApi(views.APIView):
    def post(self, request, *args, **kwargs):
        # Get the token associated with the current user and delete it
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            # The user didn't have a token or the token doesn't exist
            pass

        return Response(None, status=status.HTTP_204_NO_CONTENT)
