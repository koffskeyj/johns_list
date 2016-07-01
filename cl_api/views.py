from django.shortcuts import render
from rest_framework import generics
from cl_api.serializers import CategorySerializer, SubCategorySerializer, ListingSerializer
from craigs_list.models import Category, SubCategory, Listing
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from cl_api.permissions import IsUserOrReadOnly

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ListingListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ListingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsUserOrReadOnly,)


class SubCategoryListingListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        subcategory = self.kwargs.get('pk', None)
        return Listing.objects.filter(listing_subcategory_id=subcategory)


class CategorySubcategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return SubCategory.objects.filter(category_id=category_id)


class CategoryListingListAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(listing_category_id=category_id)
