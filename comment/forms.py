# -*- coding: utf-8 -*-
# @Time : 2022/8/1 14:13
# @Author : proudzhao
from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
