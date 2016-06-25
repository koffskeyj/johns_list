from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from craigs_list.models import Category, SubCategory, Profile, Listing

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


class ListingCreateView(CreateView):
    model = Listing
    fields = ["listing_category", "listing_subcategory", "title", "description", "value", "photo"]
    success_url = "/"

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.user = self.request.user
        return super(ListingCreateView, self).form_valid(form)

class UserListingView(ListView):

    def get_queryset(self):
        return Listing.objects.filter(user=self.request.user)


class SubCategoryListingView(ListView):

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(listing_subcategory_id=category_id)


class CityListingView(ListView):

    fields = ["city"]

    def get_queryset(self, **kwargs):
        return Listing.objects.filter(city=fields)


class UserListingDetailedView(DetailView):
    model = Listing

class ProfileUpdateView(UpdateView):

    fields = ["city"]
    success_url = reverse_lazy("profile_update_view")

    def get_object(self, queryset=None):
        return self.request.user.profile
