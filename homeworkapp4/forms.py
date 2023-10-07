from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}))
    description = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Введите описание товара'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
    image = forms.ImageField()
