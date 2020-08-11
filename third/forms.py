from django.forms import ModelForm
from third.models import Restaurant
from django.utils.translation import gettext_lazy as _

class RestaurantFrom(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']
        labels = {
            'name': _('Name:'),
            'address': _('Address:'),
        }

        help_texts = {
            'name': _('input your name.'),
            'address': _('input your address.'),
        }

        error_messages = {
            'name': {
                'max_length': _('Too long name. Type within 30 characters.')
            }
        }