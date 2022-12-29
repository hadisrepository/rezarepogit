from asyncio.windows_events import NULL
from django import forms


class AddToCartProductForm(forms.Form):
     
    QUANTITY_CHOISES=[(i, str(i)) for i in range(1, 30)]

    quantity= forms.TypedChoiceField(choices=QUANTITY_CHOISES, coerce=int)
