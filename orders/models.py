from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return 'Menu: %s' % (self.name)

class Topping(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return 'Topping: %s' % (self.name)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    small_price = models.FloatField(default = 0)
    large_price = models.FloatField(default = 0)
    allowed_toppings = models.IntegerField(default=0)

    def __str__(self):
        return 'MenuItem: %s -> %s' % (self.menu, self.name)

ORDER_CHOICES = (
    ('pending', 'PENDING'),
    ('completed', 'COMPLETED')
)
class Order(models.Model):
    order_by = models.ForeignKey(User, on_delete = models.CASCADE)
    total = models.FloatField()
    status = models.CharField(max_length=50, default="pending", choices=ORDER_CHOICES)
    date_created = models.DateField(auto_now_add = True)
    date_modified = models.DateField(auto_now = True)

    def __str__(self):
        return 'Order: By %s, Total= %s, On= %s' % (self.order_by, self.total, self.date_created)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    toppings = models.CharField(max_length=200, default="", blank=True, null=True)
    date_created = models.DateField(auto_now_add = True)
    date_modified = models.DateField(auto_now = True)

    def __str__(self):
        return 'OrderDetail: %s, Qty= %s, Price= %s, On= %s' % (self.menu_item, self.qty, self.price, self.date_created)