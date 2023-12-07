from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from web.views import index

app_name="web"

urlpatterns = [
    path("", index, name="index")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)