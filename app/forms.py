from django import forms
from .models import Gratitude, Entry


class GratitudeForm(forms.ModelForm):

    class Meta:
        model = Gratitude
        fields = ('text', )


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('created_date', )
