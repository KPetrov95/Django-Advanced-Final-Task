from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from ..catalog.models import Book
from .tasks import send_order_confirmation_email
from django.views.generic.edit import FormView
from .models import Order, OrderItem
from .forms import DeliveryDetailsForm, CheckoutForm


class CheckoutView(FormView):
    template_name = 'orders/checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            delivery_form = DeliveryDetailsForm(initial={
                'full_name': f"{profile.first_name} {profile.last_name}",
                'address': profile.address,
                'phone_number': profile.phone_number,
            })
        else:
            delivery_form = DeliveryDetailsForm()

        context['delivery_form'] = delivery_form

        cart = self.request.session.get('cart', {})
        book_ids = cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        cart_items = []
        total_price = 0
        for book in books:
            quantity = cart[str(book.id)]['quantity']
            total_price += book.price * quantity
            cart_items.append({'book': book, 'quantity': quantity})

        context['cart_items'] = cart_items
        context['total_price'] = total_price

        return context

    def form_valid(self, form):
        delivery_form = DeliveryDetailsForm(self.request.POST)
        if not delivery_form.is_valid():
            form.add_error(None, "Invalid delivery details!")
            return self.form_invalid(form)

        delivery_data = delivery_form.cleaned_data

        cart = self.request.session.get('cart', {})
        if not cart:
            form.add_error(None, "Your cart is empty!")
            return self.form_invalid(form)

        order = Order.objects.create(
            user=self.request.user,
            total_price=0,
            full_name=delivery_data['full_name'],
            address=delivery_data['address'],
            phone_number=delivery_data['phone_number'],
        )
        total_price = 0

        for book_id, item in cart.items():
            book = Book.objects.get(id=book_id)
            quantity = item['quantity']
            OrderItem.objects.create(order=order, book=book, quantity=quantity)
            total_price += book.price * quantity

        order.total_price = total_price
        order.save()
        self.request.session['cart'] = {}
        self.request.session.modified = True

        send_order_confirmation_email.delay(order.id, self.request.user.email)
        return super().form_valid(form)


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order-list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')


class OrderDetailsView(DetailView):
    model = Order
    template_name = 'orders/order-details.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
