from django.urls import path, include

from bookStore.catalog.views.author_views import AuthorListView, AuthorDetailsView, AuthorCreateView, AuthorEditView, \
    AuthorDeleteView
from bookStore.catalog.views.books_views import BookListView, BookDetailsView, BookCreateView, BookEditView, \
    BookDeleteView
from bookStore.catalog.views.genre_views import GenreListView, GenreDetailsView, GenreCreateView, GenreEditView, \
    GenreDeleteView
from bookStore.common.views import home

urlpatterns = [
    path('authors/', include([
        path('', AuthorListView.as_view(), name='author_list'),
        path('create/', AuthorCreateView.as_view(), name='author_create'),
        path('<int:id>/', include([
            path('', AuthorDetailsView.as_view(), name='author_details'),
            path('edit/', AuthorEditView.as_view(), name='author_edit'),
            path('delete/', AuthorDeleteView.as_view(), name='author_delete'),
        ])),
    ])),
    path('books/', include([
        path('', BookListView.as_view(), name='book_list'),
        path('create/', BookCreateView.as_view(), name='book_create'),
        path('<int:id>/', include([
            path('', BookDetailsView.as_view(), name='book_details'),
            path('edit/', BookEditView.as_view(), name='book_edit'),
            path('delete/', BookDeleteView.as_view(), name='book_delete'),
        ])),
    ])),
    path('genres/', include([
        path('', GenreListView.as_view(), name='genre_list'),
        path('create/', GenreCreateView.as_view(), name='genre_create'),
        path('<int:id>/', include([
            path('', GenreDetailsView.as_view(), name='genre_details'),
            path('edit/', GenreEditView.as_view(), name='genre_edit'),
            path('delete/', GenreDeleteView.as_view(), name='genre_delete'),
        ])),
    ]))
]
