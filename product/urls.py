from django.urls import path
from . import views

urlpatterns = [
    # 기존 URL 매핑들...
    path('', views.main_page, name='home'),
    path('list/', views.product_list, name='product-list'),
    path('<int:pk>/', views.product_detail, name='product-detail'),
    # 기타 URL 매핑들...
]
