from django import forms


class RamForm(forms.Form):
    capacity = forms.CharField()
    type = forms.CharField()
    frequency = forms.CharField()

    capacity.widget.attrs.update({'class': 'form-control'})
    type.widget.attrs.update({'class': 'form-control'})
    frequency.widget.attrs.update({'class': 'form-control'})
