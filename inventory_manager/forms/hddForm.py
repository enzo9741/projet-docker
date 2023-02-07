from django import forms


class HddForm(forms.Form):
    rotation_speed = forms.CharField(label='Rotation Speed')
    size = forms.CharField(label='Size')

    rotation_speed.widget.attrs.update({'class': 'form-control'})
    size.widget.attrs.update({'class': 'form-control'})
