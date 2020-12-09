from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/products/', views.ProductList.as_view()),
    path('api/products/<int:pk>/', views.ProductDetail.as_view()),
    path('api/stores/', views.StoreList.as_view()),
    path('api/stores/<int:pk>/', views.StoreDetail.as_view()),
    path('api/coupons/', views.CouponList.as_view()),
    path('api/coupons/<int:pk>/', views.CouponDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)