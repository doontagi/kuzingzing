from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model): # 슈퍼클래스 models의 하위클래스 Model을 상속 받는다.
    description = models.CharField(max_length=50)
    what = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    area=models.ForeignKey(Area, related_name='posts',on_delete=models.CASCADE)
    like=models.IntegerField(max_length=100)
