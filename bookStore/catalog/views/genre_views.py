from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bookStore.catalog.forms import GenreForm
from bookStore.catalog.models import Genre


class GenreListView(ListView):
    model = Genre
    template_name = 'catalog/genre-list.html'
    context_object_name = 'genres'

    def get_queryset(self):
        queryset = Genre.objects.all()
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
    form_class = GenreForm
    template_name = 'catalog/genre-create.html'
    success_url = reverse_lazy('genre_list')


class GenreEditView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'catalog/genre-edit.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('genre_details', kwargs={'id': self.object.id})


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'catalog/object-delete.html'
    success_url = reverse_lazy('genre_list')
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'Genre'
        context['object_name'] = str(self.object)
        return context