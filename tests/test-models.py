from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(ID=3, title="IceCream", price=80, inventory=2)
        self.assertEqual(str(item), "IceCream : $80")
