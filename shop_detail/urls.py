from django.urls import path
from .views import (
    my_shop_view,
    shop_list_view,
    shop_create_view,
)

urlpatterns = [
    path('', my_shop_view),
    path('news/', shop_list_view),
    path('news-create/', shop_create_view),
]
