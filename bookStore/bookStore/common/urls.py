from django.urls import path

from bookStore.common.views import home, ToggleFavoriteView

urlpatterns = [
    path('', home, name='home'),
    path('api/<int:book_id>/toggle-favorite/', ToggleFavoriteView.as_view(), name='toggle_favorite')
]