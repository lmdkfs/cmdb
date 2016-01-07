#!/usr/bin/env python
# -*-coding: utf-8 -*-
# __author__ = 'Richie'

class BaseResponse(object):

    def __init__(self):
        self.status = False
        self.message = ''
        self.data = None