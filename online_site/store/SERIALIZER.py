from venv import create

from rest_framework import serializers
from .models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  ='__all__'



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name','category','description','price', 'have','created']

