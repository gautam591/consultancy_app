
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from axisCore.models import seminar
from axisUsers.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class seminarForm(forms.ModelForm):

    university= forms.CharField(label='university', required=True,
                             help_text='yourname', 
                             widget=forms.TextInput(attrs={'placeholder':'fname','class':'firstname'}))
    date= forms.DateTimeField(label='lastname', required=True ,
                             help_text=' your lastname',
                             widget=forms.TextInput(attrs={'placeholder':'lname', 'class':'lastname'}))

    description=forms.CharField(label='description',required=True,
                            help_text='about semianr',
                            widget= forms.Textarea(attrs={'placeholder':'description','class':'des'}))
    
    link=forms.CharField(label='link',required=True,
                            help_text='meeting link',
                            widget=forms.TextInput(attrs={'placeholder':'meeting link', 'class':'link'}))

class Meta:
        model = seminar
        fields = ["university","date","description","link"]


class passadmin(AuthenticationForm):
    username = forms.CharField(label='username',required=True,
                                help_text='Your Username for Axis',
                                widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password',max_length=32,min_length=6,required=True,
                                help_text='A Strong Password has Combination of Letters,Numbers and Characters',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ["username","password"]