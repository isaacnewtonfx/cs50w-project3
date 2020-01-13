from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

from .models import Menu, MenuItem, Topping, Order, OrderDetail

# Handle orders page
def index(request):

    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'You are not logged in')
        return render(request, 'users/login.html')
    else:

        # Data
        Menus = Menu.objects.all()
        Toppings = Topping.objects.all()
        singlePrice = ['Pasta', 'Salads']
        smallAndLargePrice = ['Regular Pizza','Sicilian Pizza','Subs','Dinner Platters']

        CartTotal = 0
        for CartItem in request.session.get('Cart'):
            CartTotal = round(CartTotal + (int(CartItem['qty']) * float(CartItem['price'])), 2)


        context = {'Menus': Menus, 
                    'Toppings': Toppings,
                    'singlePrice': singlePrice, 
                    'smallAndLargePrice': smallAndLargePrice, 
                    'CartTotal': CartTotal}

        return render(request, 'orders/index.html', context)


def add_to_cart(request):

    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'You are not logged in')
        return render(request, 'users/login.html')

    elif request.method != "POST":
        return HttpResponseRedirect(reverse('index'))

    else:
        
        # process add to cart
        itemId = request.POST.get('itemId', None)
        itemName = request.POST.get('itemName', None)
        qty = 1 if request.POST.get('qty') == "" else request.POST.get('qty',1)
        price = request.POST.get('price', 0)
        topping1 = "" if request.POST.get('topping1') == "" else request.POST.get('topping1',"")
        topping2 = "" if request.POST.get('topping2') == "" else request.POST.get('topping2',"")
        topping3 = "" if request.POST.get('topping3') == "" else request.POST.get('topping3',"")
        toppings_list = [t for t in [topping1, topping2 , topping3] if t!=""]
        toppings = str(toppings_list).strip("[]").replace("'", "")

        # Create a Cart Item
        cartItem = {
            'id': itemId,
            'name' : itemName,
            'qty': qty,
            'price': price,
            'toppings': toppings
        }

        # Add Cart Item to Session
        Cart = request.session.get('Cart', [])
        Cart.append(cartItem)
        request.session['Cart'] = Cart

        # print(itemId)
        # print(itemName)
        # print(qty)
        # print(price)
        # print(toppings)

        return HttpResponseRedirect(reverse('index'))



def empty_cart(request):

    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'You are not logged in')
        return render(request, 'users/login.html')

    request.session['Cart'] = []
    return HttpResponseRedirect(reverse('index'))


def remove_cart_item(request, id):

    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'You are not logged in')
        return render(request, 'users/login.html')

    Cart = request.session.get('Cart', [])

    NewCart = [CartItem  for CartItem in Cart if CartItem['id'] != str(id)]
    request.session['Cart'] = NewCart
    return HttpResponseRedirect(reverse('index'))
    


def preview_checkout(request):

    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'You are not logged in')
        return render(request, 'users/login.html')

    CartTotal = 0
    for CartItem in request.session.get('Cart'):
        CartTotal = round(CartTotal + (int(CartItem['qty']) * float(CartItem['price'])), 2)


    return render(request, 'orders/preview-checkout.html', {'CartTotal': CartTotal})


def process_order(request):

    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'You are not logged in')
        return render(request, 'users/login.html')

    # Make sure there are items in the cart
    if len(request.session.get('Cart')) > 0:

        # Create the Order
        CartTotal = 0
        for CartItem in request.session.get('Cart'):
            CartTotal = round(CartTotal + (int(CartItem['qty']) * float(CartItem['price'])), 2)

        NewOrder = Order(order_by = request.user, total = CartTotal)
        NewOrder.save()


        # Create the Order Details
        print( len(request.session.get('Cart')) )
        for CartItem in request.session.get('Cart'):

            menuItem = MenuItem.objects.get(pk= CartItem['id'])

            NewOrderDetail = OrderDetail(order = NewOrder, 
                                        menu_item = menuItem, 
                                        qty = CartItem['qty'], 
                                        price = CartItem['price'],
                                        toppings = CartItem['toppings'])
            NewOrderDetail.save()

        # Redirect to the empty cart handle
        messages.add_message(request, messages.SUCCESS, 'Your order has been placed')
        return HttpResponseRedirect(reverse('empty_cart'))

    else:
        messages.add_message(request, messages.WARNING, 'Your cart is empty')
        return HttpResponseRedirect(reverse('index'))

def my_orders(request):

    if not request.user.is_authenticated:
        messages.add_message(request, messages.WARNING, 'You are not logged in')
        return render(request, 'users/login.html')

    MyOrders = Order.objects.filter(order_by = request.user)
    return render(request, 'orders/my-orders.html', {'MyOrders': MyOrders})