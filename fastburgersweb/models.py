from django.db import models

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100)    
    
#     class Meta:
#         verbose_name = ("Category")
#         verbose_name_plural = ("Categories")

#     def __str__(self):
#         return self.name

class Product(models.Model):
    CATEGORIES = [
        ('CARNE', 'Hambúrguer de carne'),
        ('FRANGO', 'Hambúrguer de frango'),
        ('ACOMPANHAMENTO', 'Acompanhamento'),
        ('SOBREMESA', 'Sobremesa'),
        ('VEGETARIANO', 'Vegetariano'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_url = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='carne')
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.title #name to be shown when called

class Store(models.Model):
    FEDERATIONS = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AM', 'Amazonas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),		
	    ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins'),    
    ]
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    uf = models.CharField(max_length=10, choices=FEDERATIONS, default='SC')
    email = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("Store")
        verbose_name_plural = ("Stores")

    def __str__(self):
        return self.name #name to be shown when called

class Coupon(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_special = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Coupon")
        verbose_name_plural = ("Coupons")

    def __str__(self):
        return self.title #name to be shown when called