from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from web.views import index, product_detail

app_name="web"

urlpatterns = [
    path("", index, name="index"),
    path('product/<int:pk>/', product_detail, name='product_detail'),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)