from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Adds a placeholder and class to remove auto generated
        labels and autofocuses on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_telephone_number': 'Telephone Number',
            'default_address_line1': 'Address Line 1',
            'default_address_line2': 'Address Line 2',
            'default_city_or_town': 'City or Town',
            'default_county_or_state': 'County or State',
            'default_postcode_or_zip': 'Postcode or Zipcode',
            'default_country': 'Country',
        }

        self.fields['default_address_line1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-inputs'
            self.fields[field].label = False
