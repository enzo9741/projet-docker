from django import forms


class CpuForm(forms.Form):
    core = forms.IntegerField()
    threads = forms.IntegerField()
    frequency = forms.CharField()

    core.widget.attrs.update({'class': 'form-control'})
    threads.widget.attrs.update({'class': 'form-control'})
    frequency.widget.attrs.update({'class': 'form-control'})
