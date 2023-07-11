from django.db import models
from django.utils import timezone
from enum import Enum

# 카테고리
class category(Enum):
    위험 = '대기'
    추행 = '취소'
    폭행 = '완료'
    침입 = '침입'

# 글 생성
class Post(models.Model):
    title = models.CharField(max_length=50)
  #  author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    body = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=[(status.value, status.name) for status in category])