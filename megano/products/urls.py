from django.urls import path
from .views import (ProductsList,
                    PopularProductsList,
                    LimitedEditionList,
                    ProductDetails,
                    TagsList,
                    SalesList,
                    CategoriesList,
                    ReviewCreate,
                    BannersList
                    )

urlpatterns = [
    path('api/catalog/', ProductsList.as_view(), name='products_list'),
    path('api/products/popular/', PopularProductsList.as_view(), name='products_popular'),
    path('api/products/limited/', LimitedEditionList.as_view(), name='products_limited'),
    path('api/product/<int:pk>/', ProductDetails.as_view(), name='product_details'),
    path('api/product/<int:pk>/reviews', ReviewCreate.as_view(), name='review_create'),
    path('api/tags/', TagsList.as_view(), name='tags_list'),
    path('api/sales/', SalesList.as_view(), name='sales_list'),
    path('api/categories/', CategoriesList.as_view(), name='categories_list'),
    path('api/banners/', BannersList.as_view(), name='banners_list'),
]
