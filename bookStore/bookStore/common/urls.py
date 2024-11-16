from django.urls import path

from bookStore.common.views import home

urlpatterns = [
    path('', home, name='home')
]