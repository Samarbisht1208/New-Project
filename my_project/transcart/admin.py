from django.contrib import admin
from .models import User, Buyer, Item


# Register your models here.
admin.site.register(User)
admin.site.register(Buyer)
admin.site.register(Item)