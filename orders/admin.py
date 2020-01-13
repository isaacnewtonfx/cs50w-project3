from django.contrib import admin
from .models import Menu, MenuItem,Topping, Order, OrderDetail


class MenuItemAdmin(admin.TabularInline):
    # list_display = ('menu','name','small_price','large_price')
    search_fields = ('name',)
    model = MenuItem


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    inlines = [MenuItemAdmin]


class ToppingAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class OrderDetailAdmin(admin.TabularInline):
    # list_display = ('order','menu_item','qty','price','date_created','date_modified')
    search_fields = ('order',)
    model = OrderDetail

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_by','total','status','date_created','date_modified')
    search_fields = ('order_by',)
    inlines =[OrderDetailAdmin]



admin.site.register(Menu, MenuAdmin)
#admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderDetail, OrderDetailAdmin)