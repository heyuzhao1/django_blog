from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CreateUser(UserCreationForm):  # 继承自UserCreationForm
    avatar = forms.ImageField(required=False)  # 头像为可选
    gender = forms.ChoiceField(choices=[
        ('male', '男'),
        ('female', '女'),
        ('other', '其他'),
    ], required=True)  # 性别为必填

    class Meta:
        model = User  # 使用Django的User模型
        fields = ['username', 'password1', 'password2']  # 只包含User模型的字段

    def save(self, commit=True):
        user = super().save(commit=commit)  # 保存User模型
        # 创建UserProfile实例
        #UserProfile.objects.create(user=user, avatar=self.cleaned_data['avatar'], gender=self.cleaned_data['gender'])
        # 创建UserProfile实例
        profile = UserProfile.objects.create(user=user)  # 创建UserProfile实例
        profile.avatar = self.cleaned_data['avatar']  # 设置头像
        profile.gender = self.cleaned_data['gender']  # 设置性别
        profile.save()  # 保存UserProfile实例
        return user
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'gender'] 