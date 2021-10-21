from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from pprint import pprint

app_id = 'YOUR APP ID(L1)'
app_key = 'YOUR APP KEY(L1)'

class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = 'Wed, 20, Oct, 2021, 13:00:45 GMT'
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = hmac username="FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF"
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature=FPHnUuYn+TszUXXStubpJPs87LE=' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': xdate,
            'Accept - Encoding': 'gzip'
        }


if __name__ == '__main__':
    a = Auth(app_id, app_key)
    response = request('get', 'https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Taipei?$top=30&$format=JSON', headers= a.get_auth_header())
    pprint(response.content)