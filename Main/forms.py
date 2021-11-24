from django import forms


class CategoryForm(forms.Form):
    Title = forms.CharField(widget=forms.Textarea)


