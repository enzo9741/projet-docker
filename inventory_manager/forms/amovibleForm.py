from django import forms


class AmovibleForm(forms.Form):
    capacity = forms.CharField()
    tech = forms.CharField()

    capacity.widget.attrs.update({'class': 'form-control'})
    tech.widget.attrs.update({'class': 'form-control'})
