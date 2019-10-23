#-*- coding:utf-8 -*-

import requests

# url = 'XXXXXXX'  # url:接口地址
# data = {'XXX': 'XXX'}                     #data:接口传递的参数
# headers = {'Connection': 'close'}  # header:传递header信息
# # files:接口中需要上传文件则需要用到该参数

def get(url,headers=None):
    response = requests.get(url,headers = headers)        #请求url，获得返回的数据信息
    # print('response.text = ' + str(response.text))
    # print('response.headers = ' + str(response.headers))
    # print('response.status_code = ' + str(response.status_code))
    return response

def post(url,data=None,headers=None):
    response = requests.post(url,data = data,headers = headers)        #请求url，获得返回的数据信息
    return response

# def post1():
#     response = requests.request("POST", url, data=payload, headers=headers)