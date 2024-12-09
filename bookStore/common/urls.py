from django.urls import path, include

from bookStore.common.views import home, ToggleFavoriteView, FavoritesListView, BookReviewsAPIView, AddToCartView, \
    CartListView, ReduceCartQuantityView, RemoveCartItemView

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('favorites/', FavoritesListView.as_view(), name='favorites'),
    path('cart/', CartListView.as_view(), name='cart_list'),
    path('api/', include([
        path('favorites/<int:book_id>/toggle/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
        path('books/<int:book_id>/reviews/', BookReviewsAPIView.as_view(), name='book_reviews_api'),
        path('books/<int:book_id>/reviews/<int:review_id>/', BookReviewsAPIView.as_view(), name='book_review_detail'),
        path('cart/<int:book_id>/add/', AddToCartView.as_view(), name='add_to_cart'),
        path('cart/<int:book_id>/reduce/', ReduceCartQuantityView.as_view(), name='reduce_quantity'),
        path('cart/<int:book_id>/remove/', RemoveCartItemView.as_view(), name='remove_cart_item'),
    ]))
]