from django.shortcuts import render, redirect
from .models import *


# Create your views here.

# info create 함수
def info(request):
    if request.method == 'POST':
        # 사용자 정보 저장
        userInfo = UserInfo()   
        userInfo.name = request.POST.get('name_box')
        userInfo.residenceNumberStart = request.POST.get('residenceNumberStart')
        userInfo.residenceNumberEnd = request.POST.get('residenceNumberEnd')
        userInfo.height = request.POST.get('height_box')
        userInfo.weight = request.POST.get('weight_box')
        userInfo.tooth = request.POST.get('tooth_option')
        userInfo.hair = request.POST.get('hair_option')
        userInfo.blood = request.POST.get('blood_option')
        userInfo.scar = request.POST.get('scar_option')
        userInfo.feature = request.POST.get('feature_box')

        userInfo.save()

        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Img()
            # 외래키로 현재 생성한 UserInfo의 기본키를 참조한다.
            photo.userinfo = userinfo
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()

        # 보호자 정보 저장
        guarInfo = GuardianInfo()
        guarInfo.user_guard = userInfo
      
        guarInfo.guard_name = request.POST.get('guard_name')
        guarInfo.guard_residenceNumberStart = request.POST.get('guard_residenceNumberStart')
        guarInfo.guard_residenceNumberEnd = request.POST.get('guard_residenceNumberEnd')
        guarInfo.phoneNumber = request.POST.get('guard_phone')
        guarInfo.save()
        return redirect('info-list')    

    tooth_choices = UserInfo._meta.get_field('tooth').choices
    hair_choices = UserInfo._meta.get_field('hair').choices
    blood_choices = UserInfo._meta.get_field('blood').choices
    scar_choices = UserInfo._meta.get_field('scar').choices
    return render(request, "html/info_create.html", {'tooth_choices': tooth_choices,'hair_choices': hair_choices,'blood_choices': blood_choices,'scar_choices': scar_choices})

# info 작성 후 값 제시 함수

def userinfo(request):
    # 단일 객체 아니므로 objects.all 사용
    photo = Img.objects.all()   
    userinfo = UserInfo.objects.all()
    guardinfo = GuardianInfo.objects.all()
    
    tooth_choices = UserInfo._meta.get_field('tooth').choices
    hair_choices = UserInfo._meta.get_field('hair').choices
    blood_choices = UserInfo._meta.get_field('blood').choices
    scar_choices = UserInfo._meta.get_field('scar').choices

    context = {
        'userinfo': userinfo,
        'guardinfo': guardinfo,
        'tooth_choices': tooth_choices,
        'hair_choices': hair_choices,
        'blood_choices': blood_choices,
        'scar_choices': scar_choices,
        'photo' : photo
  
    }

    return render(request, "html/info.html", {'context': context})

