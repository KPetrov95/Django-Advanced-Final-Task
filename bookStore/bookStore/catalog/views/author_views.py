from django.db.models import Count, Q
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView

from bookStore.catalog.forms import SearchForm, AuthorCreationForm
from bookStore.catalog.models import Author


class AuthorListView(ListView, FormView):
    model = Author
    template_name = 'catalog/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10
    form_class = SearchForm

    def get_queryset(self):
        queryset = Author.objects.filter(id__gt=1).order_by('id')

        author_name = self.request.GET.get('query')
        if author_name:
            queryset = queryset.filter(
                Q(first_name__icontains=author_name) | Q(last_name__icontains=author_name)
            )

        queryset = queryset.annotate(book_count=Count('books'))
        return queryset

class AuthorDetailsView(DetailView):
    model = Author
    template_name = 'catalog/author_details.html'
    pk_url_kwarg = 'id'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreationForm
    template_name = 'catalog/author_create.html'

    def get_success_url(self):
        return reverse_lazy('author_details', kwargs={'id': self.object.pk})