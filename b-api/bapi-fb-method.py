import string
import requests
import random
from uuid import uuid4
import hashlib
import json

def sortObj(data):
  sortedObj = {}
  sort = sorted(data)
  for item in sort:
    sortedObj[item] = data[item]
  return sortedObj

def getSig(data):
  signature = ""
  for item in data:
    signature += item + "=" + data[item]
  return encmd5(signature + "62f8ce9f74b12f84c123cc23437a4a32")

def encmd5(sig):
  result = hashlib.md5(sig.encode())
  return result.hexdigest()

def Get_Facebook_Access_Token(username, password): 

  adID = str(uuid4())
  did = str(uuid4())
  data = {
      'adid': adID,
      'format': 'json',
      'device_id': did,
      'email': username,
      'password': password,
      'cpl': 'true',
      'family_device_id': did,
      'credentials_type': 'device_based_login_password',
      'generate_session_cookies': '1',
      'error_detail_type': 'button_with_disabled',
      'source': 'device_based_login',
      'machine_id': ''.join(random.choices(string.ascii_lowercase + string.digits, k=24)),
      'meta_inf_fbmeta': '',
      'advertiser_id': adID,
      'currently_logged_in_userid': '0',
      'locale': 'en_US',
      'client_country_code': 'US',
      'method': 'auth.login',
      'fb_api_req_friendly_name': 'authenticate',
      'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
      'api_key': '882a8490361da98702bf97a021ddc14d'
  }

  data['sig'] = getSig(sortObj(data))

  sim = random.choice(['2e4', '4e4'])
  headers = {
      'x-fb-connection-bandwidth': random.choice(['2e7', '3e7']),
        'x-fb-sim-hni': sim,
        'x-fb-net-hni': sim,
        'x-fb-connection-quality': 'EXCELLENT',
        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
        'user-agent':
          'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger'
  }

  resp = requests.post(url="https://b-api.facebook.com/method/auth.login", data=data, headers=headers)
  #print(resp.text)
  return json.loads(resp.text)

print(Get_Facebook_Access_Token('username', 'password'))
