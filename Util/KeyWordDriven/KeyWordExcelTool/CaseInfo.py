#-*- coding:utf-8 -*-

class CaseInfo(object):
    """description of class"""
    def __init__(self, caseNum,caseName,caseDescribe,sheetName,rownum):
        self.caseNum = caseNum
        self.caseName = caseName
        self.caseDescribe = caseDescribe
        self.sheetName = sheetName
        self.rownum = rownum#行,int
