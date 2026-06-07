from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from task_manager.v1.serializers import CommentSerializer
from task_manager.models import Comments


@extend_schema(tags=['Comment'])
class CommentListApiView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


    @extend_schema(
        summary='Get all comments',
        description='Get all Ccomments',
        responses={200: CommentSerializer},
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        summary='Create comment',
        description='Create comment',
        request=CommentSerializer,
        responses={201: CommentSerializer},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@extend_schema(tags=['Comment'])
class CommentDetailApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


    @extend_schema(
        responses={200: CommentSerializer},
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    @extend_schema(
        request=CommentSerializer,
        responses={200: CommentSerializer},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
