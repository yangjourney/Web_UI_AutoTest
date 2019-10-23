#-*- coding:utf-8 -*-

class CaseStepInfo(object):
    """description of class"""
    def __init__(self, num, describe, keyword, method, expression, value, rownum):
        self.num = num
        self.describe = describe
        self.keyword = keyword
        self.method = method
        self.expression = expression
        self.value = value
        self.rownum = rownum
