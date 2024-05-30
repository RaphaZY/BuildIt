from django import forms
from django.forms import ModelForm
from myapp.models import *

class ProductForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = "__all__"
        labels = {
            "name": "Nome",
            "descript": "Descrição",
            "price": "Preço",
            "path": "Imagem",
            "stored":"Estoque",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
            'descript': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Preço do item",
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            ),
            'stored': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Itens no estoque",
                }
            )
        }


# class OrderForm(forms.ModelForm):
#     class Meta:

#         model = Order
#         fields = "__all__"
#         labels = {
#             "user": "Nome",
#             "request_date": "Descrição",
#         }
#         widgets = {
#             'name': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': "Id do Cliente",
#                 }
#             ),
#             'request_date': forms.DateInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': "Horário da Ordem",
#                 }
#             ),
                        
#         }

# class ItemOrderForm(forms.ModelForm):
#     class Meta:

#         model = ItemOrder
#         fields = "__all__"
#         labels = {
#             "order": "Número da Ordem",
#             "product": "Descrição",
#             "quantity": "Quantidade",
#         }
#         widgets = {
#             'order': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': "Id do Cliente",
#                 }
#             ),
#             'product': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': "Id do Produto",
#                 }
#             ),
#             'quantity': forms.DateInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': "Quantidade",
#                 }
#             ),
                        
#         }
    