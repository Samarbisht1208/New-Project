from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("vender_login", views.vender_login_view, name="vender_login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("vender_register", views.vender_register, name="vender_register"),
    path("add_item", views.createListing, name="create_kr"),
    path("my_products", views.my_products, name="my_products"),
    path("watchlist", views.watchlist, name="watchlist"),
    path('listing/<int:id>', views.listing_function, name="listing"),
    path("add/<int:id>", views.Add, name="add"),
    path("remove/<int:id>", views.Remove, name="remove"),
]