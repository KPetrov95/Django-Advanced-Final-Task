from django.urls import path

from bookStore.catalog.views.author_views import AuthorListView
from bookStore.catalog.views.books_views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
]