from django.db import models

# Create your models here.
class Order(models.Model): # type: ignore
    order_number = models.CharField(max_length=50)

    def __str__(self):  
        return self.order_number 
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items', on_delete=models.CASCADE)
    products_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.products_name} ({self.quantity})"