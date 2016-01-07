#!/usr/bin/env python
# -*-coding: utf-8 -*-
# __author__ = 'Richie'

from web_models import models
from backend.response.base_response import BaseResponse

def check_valid(**kwargs):
    response = BaseResponse()
    try:
        result = models.AdminInfo.objects.get(**kwargs)
        response.status = True
        response.data = result

    except Exception, e:
        response.message = e
    return response