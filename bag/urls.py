from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_product_to_bag, name='add_product_to_bag'),
    path('update/<item_id>/', views.update_bag_quantity, name='update_bag_quantity'),
    path('delete/<item_id>', views.delete_bag_product, name='delete_bag_product'),
]