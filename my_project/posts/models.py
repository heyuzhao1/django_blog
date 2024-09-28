from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner= models.ImageField(default='fallback.png',blank=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.title
    # 在 Django 中，如果你没有显式地定义主键字段，Django 会自动为每个模型添加一个名为 id 的主键字段。因此，在你当前的 Post 模型中，虽然你没有明确定义主键，但 Django 已经为你自动生成了一个 id 字段。