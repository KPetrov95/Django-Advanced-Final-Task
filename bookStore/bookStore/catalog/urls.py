from django.urls import path, include

from bookStore.catalog.views.author_views import AuthorListView, AuthorDetailsView, AuthorCreateView
from bookStore.catalog.views.books_views import BookListView, BookDetailsView, BookCreateView
from bookStore.catalog.views.genre_views import GenreListView, GenreDetailsView, GenreCreateView
from bookStore.common.views import home

urlpatterns = [
    path('authors/', include([
        path('', AuthorListView.as_view(), name='author_list'),
        path('<int:id>/', AuthorDetailsView.as_view(), name='author_details'),
        path('create/', AuthorCreateView.as_view(), name='author_create'),
    ])),
    path('books/', include([
        path('', BookListView.as_view(), name='book_list'),
        path('<int:id>/', BookDetailsView.as_view(), name='book_details'),
        path('create/', BookCreateView.as_view(), name='book_create'),
    ])),
    path('genres/', include([
        path('', GenreListView.as_view(), name='genre_list'),
        path('<int:id>/', GenreDetailsView.as_view(), name='genre_details'),
        path('create/', GenreCreateView.as_view(), name='genre_create'),
    ]))
]
