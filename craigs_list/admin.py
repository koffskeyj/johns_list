from django.contrib import admin

from craigs_list.models import Profile, Listing, Category, SubCategory

admin.site.register(Profile)
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(SubCategory)
