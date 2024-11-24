from django.urls import path, include

from bookStore.common.views import home, ToggleFavoriteView, FavoritesListView, BookReviewsAPIView

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('favorites/', FavoritesListView.as_view(), name='favorites'),
    # path('api/favorites/<int:book_id>/toggle/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
    path('api/', include([
        path('favorites/<int:book_id>/toggle/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
        path('books/<int:book_id>/reviews/', BookReviewsAPIView.as_view(), name='book_reviews_api')
    ]))
]