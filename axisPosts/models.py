from django.db import models
#from django.utils.text import slugify
from axisUsers.models import User
from autoslug import AutoSlugField
import datetime
#import re

# Create your models here.
class Post(models.Model):
    postTitle = models.CharField(max_length=200,unique=False)
    content = models.TextField()
    postImage = models.ImageField(upload_to="images/",null=True, blank=True)
    country= models.CharField(max_length=45) #Post Category:Regular/Complaint/Concern/Movement/Awareness
    updatedOn = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-postTitle']
    def __str__(self):
        return self.postTitle

class apply(models.Model):
    firstName = models.CharField(max_length=20,default=0)
    lastName = models.CharField(max_length=20,default=0)
    email  = models.EmailField(max_length=50,default=0)
    mobile = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,default=0)
    dob = models.DateField(default=0)
    address = models.CharField(max_length=50,null=False,default=0)
    hobby = models.CharField(max_length=10,default=0)
    qualifications = models.CharField(max_length=10,default=0)
    subject = models.CharField(max_length=10,default=0)
    applypopularity = models.IntegerField(default=0)

    class Meta:
        ordering = ['-applypopularity']
    def __str__(self):
        return self.firstName

class booking(models.Model):
    firstname=  models.CharField(max_length=10,default=0)
    lastName =  models.CharField(max_length=10,default=0)
    email  = models.EmailField(max_length=50,default=0)
    mobile = models.IntegerField(default=0)
    gender =  models.CharField(max_length=10,default=0)
    startdate = models.DateField(blank=True,null=True)
    selectclass =  models.CharField(max_length=10,default=0)
    bookingpopularity = models.IntegerField(default=0)
    shift =  models.CharField(max_length=10,default=0)
    payment = models.CharField(max_length=10,default=0)
    recipt = models.ImageField(upload_to="images/",null=True, blank=True)

    class Meta:
        ordering = ['-bookingpopularity']
    def __str__(self):
        return self.firstname





class postComments(models.Model):
    postId =  models.ForeignKey(Post,on_delete= models.CASCADE)
    active = models.BooleanField(default=True)
    parentId = models.ForeignKey('self',related_name='replies',on_delete= models.SET_NULL,null=True, blank=True)
    commentAuthor = models.ForeignKey(User,on_delete= models.SET_DEFAULT,default="1")
    comment = models.TextField()
    popularity = models.IntegerField(default=0)
    updatedOn = models.DateTimeField(auto_now=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-popularity']

class postReactions(models.Model):
    postId = models.ForeignKey(Post,on_delete= models.CASCADE)
    userName = models.ForeignKey(User,on_delete= models.CASCADE)
    reaction = models.IntegerField()

class commentReactions(models.Model):
    commentId = models.ForeignKey(postComments,on_delete=models.CASCADE)
    userName = models.ForeignKey(User,on_delete= models.CASCADE)
    reaction = models.IntegerField()

'''
def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value
'''