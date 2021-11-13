from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email_address', 'telephone_number',
                  'address_line1', 'address_line2', 'city_or_town',
                  'county_or_state', 'postcode_or_zip', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Adds a placeholder and class to remove auto generated
        labels and autofocuses on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email_address': 'Email Address',
            'telephone_number': 'Telephone Number',
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2',
            'city_or_town': 'City or Town',
            'county_or_state': 'County or State',
            'postcode_or_zip': 'Postcode or Zipcode',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
