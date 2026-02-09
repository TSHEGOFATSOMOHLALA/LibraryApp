from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES =[
        ('ELECTRONICS', 'Electronics'),
        ('CLOTHING', 'Clothing'),
        ('BOOKS' , 'Books'),
        ('HOME' , 'Home & Garden'),
        ('SPORTS', 'Sports'),
        ('OTHER', 'Other'),
      ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.CharField(max_length=500, blank=True , help_text = "URL of product image")
    in_stock = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name