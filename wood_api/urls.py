from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/data/', include('data.urls')),
    path('api/order/', include('order.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/news/', include('news.urls')),
    path('api/shop/', include('shop.urls')),

    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)