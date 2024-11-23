from django.urls import path

from bookStore.common.views import home, ToggleFavoriteView, FavoritesListView

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('favorites/', FavoritesListView.as_view(), name='favorites'),  # Favorites list
    path('api/favorites/<int:book_id>/toggle/', ToggleFavoriteView.as_view(), name='toggle_favorite'),  # Toggle favorite API
]