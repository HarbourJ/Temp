#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/27 13:49
# @Author  : HarbourJ
# @TG      : https://t.me/HarbourToulu
# @File    : ksjsb_week.py
# @Description: kuaishou_api_sts.txt为你快手极速版ck存放文件，一行一个ck；
#               code为你的助力码（获取方式-保存二维码-微信二维码转链接机器人🤖-把短链放到浏览器访问转为长链-最后一组数字即为你的助力码）

import requests
import time
import random
import urllib3
urllib3.disable_warnings()


def generate_random_did(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'abcdef0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

def ksjsbFriendAssist(api_st, code):
    url = "https://nebula.kuaishou.com/rest/zt/encourage/assistance/friendAssist"
    payload = "{\"assistanceId\":\"" + code + "\"}"
    if 'did=' in api_st:
        headers = {
            'Host': 'nebula.kuaishou.com',
            'Origin': 'https://nebula.kuaishou.com',
            'Content-Type': 'application/json',
            'Cookie': api_st,
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ksNebula/9.9.10.1646 ISLP/0 StatusHT/47 ISDM/0 TitleHT/44 NetType/WIFI ICFO/0 locale/zh-Hans CT/0 Yoda/2.6.8.4 ISLB/0 AZPREFIX/zw BHT/102 WebViewType/WK',
            'Content-Length': '35',
            'Referer': 'https://nebula.kuaishou.com/nebula/daily-invite',
            'Accept-Language': 'zh-cn'
        }
    else:
        headers = {
          'Host': 'nebula.kuaishou.com',
          'Origin': 'https://nebula.kuaishou.com',
          'Content-Type': 'application/json',
          'Cookie': 'kpn=NEBULA; kpf=ANDROID_PHONE; did=ANDROID_' + generate_random_did(16) + '; ver=9.10; appver=9.10.40.2474; language=zh-cn; countryCode=CN; sys=ANDROID_5.1; client_key=2ac2a76d; ' + api_st,
          'Accept-Encoding': 'gzip, deflate, br',
          'Connection': 'keep-alive',
          'Accept': '*/*',
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ksNebula/9.9.10.1646 ISLP/0 StatusHT/47 ISDM/0 TitleHT/44 NetType/WIFI ICFO/0 locale/zh-Hans CT/0 Yoda/2.6.8.4 ISLB/0 AZPREFIX/zw BHT/102 WebViewType/WK',
          'Content-Length': '35',
          'Referer': 'https://nebula.kuaishou.com/nebula/daily-invite',
          'Accept-Language': 'zh-cn'
        }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()
    print(response)
    print(response.get('msg'))

if __name__ == '__main__':

    code = "此处放你的周周赚助力码"
    
    api_stCK = []
    with open('kuaishou_api_sts.txt', 'r') as f:
        api_sts = f.readlines()
        for api_st in api_sts:
            api_st = api_st.replace('\n', '').split('@')
            for i in api_st:
                if len(i) >0:
                    api_stCK.append(i)
    print("共计%s个快手api_st" % len(api_stCK))
    j = 0
    for api_st in api_stCK:
        j += 1
        print(j, "-"*100)
        time.sleep(0.8)
        ksjsbFriendAssist(api_st, code)