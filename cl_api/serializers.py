from rest_framework import serializers
from craigs_list.models import Category, SubCategory, Listing


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ["id", "category", "subcategory_name"]


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ["id", "listing_category", "listing_subcategory", "city", "title",
        "description", "user", "photo"]
