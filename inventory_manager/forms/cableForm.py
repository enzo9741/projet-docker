from django import forms


class CableForm(forms.Form):
    length = forms.CharField()
    start_type = forms.CharField()
    end_type = forms.CharField()

    length.widget.attrs.update({'class': 'form-control'})
    start_type.widget.attrs.update({'class': 'form-control'})
    end_type.widget.attrs.update({'class': 'form-control'})
