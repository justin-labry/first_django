from django.forms import ModelForm
from django import forms
from third.models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1',1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'Point': _('Point:'),
            'Comment': _('Comment:'),
        }

        help_texts = {
            'Point': _('Input point.'),
            'Comment': _('input your comments.'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)
        }

class RestaurantFrom(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'image', 'password']
        labels = {
            'name': _('Name:'),
            'address': _('Address:'),
            'image': _('imge url'),
            'password': _('article password:'),
        }

        help_texts = {
            'name': _('input your name.'),
            'address': _('input your address.'),
            'image': _('input your image url:'),
            'password': _('input your article password:'),
        }

        widgets = {
            'password': forms.PasswordInput(),
        }

        error_messages = {
            'name': {
                'max_length': _('Too long name. Type within 30 characters.')
            },
            'image': {
                'max_length': _('Too long url. Type within 500 characters.')
            },
            'password': {
                'max_length': _('Too long password. Type within 20 characters.')
            },
        }

class UpdateRestaurantForm(RestaurantFrom):
    class Meta:
        model = Restaurant
        exclude = ['password']
