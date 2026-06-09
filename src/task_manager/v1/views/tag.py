from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from task_manager.models import Tags
from task_manager.v1.serializers import TagSerializer
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['Tag'],
    summary="Get or create all tags ",
    responses={
        200: TagSerializer(many=True),
        201: TagSerializer,
    },
    request=TagSerializer,
)
@api_view(["GET", "POST"])
def tags_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        tags = Tags.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Tag'],
    summary='Retrieve, update or delete tag',
    description='Получить, обновить или удалить тег',
    responses={200: TagSerializer}
)

@api_view(["GET", "PUT", "DELETE"])
def tag_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        tags = Tags.objects.get(pk=pk)
    except Tags.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TagSerializer(tags)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TagSerializer(tags, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        tags.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# @extend_schema(tags=['Tag'])
# class TagListApiView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Tags.objects.all()
#     serializer_class = TagSerializer
#
#
#     @extend_schema(
#         summary='Get all tags',
#         description='Get all tags',
#         responses={200: TagSerializer},
#     )
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     @extend_schema(
#         summary='Create tag',
#         description='Create tag',
#         request=TagSerializer,
#         responses={201: TagSerializer},
#     )
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# @extend_schema(tags=['Tag'])
# class TagsDetailApiView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Tags.objects.all()
#     serializer_class = TagSerializer
#
#
#     @extend_schema(
#         responses={200: TagSerializer},
#     )
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#
#     @extend_schema(
#         request=TagSerializer,
#         responses={200: TagSerializer},
#     )
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
