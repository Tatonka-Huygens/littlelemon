from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu

class MenuViewTest(TestCase):
    Menu.objects.setup(title="IceCream", price=80, inventory=100)
    Menu.test_getall()