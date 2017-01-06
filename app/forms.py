from django import forms
from .models import Gratitude

class EntryForm(forms.ModelForm):

    class Meta:
        model = Gratitude
        fields = ('text',)

    class Meta:
        model = Gratitude
        fields = ('text',)

    class Meta:
        model = Gratitude
        fields = ('text',)
