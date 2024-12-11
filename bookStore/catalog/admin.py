from django.contrib import admin
from django.db.models import Count

from bookStore.catalog.models import Book, Author, Genre


class AnnotatedModelAdmin(admin.ModelAdmin):
    related_field = None  # Override this in child classes
    annotated_field_name = None  # Override this in child classes

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(total_books_count=Count('books')).order_by('-total_books_count')

    def total_books_count(self, obj):
        return obj.total_books_count

    total_books_count.admin_order_field = 'total_books_count'
    total_books_count.short_description = 'Total Books'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'price', 'isbn']
    list_filter = ('author', 'genre', 'price')
    ordering = ['price', 'title', 'author', ]
    search_fields = ('title', 'author', 'genre')

class BookInline(admin.TabularInline):
    model = Book
    fields = ('title',)
    extra = 0




@admin.register(Author)
class AuthorAdmin(AnnotatedModelAdmin):
    inlines = [BookInline]
    list_display = ('first_name', 'last_name', 'total_books')
    related_field = 'books'
    annotated_field_name = 'total_books_count'

    def get_queryset(self, request):
        # Dynamically annotate total_books and order by it
        queryset = super().get_queryset(request)
        return queryset.annotate(total_books_count=Count('books')).order_by('-total_books_count')

    def total_books_count(self, obj):
        return obj.total_books_count

    total_books_count.admin_order_field = 'total_books_count'
    total_books_count.short_description = 'Total Books'


@admin.register(Genre)
class GenreAdmin(AnnotatedModelAdmin):
    inlines = [BookInline]
    list_display = ['name', 'total_books_count',]
    related_field = 'books'
    annotated_field_name = 'total_books_count'

    def total_books_count(self, obj):
        return obj.total_books_count

    total_books_count.admin_order_field = 'total_books_count'
    total_books_count.short_description = 'Total Books'