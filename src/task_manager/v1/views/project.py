from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from task_manager.v1.serializers import ProjectSerializer
from task_manager.models import Projects


@extend_schema(tags=['Project'])
class ProjectListApiView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer


    @extend_schema(
        summary='Get all projects',
        description='Get all projects',
        responses={200: ProjectSerializer},
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        summary='Create project',
        description='Create project',
        request=ProjectSerializer,
        responses={201: ProjectSerializer},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@extend_schema(tags=['Project'])
class ProjectsDetailApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer


    @extend_schema(
        responses={200: ProjectSerializer},
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    @extend_schema(
        request=ProjectSerializer,
        responses={200: ProjectSerializer},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
