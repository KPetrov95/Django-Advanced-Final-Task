from django.views.generic import ListView, FormView

from bookStore.catalog.forms import SearchForm
from bookStore.catalog.models import Book, Genre, Author


class BookListView(ListView, FormView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'books'
    paginate_by = 10
    form_class = SearchForm
    success_url = 'book_list'

    def get_queryset(self):
        queryset = Book.objects.all()

        book_title = self.request.GET.get('query')
        if book_title:
            queryset = queryset.filter(title__icontains=book_title)

        # Filtering
        genre = self.request.GET.get('genre')
        author = self.request.GET.get('author')
        if genre:
            queryset = queryset.filter(genre__name=genre)  # Assuming genre is a ForeignKey to Genre model
        if author:
            queryset = queryset.filter(author__full_name=author)  # Assuming author is a ForeignKey to Author model

        # Ordering
        order_by = self.request.GET.get('order_by', 'title')  # Default ordering by title
        if order_by in ['title', 'price']:
            queryset = queryset.order_by(order_by)

        # Get the minimum and maximum price from the request parameters
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        # Apply price filtering if values are provided
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['authors'] = Author.objects.all()
        context['min_price'] = Book.objects.all().order_by('price').first().price
        context['max_price'] = Book.objects.all().order_by('price').last().price
        return context