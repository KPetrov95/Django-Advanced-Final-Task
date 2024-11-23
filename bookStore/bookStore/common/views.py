from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from bookStore.accounts.models import UserProfile
from bookStore.catalog.models import Book


# Create your views here.
def home(request):
    return render(request, 'common/home-page.html')

class ToggleFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, book_id):
        book = Book.objects.filter(id=book_id).first()
        if not book:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        profile = request.user.profile

        if book in profile.favorite_books.all():
            profile.favorite_books.remove(book)
            return Response({'message': 'Book removed from favorites', 'favorite': False}, status=status.HTTP_200_OK)
        else:
            profile.favorite_books.add(book)  # Favorite
            return Response({'message': 'Book added to favorites', 'favorite': True}, status=status.HTTP_200_OK)



class FavoritesListView(LoginRequiredMixin, ListView):
    template_name = 'common/favorites-page.html'
    paginate_by = 5
    context_object_name = 'favorites'

    def get_queryset(self):
        return self.request.user.profile.favorite_books.all().order_by('title')