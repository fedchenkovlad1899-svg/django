from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from task_manager.v1.serializers import UserSerializer
from account.models import User
from config.pagination import CustomUserPagination


@extend_schema(tags=['User'])
class UserListApiView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomUserPagination


    @extend_schema(
        summary='Get all users',
        description='Get all users',
        responses={200: UserSerializer},
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        summary='Create user',
        description='Create user',
        request=UserSerializer,
        responses={201: UserSerializer},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@extend_schema(tags=['User'])
class UserDetailApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @extend_schema(
        responses={200: UserSerializer},
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    @extend_schema(
        request=UserSerializer,
        responses={200: UserSerializer},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
