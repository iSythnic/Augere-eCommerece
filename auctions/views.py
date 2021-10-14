from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import User, listings, comments, categories, bids


class Error():
    def __init__(self, type : int, content : str):
        self.type = type
        self.content = content

class Errors():
    def __init__(self):
        pass

    def NotFound():
        return Error(404, "Page not found!")

        
        
def index(request):
    
    return render(request, "auctions/index.html",
    {
        "listings" : listings.objects.all() 
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def product_View(request, TITLE, id):

    try:

        product = listings.objects.get(pk=id)

        return render(request, "auctions/product.html",
        {
            "listing": product
        })

    except ObjectDoesNotExist:

        return render(request, "auctions/error.html",
        {
            "error": Errors.NotFound()
        })
    

