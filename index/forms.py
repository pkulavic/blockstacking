from django import forms

class TotalOverhang(forms.Form):
    l = forms.IntegerField(label="Length of block (L):")
    n = forms.IntegerField(label="Number of blocks (n):")
