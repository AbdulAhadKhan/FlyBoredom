from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:offer_id>', views.add_to_cart, name='add_to_cart'),
    path('update/<int:cart_item_id>', views.update_number_of_people, name='update_number_of_people'),
    path('remove/<int:cart_item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('checkout', views.checkout, name='checkout'),
]