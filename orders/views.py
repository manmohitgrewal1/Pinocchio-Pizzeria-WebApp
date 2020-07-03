from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import *
from django.apps import apps
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegisterForm


# Create your views here.
objects_models= {'list_item':{"Sicilian Pizza": SicilianPizza,
                    "Regular Pizza": RegularPizza,
                    "Salad":Salad,
                    "Pasta":Pasta,
                    "Dinner Platter":DinnerPlatter,
                    "Subs": Subs
                    }
                    }


def register(request):
    """  With the help of UserRegisterForm a form format is sent to the register.html template were the user enters
        the username, email, password. When the user clicks the submit button the form data gets submitted and the 
        same is retrived with the help of request.POST. Subsequestly the user model is created.   """
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid:
            username= request.POST['username']
            password= request.POST['password1']
            user=form.save()
            messages.success(request,f"Account created for {user}!")
            User.objects.create(username= username, password=password)
            return HttpResponseRedirect(reverse('orders:login'))
        else:
            return HttpResponse("Invalid input")
    else:
        form= UserRegisterForm
        context={'form': form}
        return render(request, 'orders/register.html', context)

@login_required
def index(request, **kwargs):
    """  This function render index.html template in which a user can- from given menu- select item to oreder.
    Once the user has selected which item to order the same info is posted to this function. The api will then
    gather required info realated with the item and send it along with the index.html template. Note: diffrent if 
    conditions are used to deal with diffrent type of item as each item is structured diffrently.  """
    if request.method=='POST':
        if 'choices' in request.POST:
            try:
                selected_item=request.POST['choices']
                for run in objects_models['list_item']:
                    if selected_item== run:
                        detail= objects_models['list_item'][run].__name__
                        return HttpResponseRedirect(reverse('orders:index', kwargs=({'detail':objects_models['list_item'][run].__name__})))
            except:
                return HttpResponseRedirect(reverse('orders:index'))
        
    else:
        detail= kwargs.get('detail', False)
        for run in objects_models['list_item']:
            if detail== objects_models['list_item'][run].__name__:
                if detail=='SicilianPizza' or detail== 'RegularPizza':
                    toppings= Topping.objects.all()
                    selected_model=objects_models['list_item'][run].objects.all()
                    menu={}
                    for runner in selected_model:
                        price_list=[]
                        price_list.append(runner.small)
                        price_list.append(runner.large)
                        menu[runner.item]= price_list
                    size= 'No'
                    try:
                        if objects_models['list_item'][run].large:
                            size= 'Yes'
                    finally:
                        context ={'list_item':{"Sicilian Pizza": SicilianPizza,
                        "Regular Pizza": RegularPizza,
                        "Salad":Salad,
                        "Pasta":Pasta,
                        "Dinner Platter":DinnerPlatter,
                        "Subs": Subs
                        },
                        "clicked_item": detail,
                        "size": size,
                        "clicked_item_details": selected_model,
                        'toppings':toppings,
                        "menu": menu}
                        return render(request, 'orders/index.html', context)
                
                elif detail=='Subs':
                    toppings= SubTopping.objects.all()
                    selected_model=objects_models['list_item'][run].objects.all()
                    menu={}
                    for runner in selected_model:
                        price_list=[]
                        price_list.append(runner.small)
                        price_list.append(runner.large)
                        menu[runner.item]= price_list
                        
                    subtopping= {}
                    subtoppings= SubTopping.objects.all()
                    for runner in subtoppings:
                        price_list= []
                        price_list.append(runner.small)
                        price_list.append(runner.large)
                        subtopping[runner.item]= price_list
                    size= 'No'
                    try:
                        if objects_models['list_item'][run].large:
                            size= 'Yes'
                    finally:
                        context ={'list_item':{"Sicilian Pizza": SicilianPizza,
                        "Regular Pizza": RegularPizza,
                        "Salad":Salad,
                        "Pasta":Pasta,
                        "Dinner Platter":DinnerPlatter,
                        "Subs": Subs
                        },
                        "clicked_item": detail,
                        "size": size,
                        "clicked_item_details": selected_model,
                        "toppings": toppings,
                        "menu": menu,
                        "subtopping": subtopping}                       
                        return render(request, 'orders/index.html', context) 
  
                else:
                    selected_model=objects_models['list_item'][run].objects.all()
                    menu={}
                    if detail== "DinnerPlatter":
                        for runner in selected_model:
                            price_list=[]
                            price_list.append(runner.small)
                            price_list.append(runner.large)
                            menu[runner.item]= price_list
                    else:
                        for runner in selected_model:
                            price_list=[]
                            price_list.append(runner.price)
                            
                            menu[runner.item]= price_list
                    size= 'No'
                    try:
                        if objects_models['list_item'][run].large:
                            size= 'Yes'
                    finally:
                        context ={'list_item':{"Sicilian Pizza": SicilianPizza,
                            "Regular Pizza": RegularPizza,
                            "Salad":Salad,
                            "Pasta":Pasta,
                            "Dinner Platter":DinnerPlatter,
                            "Subs": Subs
                            },
                            "clicked_item": detail,
                            'size':size,
                            "clicked_item_details": selected_model,
                            "menu": menu}
                        return render(request, 'orders/index.html', context)        
        return render(request, 'orders/index.html', objects_models)


