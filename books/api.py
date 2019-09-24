from django.views.decorators.csrf import csrf_exempt
from .models import Author
from .serializers import AuthorSerializer
from .utils import JSONResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import pagination
from rest_framework import permissions
from .permissions import IsSuperUser
from rest_framework import viewsets


"""
@api_view(["GET", "POST"])
@csrf_exempt
def author_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JSONResponse(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return JSONResponse(status=404)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return JSONResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(instance=author, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        author.delete()
        return JSONResponse('', status=204)
"""


"""
class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    def get_object(self, pk, *args, **kwargs):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        if issubclass(queryset, Exception):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = AuthorSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None, *args, **kwargs):
        queryset = self.get_object(pk)
        if issubclass(queryset, Exception):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = AuthorSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        if issubclass(queryset, Exception):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
class AuthorList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Author.objects
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthorDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Author.objects
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""

"""
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAdminUser,)

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects
    serializer_class = AuthorSerializer
    permission_classes = (IsSuperUser,)
"""



# class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Author.objects
#     serializer_class = AuthorSerializer
#     permission_classes = (permissions.IsAuthenticated,)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects
    serializer_class = AuthorSerializer
    permission_classes = (IsSuperUser,)