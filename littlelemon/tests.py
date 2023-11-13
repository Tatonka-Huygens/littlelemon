from django.test import TestCase
from restaurant.models import Menu


#TestCase class
class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        return self.assertNotEqual(item, "IceCream : 80")
        
        
        
        