from django.urls import path
from .views import main_func, category_fiter,product_filter,product_detail,search_products


urlpatterns = [
    path('', main_func, name="home"),
    path('search/', search_products, name='search_products'),
    path('fruits_detail/<int:id>', product_detail, name='product_detail'),
    path('filter/<int:id>', category_fiter, name="product_filter"),
    path('filter/<str:data>', product_filter, name="product_filter")
]