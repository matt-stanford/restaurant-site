from django import forms
import datetime
from .models import Enquiry, Customer

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}), label='')
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject'}) , label='')
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}), label='')

class EnquiryForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'booking-modal-open'}), initial=datetime.date.today, label='')
    
    class Meta:
        model = Enquiry
        fields = '__all__'

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'