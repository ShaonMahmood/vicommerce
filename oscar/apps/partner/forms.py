from django import forms

from oscar.apps.partner.models import ProviderModel


class MyForm(forms.ModelForm):

    class Meta:
        model = ProviderModel
        fields = ['product_quantity', 'message', 'attachment', 'email']