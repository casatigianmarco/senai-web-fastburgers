from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Store, Coupon, Product

def do_logout(request):
    print("me voi")
    logout(request)
    return redirect('/')

def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("foi")
            login(request, user)
            return redirect("/")
        else:
            return redirect('/login?erro=true')
    else:
        mensagem_erro = 'Usuário e/ou senha não conferem.' if 'erro' in request.GET else ''
    return render(request, "login.html", { "mensagem_erro": mensagem_erro })

def product_view(request, product_id):
    coupon = Coupon.objects.select_related('product', 'store').get(id=product_id)
    return render(request, "product-view.html", { "coupon": coupon })

# Create your views here.
def index(request): # index view
    stores = Store.objects.all()
    if request.method == "POST":
        if "filter-task" in request.POST:
            price = int(request.POST["price-range"])
            store = request.POST["select-stores"]
            category = request.POST["select-categories"]
            specials = Coupon.objects.select_related('product').filter(
                    is_special=1
                ).filter(
                    price__gte=price-5
                ).filter(
                    price__lte=price+5
                ).filter(
                    store=int(store)
                ).filter(
                    product__category=category
                )
            all = Coupon.objects.select_related('product').all().filter(
                    is_special=0
                ).filter(
                    price__gte=price-5
                ).filter(
                    price__lte=price+5
                ).filter(
                    store=int(store)
                ).filter(
                    product__category=category
                )
            return render(request, "index.html", { "stores": stores, "specials": specials, "all": all })
    specials = Coupon.objects.select_related('product').filter(is_special=1)
    all = Coupon.objects.select_related('product').all().filter(is_special=0)
    return render(request, "index.html", { "stores": stores, "specials": specials, "all": all })
