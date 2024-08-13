from django.urls import path
from .views import CarListView,CarDetailsView

urlpatterns = [
 path('',CarListView.as_view(),name='car_list'),
 path('<int:pk>',CarDetailsView.as_view(),name='car_details')
]