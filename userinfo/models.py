from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class ToothChoice(models.TextChoices):
    NORMAL = '정상'
    DENTURE = '틀니'
    WISDOM_TOOTH = '뻐드렁니'
    MOLAR = '금니'
    SILVER_TOOTH = '은니'
    DENTAL_BRIDGE = '의치'
    TARTAR_TOOTH = '때운이빨'
    IMPLANT = '임플란트'
    OTHER = '기타'

class HairChoice(models.TextChoices):
    UNDEFINED = '미기재'
    SHAVED = '삭발'
    BALD = '대머리'
    LONG_HAIR = '긴머리'
    CURLY_LONG_HAIR = '곱슬긴머리'
    SHORT_HAIR = '단발머리'
    CUT_HAIR = '커트머리'
    CURLY_SHORT_HAIR = '곱슬단발머리'
    WIG = '가발'
    SPORTY = '스포츠형'
    SHORT_NATURAL_HAIR = '짧은머리(생머리)'
    LONG_NATURAL_HAIR = '긴머리(생머리)'
    SHORT_PERMED_HAIR = '짧은머리(펌)'
    LONG_PERMED_HAIR = '긴머리(펌)'
    TIED_HAIR = '묶음머리'
    TOPKNOT = '상고머리'
    DYED_BLEACHED = '염색/탈색'
    BOWL_CUT = '바가지머리'
    OTHER = '기타'

class BloodChoice(models.TextChoices):
    UNDEFINED = '미기재'
    A_POSITIVE = 'A (RH+)'
    B_POSITIVE = 'B (RH+)'
    O_POSITIVE = 'O (RH+)'
    AB_POSITIVE = 'AB (RH+)'
    A_NEGATIVE = 'A (RH-)'
    B_NEGATIVE = 'B (RH-)'
    O_NEGATIVE = 'O (RH-)'
    AB_NEGATIVE = 'AB (RH-)'

class ScarChoice(models.TextChoices):
    UNDEFINED = '미기재'
    HEAD = '머리'
    FACE = '얼굴'
    ARM = '팔'
    HAND = '손'
    BACK = '등'
    TORSO = '몸통'
    BUTTOCK = '둔부'
    LEG = '다리'
    FOOT = '발'
    OTHER = '기타'

class UserInfo(models.Model):
    # Nickname - will import after user registration
    name = models.CharField(max_length=10, null=True)
    residenceNumberStart = models.PositiveIntegerField()
    residenceNumberEnd = models.PositiveIntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    tooth = models.CharField(max_length=100, choices=ToothChoice.choices)
    hair = models.CharField(max_length=100, choices=HairChoice.choices)
    blood = models.CharField(max_length=100, choices=BloodChoice.choices)
    scar = models.CharField(max_length=100, choices=ScarChoice.choices)
    feature = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name

# 이미지 여러장 업로드 - 일대다
class Photo(models.Model):
    userimg = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
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