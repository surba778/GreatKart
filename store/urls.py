from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
