from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import BLANK_CHOICE_DASH, DateTimeCheckMixin
from django.utils.regex_helper import flatten_result

class User(AbstractUser):
    pass

class bids(models.Model):
    ammount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_user")
    def __str__(self):
        return f"{self.priceOfBid}, {self.user}"

class categories(models.Model):
    abbreviation = models.CharField(max_length=3, unique=True, blank=False, default='NUL')
    category = models.CharField(max_length=30, unique=True, blank=False, default="NULL")
    
    def __str__(self):
        return f"{self.category}"

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    content = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}"

def filepath(request, filename):
    return f"listingImages/{request.user.id}/{request.title}/{filename}"

class listings(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings_user", blank=False)
    bids = models.ManyToManyField(bids, blank=True, related_name="bids")
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=False, default=0.00)
    categories = models.ManyToManyField(categories, blank=False, related_name="categories")
    comments = models.ManyToManyField(comments, blank=True, related_name="comments")
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

    def __str__(self):
        return f"{self.title}, {self.user}"
