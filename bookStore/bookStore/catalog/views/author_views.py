from django.views.generic import ListView, FormView

from bookStore.catalog.models import Author


class AuthorListView(ListView, FormView):
    model = Author
    template_name = 'catalog/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        author_name = self.request.GET.get('query')
        if author_name:
            queryset = self.queryset.filter(full_name__icontains=author_name)
        return queryset
