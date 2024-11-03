from django.db.models import Count, Q
from django.views.generic import ListView, FormView, DetailView

from bookStore.catalog.forms import SearchForm
from bookStore.catalog.models import Author


class AuthorListView(ListView, FormView):
    model = Author
    template_name = 'catalog/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10
    form_class = SearchForm

    def get_queryset(self):
        queryset = super().get_queryset()

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