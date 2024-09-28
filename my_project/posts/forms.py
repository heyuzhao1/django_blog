from django import forms 
from . import models 

class CreatePost(forms.ModelForm): 
    class Meta: 
        model = models.Post
        fields = ['title','body','slug','banner']
        #这里是模型表单，自动基于模型的定义创建表单