# -*- coding:utf-8 -*-
from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=4)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]


class UpdateInfoForm(forms.Form):
    nick_name = forms.CharField(required=True, min_length=4)
    birthday = forms.DateField(required=True)
    mobile = forms.CharField(required=True, min_length=11, max_length=11, error_messages={"invalid": u"手机号码错误"})