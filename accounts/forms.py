from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class':'form-control',  
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class':'form-control',
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter First Name',
        'class':'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Last Name',
        'class':'form-control',
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email Address',
        'class':'form-control',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Phone Number',
        'class':'form-control',
    }))
    class Meta:
        model= Account
        fields = ['first_name','last_name','phone_number','email','password']

    def clean(self):
        clean_data = super(RegistrationForm,self).clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match!'
            )

'''
    def __ini__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
'''