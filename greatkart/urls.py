from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import handler404


urlpatterns = [
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'greatkart.views.handler404'
