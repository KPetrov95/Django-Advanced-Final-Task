from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from bookStore.accounts.models import UserProfile
from bookStore.catalog.models import Book
from bookStore.common.serializers import ReviewSerializer


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


class BookReviewsAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, book_id):
        book = Book.objects.filter(id=book_id).first()
        if not book:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        reviews = book.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, book_id):
        book = Book.objects.filter(id=book_id).first()
        if not book:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddToCartView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow both authenticated and unauthenticated users

    def post(self, request, book_id):

        book = get_object_or_404(Book, id=book_id)

        cart = request.session.get('cart', {})

        # Add or update the item in the cart
        if str(book_id) in cart:
            cart[str(book_id)]['quantity'] += 1
        else:
            cart[str(book_id)] = \
                {'title': book.title,
                 'price': float(book.price),
                 'quantity': 1
                 }

        # Save cart back to session
        request.session['cart'] = cart
        request.session.modified = True

        return Response({'message': 'Book added to cart', 'cart': cart})

class CartListView(TemplateView):
    template_name = 'common/cart-list-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        book_ids = cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        cart_items = []
        for book in books:
            str_book_id = str(book.id)
            cart_items.append({
                'book': book,
                'quantity': cart[str_book_id]['quantity'],
            })

        total = sum(item['book'].price * item['quantity'] for item in cart_items)

        context['total'] = total
        context['cart_items'] = cart_items
        return context

class ReduceCartQuantityView(APIView):
    def post(self, request, book_id):
        cart = request.session.get('cart', {})

        if str(book_id) in cart:
            cart[str(book_id)]['quantity'] -= 1
            if cart[str(book_id)]['quantity'] <= 0:
                del cart[str(book_id)]
            request.session['cart'] = cart
            request.session.modified = True
            return Response({'success': True, 'quantity': cart.get(str(book_id), {}).get('quantity', 0)})
        return Response({'success': False, 'message': 'Book not in cart'}, status=400)

class RemoveCartItemView(APIView):
    def post(self, request, book_id):
        cart = request.session.get('cart', {})

        if str(book_id) in cart:
            del cart[str(book_id)]
            request.session['cart'] = cart
            request.session.modified = True
            return Response({'success': True})
        return Response({'success': False, 'message': 'Book not in cart'}, status=400)
