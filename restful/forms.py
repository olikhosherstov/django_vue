from django import forms
from .models import *

PERIOD_CHOICES = (
    ("06:00 - 07:00", "06:00 - 07:00"),
    ("07:00 - 08:00", "07:00 - 08:00"),
    ("08:00 - 09:00", "08:00 - 09:00"),
    ("09:00 - 10:00", "09:00 - 10:00"),
    ("10:00 - 11:00", "10:00 - 11:00"),
    ("11:00 - 12:00", "11:00 - 12:00"),
    ("12:00 - 13:00", "12:00 - 13:00"),
    ("13:00 - 14:00", "13:00 - 14:00"),
    ("14:00 - 15:00", "14:00 - 15:00"),
    ("15:00 - 16:00", "15:00 - 16:00"),
    ("16:00 - 17:00", "16:00 - 17:00"),
    ("17:00 - 18:00", "17:00 - 18:00"),
    ("18:00 - 19:00", "18:00 - 19:00"),
    ("19:00 - 20:00", "19:00 - 20:00"),
    ("20:00 - 21:00", "20:00 - 21:00"),
    ("21:00 - 22:00", "21:00 - 22:00"),
)


class BookingAddForm(forms.Form):
    period = forms.ChoiceField(choices=PERIOD_CHOICES, label="Період, що бронюється")
    user = forms.ModelChoiceField(queryset=Profile.objects.all(), label="Користувач", empty_label="Користувач не вибраний")
