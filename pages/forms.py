from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}), label='')
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject'}) , label='')
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}), label='')