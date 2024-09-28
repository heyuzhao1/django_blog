from django.db import models
from django.contrib.auth.models import User

# 创建用户资料模型
class UserProfile(models.Model):
    # 一对一关系，表示每个UserProfile对应一个User
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 如果User被删除，则对应的UserProfile也会被删除

    # 头像字段，使用ImageField来存储用户的头像图片
    avatar = models.ImageField(default='fallback.png',blank=True) 
  

    # 简介字段，使用TextField来存储用户的个人简介
    bio = models.TextField(blank=True, null=True)  # 可以为空，允许用户提供个人简介

    # 性别字段，使用CharField来存储用户的性别，选择范围为'男'、'女'和'其他'
    gender = models.CharField(max_length=10, choices=[  # 定义性别选项
        ('male', '男'),  # 男性选项
        ('female', '女'),  # 女性选项
        ('other', '其他'),  # 其他性别选项
    ], blank=True, null=True)  # 可以为空，用户可选择不提供性别信息

    # 返回用户的字符串表示，通常是用户的用户名
    def __str__(self):
        return self.user.username  # 返回与该用户关联的用户名
