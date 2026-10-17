from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Emri")
    email = forms.EmailField(label="Email")
    message = forms.CharField(
        label="Mesazhi",
        widget=forms.Textarea(attrs={"rows": 5}),
    )
