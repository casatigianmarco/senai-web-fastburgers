from django.contrib import admin
from .models import Product, Store, Coupon
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",  "image_url", "category")

class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "uf", "email")

class CouponAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_special", "store", "product")

admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Coupon, CouponAdmin)