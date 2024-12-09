from django import forms
from bookStore.catalog.models import Book, Genre, Author


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=10,
        widget=forms.TextInput()
    )
    def __init__(self, *args, **kwargs):
        placeholder = kwargs.pop('placeholder', 'Search...')  # Default placeholder
        super().__init__(*args, **kwargs)
        self.fields['query'].widget.attrs['placeholder'] = placeholder


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'author', 'price', 'description', 'isbn', 'cover', 'published_at']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
                'placeholder': 'Enter book title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
                'placeholder': 'Short description',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
                'placeholder': 'Enter price',
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
                'placeholder': 'Enter ISBN',
            }),
            'author': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
            }),
            'genre': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
            }),
            'cover': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
            }),
            'published_at': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
            }),
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
                'placeholder': 'Enter genre name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500 resize-none',
                'placeholder': 'Enter genre description',
                'rows': 4,
            }),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'biography', 'birth_date', 'photo']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
                'placeholder': 'Last Name',
            }),
            'biography': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500 resize-none',
                'placeholder': 'Author\'s Biography',
                'rows': 5,
            }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 '
                         'focus:ring-orange-500',
            }),
        }
