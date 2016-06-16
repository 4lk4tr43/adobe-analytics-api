import base64
import json
import time
from hashlib import sha256
from datetime import datetime
import httplib2

u = ''
s = ''

c = datetime.today().isoformat()
n = str(int(time.time()))

f1 = base64.b64encode(sha256(n + c + s).digest())
f2 = base64.b64encode(n)

#wsse_header = 'X-WSSE' : 'UsernameToken Username="' + u + '", PasswordDigest="' + d + '", Nonce="' + n + '", Created="' + c,

class ReportDescription:
    def __init__(self):
        self.reportSuiteId = ''

payload = '{' + json.dumps(ReportDescription().__dict__) + '}'

http = httplib2.Http()
http.add_credentials(u, s)
httplib2.WsseAuthentication()
print http.request('https://api.omniture.com/admin/1.4/rest/?method=Report.Queue', 'POST', payload)