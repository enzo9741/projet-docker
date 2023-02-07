from django import forms


class DriveForm(forms.Form):
    capacity = forms.CharField()
    read_value = forms.CharField()
    write_value = forms.CharField()

    capacity.widget.attrs.update({'class': 'form-control'})
    read_value.widget.attrs.update({'class': 'form-control'})
    write_value.widget.attrs.update({'class': 'form-control'})
