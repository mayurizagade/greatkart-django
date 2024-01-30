from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password         = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Enter Password', 'class' : 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm Password'}))
    class Meta:
        model  = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']   = 'Enter First Name'  # placeholder means text displayed hote thod blur madhe
        self.fields['last_name'].widget.attrs['placeholder']    = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder']        = 'Enter EmailAddress'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'   # form-control means blur krte ti jaga 
        # form-control is a CSS class commonly used in frameworks like Bootstrap to style form elements such as 
        #  input fields, select boxes, and textareas.

    # PASSWORD   
    def clean(self): # django madhe already define aahe pn mla maza pramane define krayche aahe 
        cleaned_data     = super(RegistrationForm, self).clean() # allow u to change the way u save
        password         = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password: # password & confirm_password madhe same pswrd nahi lihila tr error yeil
            raise forms.ValidationError('Password Does Not Match...!')


