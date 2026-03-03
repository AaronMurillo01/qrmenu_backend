from django.contrib import admin
from django.urls import path, include, re_path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('api/places/', views.PlaceList.as_view()),
    path('api/places/<int:pk>/', views.PlaceDetail.as_view()),

    path('api/categories/', views.CategoryList.as_view()),
    path('api/categories/<int:pk>/', views.CategoryDetail.as_view()),

    path('api/menu_items/', views.MenuItemList.as_view()),
    path('api/menu_items/<int:pk>/', views.MenuItemDetail.as_view()),

    path('api/create_payment_intent/', views.create_payment_intent),

    path('api/orders/', views.OrderList.as_view()),
    path('api/orders/<int:pk>/', views.OrderDetail.as_view()),

    # Catch-all for the React SPA — must be last, only matches non-API paths
    re_path(r'^(?!api/|admin/|auth/).*$', views.home),
]
