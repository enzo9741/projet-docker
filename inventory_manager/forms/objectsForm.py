from django import forms


class ObjectsForm(forms.Form):
    brand = forms.CharField()
    reference = forms.CharField()
    serial_number = forms.CharField()
    available = forms.BooleanField()

    brand.widget.attrs.update({'class': 'form-control'})
    reference.widget.attrs.update({'class': 'form-control'})
    serial_number.widget.attrs.update({'class': 'form-control'})
    available.widget.attrs.update({'class': 'form-check-input', 'checked': 'checked', 'value': '1'})
