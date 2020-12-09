from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from .models import Store, Coupon, Product, Favorite

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        users = get_user_model().objects.filter(email=email)
        print(len(users))
        if len(users) == 0:
            new_user = get_user_model().objects.create_user(username, email, password)
            new_user.save()
            login(request, new_user)
            return redirect("/")
        else:
            return redirect('/signin?erro=true')
    else:
        mensagem_erro = 'Usuário já existente.' if 'erro' in request.GET else ''
    return render(request, "signin.html", { "mensagem_erro": mensagem_erro })


def do_logout(request):
    logout(request)
    return redirect('/')

def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect('/login?erro=true')
    else:
        mensagem_erro = 'Usuário e/ou senha não conferem.' if 'erro' in request.GET else ''
    return render(request, "login.html", { "mensagem_erro": mensagem_erro })

def coupon(request, coupon_id):
    coupon = Coupon.objects.select_related('product', 'store').get(id=coupon_id)
    return render(request, "coupon.html", { "coupon": coupon })

def like(request, coupon_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    favorites = Favorite.objects.filter(user_id=request.user.id, coupon_id=coupon_id)
    if len(favorites) == 0:
        new_favorite = Favorite.objects.create(user_id=request.user.id, coupon_id=coupon_id)
        new_favorite.save()
    return redirect('/favorites')

def dislike(request, coupon_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    try:
        favorite = Favorite.objects.get(user_id=request.user.id, coupon_id=coupon_id)
    except (get_user_model().DoesNotExist):
        favorite = None

    if favorite is not None:
        favorite.delete()
        
    return redirect('/favorites')

def favorites(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    favorites = Favorite.objects.select_related('coupon').filter(user_id=request.user.id)
    return render(request, "favorites.html", {"favorites": favorites})

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
    all = Coupon.objects.select_related('product').filter(is_special=0)
    return render(request, "index.html", { "stores": stores, "specials": specials, "all": all })
