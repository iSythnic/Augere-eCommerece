from django.contrib import admin
from .models import User, listings, comments, bids, categories

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "username")

admin.site.register(User, userAdmin)
admin.site.register(listings)
admin.site.register(comments)
admin.site.register(bids)
admin.site.register(categories)