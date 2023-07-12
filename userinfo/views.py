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

        # name 속성이 img인 input 태그로부터 받은 파일들 반복문 통해 하나씩 가져옴
        for img in request.FILES.getlist('imgs'):
            # Photo 객체 생성
            photo = Photo()
            # 외래키 -  UserInfo 기본키 참조
            photo.userInfo = userInfo
            # imgs 로 가져온 이미지 파일 하나 저장
            photo.image = img
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
    
    context = {
        'tooth_choices': UserInfo._meta.get_field('tooth').choices,
        'hair_choices': UserInfo._meta.get_field('hair').choices,
        'blood_choices': UserInfo._meta.get_field('blood').choices,
        'scar_choices': UserInfo._meta.get_field('scar').choices
    }
    
    return render(request, "html/info_create.html", {'context':context})

# info 작성 후 값 제시 함수
def userinfo(request):
    # 단일 객체 아니므로 objects.all 사용
    userinfo = UserInfo.objects.all()
    photoinfo = Photo.objects.all()
    guardinfo = GuardianInfo.objects.all()

    context = {
        'userinfo' : userinfo, 
        'photoinfo' : photoinfo, 
        'guardinfo' : guardinfo
    }

    return render(request, "html/info.html", {'context': context})