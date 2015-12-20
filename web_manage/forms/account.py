#!/usr/bin/env python
# -*-coding: utf-8 -*-
# __author__ = 'Richie'
from django import forms
from web_models import models


class LoginForm(forms.ModelForm):

    class Meta:
        model = models.AdminInfo
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class':"form-control", "placeholder": "用户名", "type":"text"}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'密码'}),
        }