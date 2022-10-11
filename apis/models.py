from django.db import models
import random
rand_num = random.randrange(1, 999999)


# Create your models here.
class Product(models.Model):
    """Model definition for MODELNAME."""
    product_name = models.CharField(max_length=50)
    size = models.CharField(max_length=2)
    colour  = models.CharField(max_length=20)
    price = models.CharField(max_length=150)
    image = models.ImageField(null=True)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.product_name

   

class Customer(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150)
    postcode = models.CharField(max_length=150)
    def __str__(self):
        return self.email




class OrderProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    order_number = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        self.order_number = rand_num
        super(OrderProduct, self).save(*args, **kwargs)
    def __str__(self):
        return self.product.product_name




