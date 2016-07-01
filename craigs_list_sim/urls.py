"""craigs_list_sim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from craigs_list.views import IndexView, UserCreateView, UserListingView, ProfileUpdateView, ListingCreateView, ListingDetailedView, SubCategoryListingView, UserCityListingView, AnonChooseCityView, ListingUpdateView, ListingDeleteView, AnonListingsView, SortByCreatedView, SortByHighestView, SortByLowestView
from cl_api.views import  CategoryListAPIView, CategoryDetailAPIView, SubCategoryListAPIView, SubCategoryDetailAPIView, ListingListAPIView, ListingDetailAPIView, SubCategoryListingListAPIView, CategorySubcategoryListAPIView, CategoryListingListAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^user_city_listing/$', UserCityListingView.as_view(), name='user_city_listing_view'),
    url(r'^anon_choose_city/$', AnonChooseCityView.as_view(), name='anon_choose_city_view'),
    url(r'^anon_choose_city/anon_listings$', AnonListingsView.as_view(), name='anon_listing_view'),
    url(r'^(?P<pk>\d+)/$', SubCategoryListingView.as_view(), name='subcategory_listing_view'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^user_create/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/listings/$', UserListingView.as_view(), name='user_listing_view'),
    url(r'^details/(?P<pk>\d+)/$', ListingDetailedView.as_view(), name='listing_detailed_view'),
    url(r'^accounts/profile/listings/update_listing/(?P<pk>\d+)/$', ListingUpdateView.as_view(), name='update_listing_view'),
    url(r'^accounts/profile/listings/delete_listing/(?P<pk>\d+)/$', ListingDeleteView.as_view(), name='delete_listing_view'),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^listing_create/$', ListingCreateView.as_view(), name='listing_create_view'),
    url(r'^sort_by_created/(?P<pk>\d+)/$', SortByCreatedView.as_view(), name='sort_by_created_view'),
    url(r'^sort_by_highest/(?P<pk>\d+)/$', SortByHighestView.as_view(), name='sort_by_highest_view'),
    url(r'^sort_by_lowest/(?P<pk>\d+)/$', SortByLowestView.as_view(), name='sort_by_lowest_view'),
    url(r'^api/categories/$',CategoryListAPIView.as_view(), name='category_list_api_view'),
    url(r'^api/categories/(?P<pk>\d+)/$', CategoryDetailAPIView.as_view(), name='category_detail_api_view'),
    url(r'^api/categories/(?P<pk>\d+)/subcategories/$', CategorySubcategoryListAPIView.as_view(), name='category_subcategory_list_api_view'),
    url(r'^api/categories/(?P<pk>\d+)/listings/$', CategoryListingListAPIView.as_view(), name='category_listing_list_api_view'),
    url(r'^api/subcategories/$', SubCategoryListAPIView.as_view(), name='subcategory_list_api_view'),
    url(r'^api/subcategories/(?P<pk>\d+)/$', SubCategoryDetailAPIView.as_view(), name='subcategory_detail_api_view'),
    url(r'^api/subcategories/(?P<pk>\d+)/listings/$', SubCategoryListingListAPIView.as_view(), name="subcategory_listing_list_api_view"),
    url(r'^api/listings/$', ListingListAPIView.as_view(), name="listing_list_api_view"),
    url(r'^api/listings/(?P<pk>\d+)/$', ListingDetailAPIView.as_view(), name="listing_detail_api_view"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
