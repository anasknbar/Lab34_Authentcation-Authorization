from django.test import TestCase

from django.contrib.auth import get_user_model
from datetime import datetime
from .models import Car
# Create your tests here.


class CarsTests(TestCase):
  
  @classmethod
  def setUpTestData(cls):
      cls.user = get_user_model().objects.create_user(
      username= 'test_user',
      email="test@email.com",
      password="1234"
  )   
      cls.car = Car.objects.create(
            model='test_model',
            brand='test_brand',
            price=10000.0,  # Ensure this is a float
            is_bought=True,
            buyer_id=cls.user,  # Assign the user instance
            buy_time=datetime(2020, 3, 7)  # Use datetime for date fields
        )
      
      
      
  def test_str_method(self):
    expected_str = f"{self.car.model}, {self.car.brand} - ${self.car.price}"
    self.assertEqual(str(self.car), expected_str)


 
