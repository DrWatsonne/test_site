from django import forms


class SendForm(forms.Form):
    u"""
    Main form for sending messages
    """
    email = forms.EmailField(label='Email', required=True)
    text = forms.CharField(label='Message', required=True, widget=forms.Textarea())
