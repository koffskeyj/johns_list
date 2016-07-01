from rest_framework import serializers
from craigs_list.models import Category, SubCategory, Listing


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


class SubCategorySerializer(serializers.ModelSerializer):
    # category = serializers.HyperlinkedRelatedField(
    # read_only=True,
    # view_name="category_detail_api_view"
    # )

    class Meta:
        model = SubCategory
        fields = ["id", "category", "subcategory_name"]


class ListingSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # listing_category = serializers.HyperlinkedRelatedField(
    # read_only=True,
    # view_name="category_detail_api_view"
    # )

    # listing_subcategory = serializers.HyperlinkedRelatedField(
    # read_only=True,
    # view_name="subcategory_detail_api_view"
    # )


    class Meta:
        model = Listing
        fields = ["id", "listing_category", "listing_subcategory", "city", "title",
        "description", "user", "photo"]
