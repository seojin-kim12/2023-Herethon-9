from django.contrib import admin
from .models import *
# Register your models here.

# Photo 클래스를 inline으로 나타냄

class PhotoInline(admin.TabularInline):
    model=Photo

class GuardianInfoInline(admin.TabularInline):
    model=GuardianInfo

# UserInfo 클래스는 해당하는 Photo 객체를 리스트로 관리함
# UserInfo 테이블 안에 Photo가 들어가게 하기 위함
class UserInfoAdmin(admin.ModelAdmin):
    inlines=[PhotoInline, ]
    inlines=[GuardianInfoInline, ]


admin.site.register(UserInfo, UserInfoAdmin)