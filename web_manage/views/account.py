#!/usr/bin/env python
# -*-coding: utf-8 -*-
# __author__ = 'Richie'
import StringIO
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from backend.commons.check_code import create_validate_code
from web_manage.forms.account import LoginForm
from web_manage.bll import account_manager
import json


def check_code(request):
    stream_obj = StringIO.StringIO()
    validate_code = create_validate_code()
    img = validate_code[0]
    img.save(stream_obj, 'GIF')
    request.session['CheckCode'] = validate_code[1]
    print validate_code[1]
    return HttpResponse(stream_obj.getvalue())

def richie(request):
    print 'welcome'
    return  HttpResponse('hello Richie')



def login(request):
    error = ''
    login_form = LoginForm(request.POST)
    if request.method == 'POST':
        check = request.POST.get('checkcode', None)
        print check
        if check != request.session['CheckCode'].lower():
            error = '验证码错误'
        else:
            if not login_form.is_valid():
                error = '用户名或者密码格式错误'
            else:
                data = login_form.clean()
                result = account_manager.check_valid(**data)
                if result.status:
                    ret = {'id':result.data.user_info.id, 'name': result.data.user_info.name}
                    request.session['auth_user'] = json.dumps(ret)
                    target = request.GET.get('back', '/account/index.html')
                    return redirect(target)
                else:
                    error = '用户名或密码错误'
    print error
    return render_to_response('account/login.html', {'model': login_form,'error': error})