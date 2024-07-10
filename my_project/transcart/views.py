from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Buyer, Item



# Create your views here.
def index(request):
    all_products = Item.objects.all()
    return render(request, "transcart/index.html", {
        "content_placeholder": all_products
    })

def my_products(request):
    current_user = request.user
    products = Item.objects.filter(owner=current_user)
    return render(request, "transcart/my_products.html", {
        "content_placeholder": products
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        type = request.post["type"]
        user = authenticate(request, username=username, password=password, type=type)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "transcart/login.html", {
                "message": "Invalid username and/or password and/or type."
            })
    else:
        return render(request, "transcart/login.html")
    

def vender_login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        type = request.post["type"]
        user = authenticate(request, username=username, password=password, type=type)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "transcart/vender_login.html", {
                "message": "Invalid username and/or password and/or type."
            })
    else:
        return render(request, "transcart/vender_login.html")
    


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        type = request.POST["type"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "transcart/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password, type=type)
            user.save()
        except IntegrityError:
            return render(request, "transcart/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "transcart/register.html")


def vender_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        type = request.POST["type"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "transcart/vender_register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password, type=type)
            user.save()
        except IntegrityError:
            return render(request, "transcart/vender_register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "transcart/vender_register.html")
    

def createListing(request):
    if request.method == 'GET':
        return render(request, "transcart/create.html")
    else:
        name = request.POST["title_data"]
        price = request.POST["price_data"]
        image = request.POST["image_data"]

        current_user = request.user

        new_item = Item(
            owner = current_user,
            name = name,
            prize = price,
            imageURL = image,
        )

        new_item.save()
        return HttpResponseRedirect(reverse(index))
    
def watchlist(request):
    current_user = request.user
    listing = current_user.listing_watchlist_related_name.all()
    return render(request, "transcart/watchlist.html", {
        "content_placeholder": listing
    })

def listing_function(request, id):
    listing_data = Item.objects.get(pk = id)
    is_listing_in_watchlistlist = request.user in listing_data.watchlist.all()
    is_owner = request.user.username == listing_data.owner.username
    return render(request, "transcart/listing.html", {
        "listing_content_placeholder": listing_data,
        "is_listing_in_watchlistlist_placeholder": is_listing_in_watchlistlist,
        "is_owner_placeholder": is_owner,
        "update_placeholder": "kuch_bhi_nhi",
    })

def Remove(request, id):
    listing_data = Item.objects.get(pk = id)
    current_user = request.user
    listing_data.watchlist.remove(current_user)
    return HttpResponseRedirect(reverse("listing", args=(id, )))

def Add(request, id):
    listing_data = Item.objects.get(pk = id)
    current_user = request.user
    listing_data.watchlist.add(current_user)
    return HttpResponseRedirect(reverse("listing", args=(id, )))