
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from axisCore.models import seminar
from axisUsers.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

YEARS= [x for x in range(1940,2021)]
class seminarForm(forms.ModelForm):

    university= forms.CharField(label='university', required=True,
                             help_text='yourname', 
                             widget=forms.TextInput(attrs={'placeholder':'university name','class':'firstname'}))
    date = forms.DateField(label='startDate',required=False,
                                widget=forms.SelectDateWidget(years=YEARS))


    description=forms.CharField(label='description',required=True,
                            help_text='about semianr',
                            widget= forms.Textarea(attrs={'placeholder':'description','class':'des'}))
    
    link=forms.CharField(label='link',required=True,
                            help_text='meeting link',
                            widget=forms.TextInput(attrs={'placeholder':'meeting link', 'class':'link'}))

    class Meta:
        model = seminar
        fields = ["university","date","description","link"]


