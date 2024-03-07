from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Product(models.Model):
    name=models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate=models.IntegerField()
    description=models.TextField(max_length=500)
    weight=models.CharField(max_length=1)
    countryofOrigin = models.CharField(max_length=20)
    quality=models.CharField(max_length=20)
    checked=models.CharField(max_length=20)
    minWeight=models.CharField(max_length=20)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["updated_at"]



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.product.name} by {self.author}'

