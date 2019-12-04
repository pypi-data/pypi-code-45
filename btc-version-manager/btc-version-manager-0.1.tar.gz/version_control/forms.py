from django import forms


class RangeForm(forms.Form):
    """
    Accepts datetime range for clean
    """

    datetime_input_formats = ['%Y-%m-%dT%H:%M']

    range_start = forms.DateTimeField(
        label='От',
        input_formats=datetime_input_formats,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'vcs-form-input'
            }
        )
    )
    range_end = forms.DateTimeField(
        label='По',
        input_formats=datetime_input_formats,
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'vcs-form-input'
            }
        )
    )
