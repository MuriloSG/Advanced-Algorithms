from django import forms
from crispy_forms.helper import FormHelper


class ProductSearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'placeholder': 'Digite o nome do produto...',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.template_pack = 'tailwind'
        self.helper.form_show_labels = False
        
