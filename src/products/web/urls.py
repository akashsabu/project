from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from web import views


app_name="web"

urlpatterns = [
    path("", views.index, name="index"),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)