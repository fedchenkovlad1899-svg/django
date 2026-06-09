from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from task_manager.v1.serializers import AttachmentSerializer
from task_manager.models import Attachments


@extend_schema(tags=['Attachment'])
class AttachmentListApiView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentSerializer


    @extend_schema(
        summary='Get all attachments',
        description='Get all attachments',
        responses={200: AttachmentSerializer},
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        summary='Create attachment',
        description='Create attachment',
        request=AttachmentSerializer,
        responses={201: AttachmentSerializer},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@extend_schema(tags=['Attachment'])
class AttachmentDetailApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentSerializer


    @extend_schema(
        responses={200: AttachmentSerializer},
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    @extend_schema(
        request=AttachmentSerializer,
        responses={200: AttachmentSerializer},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