@login_required
def cart(request):
    """  Once the user has selected the order, form contating order information is posted to cart function. 
    using the posted data order is created with the help of model class. """
    if request.method == "POST":
        if "selected_item" in request.POST:
            try:
                selected_varient= request.POST['selected_item']
                model_name=selected_varient.split()      
                if model_name[1] == 'Pasta' or model_name[1] ==  'Salad':
                    mdl= apps.get_model(app_label='orders', model_name=model_name[1])
                    order_entry=mdl.objects.get(item= model_name[0])
                    price= order_entry.price
                    active_user= request.user.username
                    customer= User.objects.get(username= active_user)
                    # Creating the ORDER
                    placed_order= Order.objects.create(item=model_name[1], varient= model_name[0], amount= price)
                    placed_order.user.add(customer)
                    messages.success(request, "ORDER ADDED TO CART!")
                else:
                    mdl= apps.get_model(app_label='orders', model_name=model_name[1])
                    order_entry=mdl.objects.get(item= model_name[0])
                    active_user= request.user.username
                    customer= User.objects.get(username= active_user)
                    size= request.POST['size']
                    order_price= getattr(order_entry, size)
                    topping_list= request.POST.getlist('selected_toppings')
                    if ((model_name[1] == 'RegularPizza' or model_name[1] == 'SicilianPizza') and  model_name[0] != "Cheese" and model_name[0] != "Special"):
                        toppings=[Topping.objects.get(item= run) for run in topping_list]   
                    elif ((model_name[1] == 'RegularPizza' or model_name[1] == 'SicilianPizza') and model_name[0] == "Special"):                        
                        toppings= list(Topping.objects.order_by()[:5]) 
                    else:
                        toppings=[SubTopping.objects.get(item= run) for run in topping_list]    
                    # Creating the ORDER 
                    placed_order= Order.objects.create(item=model_name[1], varient= model_name[0], amount= order_price, size= size, status="P")
                    placed_order.user.add(customer)
                    if model_name[1] =='RegularPizza' or model_name[1] == 'SicilianPizza':
                        for run in range(0, len(toppings)):
                            top_pop=toppings.pop()
                            placed_order.topping.add(top_pop)
                    elif model_name[1] =='Subs':
                        for run in range(0, len(toppings)):
                            top_pop=toppings.pop()
                            placed_order.sub_topping.add(top_pop)
                    messages.success(request, "ORDER ADDED TO THE CART!")
                return HttpResponseRedirect(reverse('orders:index'))
            except Exception as e:
                print(e)
                messages.warning(request, "PLEASE SELECT A VALID ITEM!")
                return HttpResponseRedirect(reverse('orders:index'))
        else:
            print(request.POST)
            pk= int(request.POST['remove'])
            active_user=request.user
            user= User.objects.get(username= active_user)
            orders= user.order.all()
            orders[pk-1].delete()
            
            return HttpResponseRedirect(reverse("orders:cart"))
    else:
        active_user=request.user
        user= User.objects.get(username= active_user)
        orders= user.order.all()
        order_package={}
        total=0
        counter=1
        checker=1
        status= "Confirmed"
        for order in orders:
            if order.topping.all():
                topping= order.topping.all()
                total+= order.amount
                order_package[counter]= [order.item, order.varient,topping ,order.size, order.amount] 
                if order.status == "P":
                    status="Pending"
            elif order.sub_topping.all():
                toppings= order.sub_topping.all()
                subs_total=order.amount
                total+= order.amount
                for topping in toppings:
                    subs_total+= getattr(topping, order.size)
                order_package[counter]= [order.item, order.varient,toppings ,order.size, subs_total] 
                if order.status == "P":
                    status="Pending"
            else:
                total+= order.amount
                order_package[counter]= [order.item, order.varient, order.size, order.amount] 
                if order.status == "P":
                    status="Pending"
            counter+=1
        context={
            "user": active_user,
            "order_package": order_package,
            "total": round(total,2),
            "status": status
        }
        return render(request, 'orders/cart.html', context)   