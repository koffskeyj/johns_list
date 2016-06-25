from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from craigs_list.models import Category, SubCategory, Profile, Listing
from django.contrib.auth.mixins import LoginRequiredMixin
from craigs_list.forms import CityForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        # context["subcategories"] = SubCategory.objects.all()
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/login"


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ["listing_category", "listing_subcategory", "title", "description", "value", "photo"]
    success_url = "/"

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.user = self.request.user
        return super(ListingCreateView, self).form_valid(form)

class UserListingView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Listing.objects.filter(user=self.request.user)


class SubCategoryListingView(ListView):

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(listing_subcategory_id=category_id)


class UserCityListingView(ListView):
    template_name = "user_city_listing.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Listing.objects.filter(city=self.request.user.profile.city).exclude(user=self.request.user)


class AnonChooseCityView(FormView):
    template_name = "anon_choose_city.html"
    form_class = CityForm



class ListingDetailedView(LoginRequiredMixin, DetailView):
    model = Listing


class ProfileUpdateView(UpdateView):
    fields = ["city"]
    success_url = reverse_lazy("profile_update_view")

    def get_object(self, queryset=None):
        return self.request.user.profile
