#!/usr/bin/env python
# -*-coding: utf-8 -*-
# __author__ = 'Richie'
import StringIO
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from backend.commons.check_code import create_validate_code
from web_manage.forms.account import LoginForm

def check_code(request):
    stream_obj = StringIO.StringIO()
    validate_code = create_validate_code()
    img = validate_code[0]
    img.save(stream_obj, 'GIF')
    request.session['CheckCode'] = validate_code[1]
    print stream_obj
    return HttpResponse(stream_obj.getvalue())