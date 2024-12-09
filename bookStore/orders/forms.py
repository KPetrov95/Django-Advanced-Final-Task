from django import forms

class CheckoutForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="I confirm my order")


from django import forms

class DeliveryDetailsForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-500',
            'placeholder': 'Full Name',
        })
    )
    address = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-500 resize-none',
            'rows': 3,
            'placeholder': 'Delivery Address',
        })
    )
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-orange-500',
            'placeholder': 'Phone Number',
        })
    )
