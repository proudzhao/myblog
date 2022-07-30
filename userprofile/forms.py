# -*- coding: utf-8 -*-
# @Time : 2022/7/30 13:19
# @Author : proudzhao
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
