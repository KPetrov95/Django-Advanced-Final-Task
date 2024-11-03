# # #slider price filter
# # #view file
# # def get_queryset(self):
# #     queryset = Book.objects.all()
# #
# #     # Get the minimum and maximum price from the request parameters
# #     min_price = self.request.GET.get('min_price')
# #     max_price = self.request.GET.get('max_price')
# #
# #     # Apply price filtering if values are provided
# #     if min_price:
# #         queryset = queryset.filter(price__gte=min_price)
# #     if max_price:
# #         queryset = queryset.filter(price__lte=max_price)
# #
# #     return queryset
# #
# #
# # def get_context_data(self, **kwargs):
# #     context = super().get_context_data(**kwargs)
# #     # Optionally, pass the min and max prices for the range slider
# #     context['min_price'] = Book.objects.all().order_by('price').first().price
# #     context['max_price'] = Book.objects.all().order_by('price').last().price
# #     return context
#
# #template
# <!-- book_list.html -->
# <form method="get">
#     <div>
#         <label for="min_price">Min Price:</label>
#         <input type="range" id="min_price" name="min_price" min="{{ min_price }}" max="{{ max_price }}" value="{{ request.GET.min_price|default:min_price }}" oninput="this.nextElementSibling.value = this.value">
#         <output>{{ request.GET.min_price|default:min_price }}</output>
#     </div>
#     <div>
#         <label for="max_price">Max Price:</label>
#         <input type="range" id="max_price" name="max_price" min="{{ min_price }}" max="{{ max_price }}" value="{{ request.GET.max_price|default:max_price }}" oninput="this.nextElementSibling.value = this.value">
#         <output>{{ request.GET.max_price|default:max_price }}</output>
#     </div>
#     <button type="submit">Apply Filter</button>
# </form>
#
# <!-- Display Books -->
# <ul>
#     {% for book in books %}
#         <li>{{ book.title }} - ${{ book.price }}</li>
#     {% endfor %}
# </ul>
