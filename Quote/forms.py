from django import forms
from .models import Quote, Item, Terms


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        exclude = ['total']


class ItemForm(forms.ModelForm):
    hiring_days = forms.IntegerField(required=False, label='Days')
    quantity = forms.IntegerField(label='QTY')
    unit_price = forms.FloatField(label='Price')

    class Meta:
        model = Item
        exclude = ['quote']


class TermsForm(forms.ModelForm):
    terms = forms.CharField(initial=Terms.objects.get(id=1).terms, widget=forms.Textarea)

    class Meta:
        model = Terms
        fields = ['terms']
