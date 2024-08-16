from django.urls import path,include
from . import views

urlpatterns = [
    path('categories', views.GetCategories.as_view()),
    path('services', views.GetServices.as_view()),
    path('service/<slug>', views.GetService.as_view()),
    path('category/<slug>', views.GetCategory.as_view()),
    path('subcategory/<slug>', views.GetSubCategory.as_view()),
    path('product/<slug>', views.GetProduct.as_view()),
    path('popular', views.GetPopularProducts.as_view()),
]
