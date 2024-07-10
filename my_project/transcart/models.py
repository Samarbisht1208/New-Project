from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    type = models.CharField(max_length=50, null=True)

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="vender")
    name = models.CharField(max_length=500)
    prize = models.FloatField(blank=True)
    imageURL = models.CharField(max_length=1000, blank=False)
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="listing_watchlist_related_name")

    def __str__(self):
        return self.name
    

class Buyer(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="buyer")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True, related_name="item")
    numbers_of_item = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.buyer} bought {self.numbers_of_item} {self.item} "
