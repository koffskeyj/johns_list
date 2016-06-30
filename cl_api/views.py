from django.shortcuts import render
from rest_framework import generics
from cl_api.serializers import CategorySerializer, SubCategorySerializer, ListingSerializer
from craigs_list.models import Category, SubCategory, Listing

class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryListAPIView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubcategoryDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ListingListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
