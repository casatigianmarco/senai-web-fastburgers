from django.http import Http404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from fastburgersweb.models import Product, Store, Coupon
from .serializers import ProductSerializer, StoreSerializer, CouponSerializer

# Create your views here.
class ProductList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        params = request.query_params
        products = Product.objects.all()
        if 'category' in params:
            category_filter = params.get('category')
            products = products.filter(category=category_filter)        
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StoreList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        params = request.query_params
        stores = Store.objects.all()
        if 'uf' in params:
            uf_filter = params.get('uf')
            stores = stores.filter(uf=uf_filter)        
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoreDetail(APIView):    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        store = self.get_object(pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CouponList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        params = request.query_params
        coupons = Coupon.objects.all()
        if 'store' in params:
            try:
                store_filter =  int(params.get('store'))
            except ValueError:
                # Handle the exception
                print('Please enter an integer: ' + params.get('store'))
                store_filter = -1
            if store_filter > 0:
                coupons = coupons.filter(store=store_filter)
        if 'product' in params:
            try:
                product_filter =  int(params.get('product'))
            except ValueError:
                # Handle the exception
                print('Please enter an integer: ' + params.get('product'))
                product_filter = -1
            if product_filter > 0:
                coupons = coupons.filter(product=product_filter)        
        serializer = CouponSerializer(coupons, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CouponDetail(APIView):    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Coupon.objects.get(pk=pk)
        except Coupon.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        coupon = self.get_object(pk)
        serializer = CouponSerializer(coupon)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        coupon = self.get_object(pk)
        serializer = CouponSerializer(coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        coupon = self.get_object(pk)
        serializer = CouponSerializer(coupon, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        coupon = self.get_object(pk)
        coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)