from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (CategoryListView, ContactsTemplateView,
                           ProductCreateView, ProductDeleteView,
                           ProductDetailView, ProductListView,
                           ProductsByCategoryView, ProductUpdateView)

app_name = CatalogConfig.name
urlpatterns = [
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_list/<int:pk>/update",
        ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product_list/<int:pk>/delete",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "category/<int:pk>/",
        ProductsByCategoryView.as_view(),
        name="products_by_category",
    ),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
]
