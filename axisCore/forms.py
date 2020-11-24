
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from axisCore.models import seminar


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