from django.test import TestCase 
from restaurant.views import MenuItemView
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer
import json
# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self):
        self.burger = MenuItem.objects.create(
            title='Burger',
            price=9.99,
            inventory = 15
        )
        self.pizza = MenuItem.objects.create(
            title='Pizza',
            price=12.99,
            inventory = 20
        )
        self.salad = MenuItem.objects.create(
            title='Salad',
            price=7.99,
            inventory = 10
        )

    def test_getall(self):
        # Get all menu items
        menu = MenuItem.objects.all()
        serialized_menu = MenuSerializer(menu, many=True)
        response = self.client.get('/api/menu/')
        response_data = json.loads(response.content)

        # Make sure the serialized data equals the response
        self.assertEqual(serialized_menu.data, response_data)
        self.assertEqual(response.status_code, 200)
