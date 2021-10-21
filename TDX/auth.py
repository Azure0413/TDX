from hashlib import sha1
import hmac
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import base64
from requests import request
from pprint import pprint

app_id = '6e4483c0931943f0b52fdf61fa97277b'
app_key = 'UjB5oLj7-KT1W6Ki1NtC1OoYLo8'

class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = 'x-date: Thu, 21 Oct 2021 07:48:02 GMT'
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username=FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature=EKw7drl2J+4s4/TuTnk+9daZHnM=' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }


if __name__ == '__main__':
    a = Auth(app_id, app_key)
    response = request('get', 'https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/NewTaipei?$top=30&$format=JSON', headers= a.get_auth_header())
    pprint(response.content)