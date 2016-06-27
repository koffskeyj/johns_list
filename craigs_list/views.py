from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.template import RequestContext
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
    fields = ["listing_category", "listing_subcategory", "title", "description", "value", "city", "photo"]
    success_url = "/"

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.user = self.request.user
        return super(ListingCreateView, self).form_valid(form)

class UserListingView(LoginRequiredMixin, ListView):
    template_name = "user_listing.html"

    def get_queryset(self):
        return Listing.objects.filter(user=self.request.user)


class SubCategoryListingView(ListView):

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(listing_subcategory_id=category_id)


class UserCityListingView(ListView):
    template_name = "user_city_listing.html"

    def get_queryset(self, **kwargs):
        if self.request.user.is_authenticated:
            profile = Profile()
            return Listing.objects.filter(city=user_instance.user_profile).exclude(user=self.request.user)


class AnonChooseCityView(FormView):
    template_name = "anon_choose_city.html"
    form_class = CityForm
    success_url = "/anon_choose_city/anon_listings"

    # def form_valid(self, form):
        # city_choice = form.save(commit=False)
        # city_choice.city = Profile.city
        # return super(AnonChooseCityView, self).form_valid(form)

    # def get_city(request):
        # if request.method == "POST":
            # form = CityForm(request.POST)
            # if form.is_valid():
                # clean_city = form.cleaned_data["city"]
        # else:
            # form = CityForm()
        # return render_to_response("craigs_list/anon_listing_list.html", {"form" : form}, context_instance=RequestContext(request))

class AnonListingsView(ListView):
    template_name = "craigs_list/anon_listing_list.html"


    def get_queryset(self):
        form = CityForm()
        if form.city == "Greenville":
            return Listing.objects.filter(city="Greenville")
    # def get_queryset(self):
        # Case(
            # When(city="Greenville", then=Listing.objects.filter(city="Greenville")),
            # When(city="Columbia", then=Listing.objects.filter(city="Columbia")),
            # When(city="Spartanburg", then=Listing.objects.filter(city="Spartanburg")))


class SortByCreatedView(ListView):
    template_name = "sort_by_created.html"

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(listing_subcategory_id=category_id).order_by("-created")


class SortByHighestView(ListView):
    template_name = "sort_by_highest.html"

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(listing_subcategory_id=category_id).order_by("-value")


class SortByLowestView(ListView):
    template_name = "sort_by_lowest.html"

    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk', None)
        return Listing.objects.filter(listing_subcategory_id=category_id).order_by("value")


class ListingDetailedView(DetailView):
    model = Listing


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    fields = ["city"]
    success_url = reverse_lazy("profile_update_view")

    def get_object(self, queryset=None):
        return self.request.user.profile

class ListingUpdateView(LoginRequiredMixin, UpdateView):
    model = Listing
    fields = ['title', 'description', 'value', 'photo']
    success_url = '/accounts/profile/listings'

    def form_valid(self, form):

        listing = form.save(commit=False)
        listing.user = self.request.user
        return super(ListingUpdateView, self).form_valid(form)

class ListingDeleteView(LoginRequiredMixin, DeleteView):
    model = Listing
    success_url = '/accounts/profile/listings'
