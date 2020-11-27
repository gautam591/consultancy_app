from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from axisPosts.models import Post, apply,booking


class uploadPostForm(forms.ModelForm):
    postTitle = forms.CharField(label='postTitle',required=True,
                                help_text='Title of this Post',
                                widget=forms.TextInput(attrs={'placeholder': 'University Name','class':'newPostTitle'}))

    content = forms.CharField(label='content',required=True,
                                help_text='Description of the Post',
                                widget=forms.Textarea(attrs={'placeholder': 'Write Your Post Here ...','class':'newPostContent'}))

    country = forms.CharField(label='country',required=True,
                                help_text='Title of this university',
                                widget=forms.TextInput(attrs={'placeholder': 'country','class':'country'}))   
    postImage = forms.ImageField(label="postImagae", required=False,help_text="Upload Images for Post")
    

    class Meta:
        model = Post
        fields = ["postTitle","content","postImage","country"]


class  applyForm(forms.ModelForm):
    firstName = forms.CharField(label='firstname', required=True,
                             help_text='yourname', 
                             widget=forms.TextInput(attrs={'placeholder':'fname','class':'firstname'}))
    lastName = forms.CharField(label='lastname', required=True ,
                             help_text=' your lastname',
                             widget=forms.TextInput(attrs={'placeholder':'lname', 'class':'lastname'}))

    emailId = forms.EmailField(label='email',required=True,
                            help_text='your email address',
                            widget= forms.TextInput(attrs={'placeholder':'abcd@gamil.com','class':'email'}))
    
    mobile = forms.IntegerField(label='mobile',required=True,
                            help_text='your email address',
                            widget=forms.IntegerField())
    
    gendertype = [('0', 'select'),('1', 'male'),('2', 'female'),('3', 'others')]   
    gender = forms.ChoiceField (label='gender',required=True,
                                widget=forms.Select(attrs={'title': 'gender','class':'gender'}),choices=gendertype)   
    
    dob = forms.DateField(label='dob',required=True,
                            help_text='yourdob',
                            widget=forms.TextInput(attrs={'placeholder':'dob','class':'dob'}))
                     
    
    address = forms.CharField(label='address',required=True,
                            help_text='your address',
                            widget=forms.TextInput(attrs={'placeholder':'','class':'address'}))

    selecthobbies = [('0', 'select'),('1', 'drawing'),('2', 'signing'),('3', 'dancing')]   
    hobby = forms.MultipleChoiceField (label='hobby',required=False,
                                widget=forms.Select(attrs={'title': 'hobby','class':'hobby'}),choices=selecthobbies)

    yourqualification = [('0', 'select'),('1', 'high school '),('2', 'higherschool'),('3', 'bacelors'),('4', 'masters')]   
    qualifications = forms.MultipleChoiceField (label='qualifications',required=False,
                                widget=forms.Select(attrs={'title': 'qualifations','class':'qualifications'}),choices=yourqualification)


    appliedfor = [('0', 'select'),('1', 'computer science'),('2', 'MBA'),('3', 'BBA')]   
    subject = forms.ChoiceField (label='subject',required=True,
                              widget=forms.Select(attrs={'title': 'subject','class':'subject'}),choices=appliedfor) 


class Meta:
        model = apply
        fields = ["firstName","lastName","email","mobile","gender","dob","address","hobby","qualifications","subject"]


class bookingForm(forms.ModelForm):

    firstName = forms.CharField(label='firstname', required=True,
                             help_text='yourname', 
                             widget=forms.TextInput(attrs={'placeholder':'fname','class':'firstname'}))
    lastName = forms.CharField(label='lastname', required=True ,
                             help_text=' your lastname',
                             widget=forms.TextInput(attrs={'placeholder':'lname', 'class':'lastname'}))

    emailId = forms.EmailField(label='email',required=True,
                            help_text='your email address',
                            widget= forms.TextInput(attrs={'placeholder':'abcd@gamil.com','class':'email'}))
    
    mobile = forms.IntegerField(label='mobile',required=True,
                            help_text='your email address',
                            widget=forms.IntegerField())
    
    gendertype = [('0', 'select'),('1', 'male'),('2', 'female'),('3', 'others')]   
    gender = forms.ChoiceField (label='gender',required=True,
                                widget=forms.Select(attrs={'title': 'gender','class':'gender'}),choices=gendertype)   
    
    startdate = forms.DateField(label='startdate',required=True,
                            help_text='your estimated start date',
                            widget=forms.TextInput(attrs={'placeholder':'start date','class':'startDate'}))
                     
    

    selectclasses = [('0', 'ielts'),('1', 'Toefl'),('2', 'sat'),('3', 'gre')]   
    selectclass = forms.ChoiceField (label='selectclass',required=True,
                                widget=forms.Select(attrs={'title': 'class','class':'class'}),choices=selectclasses)

    selectshift = [('0', 'morning'),('1', 'afternoon'),('2', 'evening')]   
    shift = forms.ChoiceField (label='shift',required=True,
                                widget=forms.Select(attrs={'title': 'shift','class':'shift'}),choices=selectclasses)

    Recipt = forms.ImageField(label="recipt", required=True,help_text="Upload Images of yourpayment")

class Meta:
        model = booking
        fields = ["firstName","lastName","email","mobile","gender","startdate","selectclass","selectshift","recipt"]


