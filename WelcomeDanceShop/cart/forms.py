from django import forms

# При добавлении в корзину можно выбрать до 10 единиц товара:
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


# override нужно для прибавления единиц товара, если товар уже есть в корзине
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='Количество')
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

