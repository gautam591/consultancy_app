from django.contrib import admin
from .models import seminar
# Register your models here.
class seminarViewAdmin(admin.ModelAdmin):
    list_display = ('university', 'link','description')
    list_filter = ("awardId",'user',"count")
    search_fields = ['awardId', 'count','user']

admin.site.register(seminar)