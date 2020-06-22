#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: smh
@contact: 809175193@qq.com
@software: PyCharm
@file: download_pic.py
@time: 2020/6/17 5:19 下午
"""

import requests
import re
import os
from common.project_path import *


def downloadPic(html, keyword):
    # 正则匹配需要查找的图片url
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    # print("输出找到的全部结果：", pic_url)
    i = 1
    print("关键词 {0} 的图片已找到{1}张，开始下载...".format(keyword, len(pic_url)))
    for each in pic_url:
        dir = pic_path + "/" + keyword + "_" + str(i) + ".jpg"
        i += 1
        pic_list = os.listdir(pic_path)
        # print("已有图片列表：{0}".format(pic_list))
        pic_name = os.path.basename(dir)

        # 去重
        if pic_name in pic_list:
            print("{0} 此图片已存在，不再下载！！！".format(pic_name))
            continue

        print("正在下载第{0}张图片，图片地址：{1}".format(str(i-1), each))
        try:
            pic = requests.get(each, timeout=10)
            pic.raise_for_status()
        except:
            print("图片下载失败！！！")
            continue

        fp = open(dir, "wb")
        fp.write(pic.content)
        fp.close()


if __name__ == '__main__':
    keyword = input("请输入搜索关键词：")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + keyword + '&ct=201326592&v=flip'
    html = requests.get(url)
    downloadPic(html.text, keyword)
