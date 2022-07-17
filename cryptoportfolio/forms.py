from django import forms
from cryptoportfolio.models import Crypto, models 


class CryptoForm(forms.ModelForm):  
    class Meta:  
        model = Crypto 
        fields = "__all__"  