from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from web.views import index, product_detail, product_create, product_update,product_delete

app_name="web"

urlpatterns = [
    path("", index, name="index"),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/new/', product_create, name='product_create'),
    path('product/<int:pk>/edit/', product_update, name='product_update'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)