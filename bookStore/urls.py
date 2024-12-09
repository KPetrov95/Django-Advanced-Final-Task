
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookStore.common.urls')),
    path('catalog/', include('bookStore.catalog.urls')),
    path('accounts/', include('bookStore.accounts.urls')),
    path('orders/', include('bookStore.orders.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

]
