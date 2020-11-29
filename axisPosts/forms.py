from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from axisPosts.models import Post, apply,booking,gender,hobby,qualification,subject


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

YEARS= [x for x in range(1940,2021)]

class  applyForm(forms.ModelForm): 
    firstName = forms.CharField(label='firstName', required=True,
                             help_text='yourname', 
                             widget=forms.TextInput(attrs={'placeholder':'firstname','class':'firstname'}))
    lastName = forms.CharField(label='lastName', required=True ,
                             help_text=' your lastname',
                             widget=forms.TextInput(attrs={'placeholder':'lastname', 'class':'lastname'}))
     
    university = forms.CharField(label='selected university', required=True ,
                             help_text=' your lastname',
                             widget=forms.TextInput(attrs={'placeholder':'selected university', 'class':'lastname'}))
    email = forms.EmailField(label='email',required=True,
                            help_text='your email address',
                            widget= forms.TextInput(attrs={'placeholder':'abcd@gamil.com','class':'email'}))
    
    mobile = forms.CharField(label='mobile',required=True,
                            help_text='your email address',
                            widget=forms.TextInput(attrs={'placeholder':'phonenumber'}))
    
     
    gender = forms.ChoiceField (label='gender',required=True,
                                widget=forms.Select(attrs={'title': 'gender','class':'gender'}),choices=gender)   
    
    
    dob = forms.DateField(label='dob',required=True,
                                widget=forms.SelectDateWidget(years=YEARS))                 
    
    address = forms.CharField(label='address',required=True,
                            help_text='your address',
                            widget=forms.TextInput(attrs={'placeholder':'','class':'address'}))

      
    hobby = forms.ChoiceField (label='hobby',required=False,
                                widget=forms.Select(attrs={'title': 'hobby','class':'hobby'}),choices=hobby)

      
    qualifications = forms.ChoiceField (label='qualifications',required=False,
                                widget=forms.Select(attrs={'title': 'qualifations','class':'qualifications'}),choices=qualification)
# 

 
    subject = forms.ChoiceField (label='subject',required=True,
                              widget=forms.Select(attrs={'title': 'subject','class':'subject'}),choices=subject) 


    class Meta:
        model = apply
        fields = ["firstName","lastName", "university","email","mobile","gender","dob","address","hobby","qualifications","subject"]

YEARS= [x for x in range(1940,2021)]
class bookingForm(forms.ModelForm):

    firstName = forms.CharField(label='firstname', required=True,
                             help_text='yourname', 
                             widget=forms.TextInput(attrs={'placeholder':'fname','class':'firstname'}))
    lastName = forms.CharField(label='lastname', required=True ,
                             help_text=' your lastname',
                             widget=forms.TextInput(attrs={'placeholder':'lname', 'class':'lastname'}))

    email = forms.EmailField(label='email',required=True,
                            help_text='your email address',
                            widget= forms.TextInput(attrs={'placeholder':'abcd@gamil.com','class':'email'}))
    
    mobile = forms.IntegerField(label='mobile',required=True,
                            help_text='your email address',
                            widget=forms.NumberInput(attrs={'placeholder':'phone no','class':'pno'}))
    
    gendertype = [('0', 'select'),('1', 'male'),('2', 'female'),('3', 'others')]   
    gender = forms.ChoiceField (label='gender',required=True,
                                widget=forms.Select(attrs={'title': 'gender','class':'gender'}),choices=gendertype)   
    
    startdate = forms.DateField(label='startDate',required=False,
                                widget=forms.SelectDateWidget(years=YEARS))
                     
    

    selectclasses = [('0', 'ielts'),('1', 'Toefl'),('2', 'sat'),('3', 'gre')]   
    selectclass = forms.ChoiceField (label='selectclass',required=True,
                                widget=forms.Select(attrs={'title': 'class','class':'class'}),choices=selectclasses)

    selectshift = [('0', 'morning'),('1', 'afternoon'),('2', 'evening')]   
    shift = forms.ChoiceField (label='shift',required=True,
                                widget=forms.Select(attrs={'title': 'shift','class':'shift'}),choices=selectshift)

    paymentmethod = [('0', 'paypal'),('1', 'skrill'),('2', 'e-sewa')]   
    payment = forms.ChoiceField (label='pm',required=True,
                                widget=forms.Select(attrs={'title': 'pay','class':'pay'}),choices=paymentmethod)

    recipt = forms.ImageField(label="recipt", required=True,help_text="Upload Images of yourpayment")

    class Meta: # 
        model = booking
        fields = ["firstName","lastName","email","mobile","gender","startdate","selectclass","shift","payment","recipt"]


