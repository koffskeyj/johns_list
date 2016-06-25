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
from craigs_list.views import IndexView, UserCreateView, UserListingView, ProfileUpdateView, ListingCreateView, UserListingDetailedView, SubCategoryListingView, CityListingView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^city_listing/$', CityListingView.as_view(), name='city_listing_view'),
    url(r'^(?P<pk>\d+)/$', SubCategoryListingView.as_view(), name='subcategory_listing_view'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^user_create/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/listings/details/(?P<pk>\d+)/$', UserListingDetailedView.as_view(), name='user_listing_detailed_view'),
    url(r'^accounts/profile/listings/$', UserListingView.as_view(), name='user_listing_view'),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^listing_create/$', ListingCreateView.as_view(), name='listing_create_view')
]
