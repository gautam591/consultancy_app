from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from axisPosts.models import Post


class uploadPostForm(forms.ModelForm):
    postTitle = forms.CharField(label='postTitle',required=True,
                                help_text='Title of this Post',
                                widget=forms.TextInput(attrs={'placeholder': 'Title/Heading','class':'newPostTitle'}))

    content = forms.CharField(label='content',required=True,
                                help_text='Description of the Post',
                                widget=forms.Textarea(attrs={'placeholder': 'Write Your Post Here ...','class':'newPostContent'}))
    categoryChoices = [('0', 'choose'),('1', 'south korea'),('2', 'japan'),('3', 'canada'),('4', 'austrelia'),('5', 'usa')]
    country = forms.ChoiceField (label='category',required=False,
                                widget=forms.Select(attrs={'title': 'Post Category','class':'optionSelection'}),choices=categoryChoices)
   
    postImage = forms.ImageField(label="postImagae", required=False,help_text="Upload Images for Post")


    class Meta:
        model = Post
        fields = ["postTitle","content","postImage","country"]
