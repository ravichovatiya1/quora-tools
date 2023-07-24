from django import forms
from auth_app import validators
from django.core.exceptions import ValidationError
from auth_app.models import User


class SignUpForm(forms.ModelForm):
    '''
        common signU=up form for all the users
    '''
    half = ['last_name', 'first_name']
    
    first_name = forms.CharField(
        max_length=50,
        min_length=1,
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    last_name = forms.CharField(
        max_length=50,
        min_length=1,
        label="Last Name",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    confirm_password = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password",
        validators=[validators.password_validator],
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 
                  'email', 'password', 'confirm_password')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            self.add_error('confirm_password', "Passwords don't match.")
            raise ValidationError("Passwords don't match.")
        


class SigninForm(forms.Form):
    '''
        common signin form,
    '''
    email = forms.EmailField(
        max_length=60,
        required = True,
        widget= forms.TextInput(),
        label= "Email",
    )

    password = forms.CharField(
        required = True,
        widget= forms.PasswordInput(),
        label = "Password",
        validators = [validators.password_validator,],
    )

    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

