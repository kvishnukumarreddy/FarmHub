from django.shortcuts import render,redirect
from .models import Product,Cart,Order
from django.core.paginator import Paginator
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')


def products(request):
    query = request.GET.get('q')

    if query:
        product_list = Product.objects.filter(name__icontains=query)
    else:
        product_list = Product.objects.all()

    paginator = Paginator(product_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'products.html', {'products': products})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(request, username=username, password=password)

        print("USER:", user)

        if user is not None:
            login(request, user)
            messages.success(request,"Login Successfull")
            return redirect('/')
        else:
            messages.error(request,"Invalid Username or Password")
            return render(request, 'login.html',)

    return render(request, 'login.html')


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    product = Product.objects.get(id=product_id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/products/')
def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    cart_items = Cart.objects.filter(user=request.user)

    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def increase_quantity(request, item_id):
    item = Cart.objects.get(id=item_id)
    item.quantity += 1
    item.save()
    return redirect('/cart/')


def decrease_quantity(request, item_id):
    item = Cart.objects.get(id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('/cart/')


def remove_from_cart(request, item_id):
    item = Cart.objects.get(id=item_id)
    item.delete()
    return redirect('/cart/')

def buy_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    for item in cart_items:
        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return render(request, 'buy.html')



@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})