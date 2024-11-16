from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from bookStore.catalog.forms import GenreCreationForm
from bookStore.catalog.models import Genre


class GenreListView(ListView):
    model = Genre
    template_name = 'catalog/genre-list.html'
    context_object_name = 'genres'

    def get_queryset(self):
        queryset = Genre.objects.filter(id__gt=1)
        return queryset


class GenreDetailsView(DetailView):
    model = Genre
    template_name = 'catalog/genre-details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = self.object.books.all()
        context['books'] = books
        return context

class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreCreationForm
    template_name = 'catalog/genre-create.html'
    success_url = reverse_lazy('genre_list')
