import requests
from user_agent import *
import random
import SignerPy
import os
import webbrowser

webbrowser.open("https://t.me/tols_python")

# ===================== ألوان =====================
BOLD   = '\033[1m'
RED    = '\033[1;91m'
GREEN  = '\033[1;92m'
YELLOW = '\033[1;93m'
CYAN   = '\033[1;96m'
PURPLE = '\033[1;95m'
WHITE  = '\033[1;97m'
RESET  = '\033[0m'

COLORS = [RED, GREEN, YELLOW, CYAN, PURPLE, WHITE]

# ===================== Logo =====================
logo = f"""
{PURPLE}{BOLD}
╭━━━┳━━━╮
┃╭━╮┃╭━╮┃
┃╰━╯┃╰━━╮
┃╭━━┻━━╮┃
┃┃╱╱┃╰━╯┃
╰╯╱╱╰━━━╯
@𝒗77𝒗6
{RESET}
"""

# ===================== Banner =====================
print(logo)
print(f"{CYAN}{BOLD}🔥 VIP ULTRA TIK CHECKER 🔥{RESET}")
print(f"{YELLOW}{BOLD}اهلا بك في الاداة | PS: متاح TikTok{RESET}\n")

# ===================== Inputs =====================
ID = input(f"{CYAN}{BOLD}ENTER YOUR ID => {RESET}")
token = input(f"{CYAN}{BOLD}ENTER YOUR TOKEN => {RESET}")
os.system('clear')

# إعادة طباعة الشعار والترحيب بعد clear
print(logo)
print(f"{CYAN}{BOLD}🔥 VIP ULTRA TIK CHECKER 🔥{RESET}")
print(f"{YELLOW}{BOLD}اهلا بك في الاداة | PS: متاح TikTok{RESET}\n")

# ===================== Counters =====================
good = 0
bad = 0
light = 0
total_checked = 0

# ===================== Function =====================
def s():
    global good, bad, light, total_checked
    while True:
        # توليد الإيميل
        email = "".join(
            random.choice('qwertyuiopasdfghjklzxcvbnm1234567890')
            for i in range(3)
        ) + "@yopmail.com"

        headers = {
            'user-agent': str(generate_user_agent()),
        }

        data = {
            'mix_mode': '1',
            'email': email,
            'aid': '1459',
            'is_sso': 'false',
            'account_sdk_source': 'web',
            'region': 'IQ',
            'language': 'ar',
            'locale': 'ar',
            'did': '7596755445672805895',
        }

        # إرسال الطلب
        response = requests.post(
            'https://web-sg.tiktok.com/passport/web/user/check_email_registered?multi_login=1&did=7596755445672805895',
            headers=headers,
            data=data,
        ).text

        total_checked += 1

        # تحديث العدادات
        if '"is_registered":1' in response:
            good += 1
            status = "GOOD"
            color = random.choice(COLORS)
        else:
            bad += 1
            status = "NOT"
            color = random.choice(COLORS)

        light = bad % 10

        # -------- SINGLE LINE FULL COLOR VIP ULTRA --------
        print(f"{BOLD}{color}GOD: {good} ~ NOT: {bad} ~ 🔅: {light} ~ STATUS: {status}{RESET}")

# ===================== RUN =====================
s()