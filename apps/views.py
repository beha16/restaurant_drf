from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    UpdateAPIView, RetrieveAPIView,
    DestroyAPIView, ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category
from .serializers import (
    UserCreateSerializer, UserListSerializer,
    UserUpdateSerializer, ProductListSerializer,
    CategoryListSerializer, ProductDetailSerializer, ProductCreateSerializer
)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer
        elif self.request.method == 'POST':
            return UserCreateSerializer
        return super().get_serializer_class()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListSerializer
        elif self.request.method == 'DELETE':
            return UserCreateSerializer
        elif self.request.method == 'PUT':
            return UserUpdateSerializer
        return super().get_serializer_class()


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductDetailAPIView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductDetailSerializer(product).data

        data = {
            'status': status.HTTP_200_OK,
            'data': serializer
        }
        return Response(data)


class ProductCreateAPIView(APIView):
    def post(self, request):
        pass
        # serializer = ProductCreateSerializer







