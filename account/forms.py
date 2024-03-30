from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class MarketingForm(forms.ModelForm):
    class Meta:
        model = Marketing
        fields = '__all__'


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        exclude = ()