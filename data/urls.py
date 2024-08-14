from django.urls import path,include
from . import views

urlpatterns = [
    path('banners', views.GetBanners.as_view()),
    path('faq', views.GetFaqs.as_view()),
    path('form', views.NewForm.as_view()),




]
