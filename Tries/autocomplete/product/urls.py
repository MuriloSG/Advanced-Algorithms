from django.urls import path
from .views import  ProductAutocompleteView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('autocomplete/', ProductAutocompleteView.as_view(), name='autocomplete'),
]
