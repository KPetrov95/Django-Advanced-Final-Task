from django.db.models import F, Value
from django.db.models.functions import Concat
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView, DeleteView

from bookStore.catalog.forms import SearchForm, BookForm
from bookStore.catalog.models import Book, Genre, Author


class BookListView(ListView, FormView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'books'
    paginate_by = 8
    form_class = SearchForm
    success_url = 'book_list'

    def get_queryset(self):
        queryset = Book.objects.all()

        book_title = self.request.GET.get('query')
        if book_title:
            queryset = queryset.filter(title__icontains=book_title)

        genre = self.request.GET.get('genre')
        author = self.request.GET.get('author')
        if genre:
            queryset = queryset.filter(genre__name=genre)
        if author:
            queryset = queryset.annotate(
                full_name=Concat(F('author__first_name'), Value(' '), F('author__last_name'))
            ).filter(full_name__icontains=author)

        order_by = self.request.GET.get('order_by', 'title')
        if order_by in ['title', 'price']:
            queryset = queryset.order_by(order_by)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')


        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        context['genres'] = Genre.objects.all()
        context['authors'] = Author.objects.all()
        context['form'] = SearchForm(placeholder='Book Title...')
        if books:
            context['min_price'] = books.order_by('price').first().price
            context['max_price'] = books.order_by('price').last().price
        return context


class BookDetailsView(DetailView):
    model = Book
    template_name = 'catalog/book_details.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit_reviews'] = self.request.user.has_perm('catalog.change_bookreview')
        return context


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'catalog/book_create.html'  # Adjust this to your template path
    success_url = reverse_lazy('book_list')  # Adjust this to the correct URL name for your book list

    def form_valid(self, form):
        # Additional processing if needed
        return super().form_valid(form)


class BookEditView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'catalog/book-edit.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('book_details', kwargs={'id': self.object.id})


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'catalog/object-delete.html'
    success_url = reverse_lazy('book_list')
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'Book'
        context['object_name'] = str(self.object)
        return context