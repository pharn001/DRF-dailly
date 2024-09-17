from rest_framework import serializers
from .models import Order,OrderItem

class OrderItemSerializers(serializers.ModelSerializer):
   class Meta:
    
    model = OrderItem
    fields =  ['products_name', 'quantity']

class OrderSerializers(serializers.ModelSerializer):
  items = OrderItemSerializers(many=True)
  class Meta:
    model = Order
    fields =  ['order_number', 'items']

 