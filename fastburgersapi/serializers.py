from fastburgersweb.models import Product, Store, Coupon
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image_url', 'category']

class StoreSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Store
        fields = ['id', 'name', 'city', 'uf', 'email']

class CouponSerializer(serializers.ModelSerializer):   
    # permite trazer o campo do objeto e não o ID
    product = serializers.SlugRelatedField(many=False, read_only=False, queryset=Product.objects.all(),slug_field='title') 
    store = serializers.SlugRelatedField(many=False, read_only=False, queryset=Store.objects.all(),slug_field='name')
    class Meta:
        model = Coupon
        fields = ['id', 'title', 'price', 'is_special', 'product', 'store']