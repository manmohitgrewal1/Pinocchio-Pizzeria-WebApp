from django.contrib import admin
from orders.models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= ('get_user', 'item', 'varient', 'status','get_topping','size', 'amount')
    list_filter= ( 'item', 'varient')
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display= ('username')
    pass


@admin.register(RegularPizza)
class RegularPizzaAdmin(admin.ModelAdmin):
    list_display= ['item', 'large', 'small']
    pass


@admin.register(SicilianPizza)
class SicilianPizzaAdmin(admin.ModelAdmin):
    list_display= ['item', 'large', 'small']
    pass

@admin.register(DinnerPlatter)
class DinnerPlatterAdmin(admin.ModelAdmin):
    list_display= ['item', 'large', 'small']
    pass


@admin.register(Subs)
class SubsAdmin(admin.ModelAdmin):
    list_display= ['item', 'large', 'small']
    pass

@admin.register(Pasta)
class PastaAdmin(admin.ModelAdmin):
    list_display= ['item', 'price']
    pass

@admin.register(Salad)
class SaladAdmin(admin.ModelAdmin):
    list_display= ['item', 'price']
    pass

# Register your models here.
admin.site.register(Topping)
admin.site.register(SubTopping)
