from django import forms




class QueryForms(forms.Form):
    error_message = {
        "Input at least one title"
    }

    attribute = {
        'type': 'text',
        'placeholder': 'Search...',
    }

    query_book = forms.CharField(label='', required=True, max_length=200, widget=forms.TextInput(attrs=attribute))
