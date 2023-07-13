from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from accounts.models import *

TOOTH_CHOICES = (
    ('정상','정상'),
    ('틀니', '틀니'),
    ('뻐드렁니', '뻐드렁니'),
    ('금니', '금니'),
    ('은니', '은니'),
    ('의치', '의치'),
    ('때운이빨','때운이빨'),
    ('임플란트','임플란트'),
    ('기타','기타')
)

HAIR_CHOICES = (
    ('미기재', '미기재'),
    ('삭발', '삭발'),
    ('대머리', '대머리'),
    ('긴머리', '긴머리'),
    ('곱슬긴머리', '곱슬긴머리'),
    ('단발머리', '단발머리'),
    ('커트머리', '커트머리'),
    ('곱슬단발머리', '곱슬단발머리'),
    ('가발', '가발'),
    ('스포츠형', '스포츠형'),
    ('짧은머리(생머리)', '짧은머리(생머리)'),
    ('긴머리(생머리)', '긴머리(생머리)'),
    ('짧은머리(펌)', '짧은머리(펌)'),
    ('긴머리(펌)', '긴머리(펌)'),
    ('묶음머리', '묶음머리'),
    ('상고머리', '상고머리'),
    ('염색/탈색', '염색/탈색'),
    ('바가지머리', '바가지머리'),
    ('기타', '기타'),
)

BLOOD_CHOICES = (
    ('미기재', '미기재'),
    ('A (RH+)', 'A (RH+)'),
    ('B (RH+)', 'B (RH+)'),
    ('O (RH+)', 'O (RH+)'),
    ('AB (RH+)', 'AB (RH+)'),
    ('A (RH-)', 'A (RH-)'),
    ('B (RH-)', 'B (RH-)'),
    ('O (RH-)', 'O (RH-)'),
    ('AB (RH-)', 'AB (RH-)'),
)

SCAR_CHOICES = (
    ('미기재', '미기재'),
    ('머리', '머리'),
    ('얼굴', '얼굴'),
    ('팔', '팔'),
    ('손', '손'),
    ('등', '등'),
    ('몸통', '몸통'),
    ('둔부', '둔부'),
    ('다리', '다리'),
    ('발', '발'),
    ('기타', '기타'),
)

class UserInfo(models.Model):
    # Nickname - will import after user registration
    name = models.CharField(max_length=10, null=True)
    residenceNumberStart = models.PositiveIntegerField()
    residenceNumberEnd = models.PositiveIntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    tooth = models.CharField(max_length=200, choices= TOOTH_CHOICES, null=True)
    hair = models.CharField(max_length=200, choices= HAIR_CHOICES, null=True)
    blood = models.CharField(max_length=200, choices= BLOOD_CHOICES, null=True)
    scar = models.CharField(max_length=200, choices= SCAR_CHOICES, null=True)
    feature = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Img(models.Model):
    info = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


# 보호자 정보 - 일대일
class GuardianInfo(models.Model):
    user_guard = models.OneToOneField(UserInfo, on_delete=models.CASCADE, primary_key=True)
    guard_name = models.CharField(max_length=10)
    guard_residenceNumberStart = models.PositiveIntegerField()
    guard_residenceNumberEnd = models.PositiveIntegerField()
    # 핸드폰번호 정규식 포맷
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, null=True)

    def __str__(self):
        return self.guard_name