#!/usr/local/bin/python3

import sys
import cgi
import smtplib
import csv
import json
from email.mime.text import MIMEText
from urllib.parse import urlencode
from urllib.request import Request, urlopen

form = cgi.FieldStorage()
name =  form.getvalue('name')
email =  form.getvalue('email')
attendance =  form.getvalue('attendance')
guest =  form.getvalue('guest')
allergies =  form.getvalue('allergies')
recaptcha = form.getvalue('g-recaptcha-response')

url = 'https://www.google.com/recaptcha/api/siteverify'
post_fields = {'secret': '6Ld9WBQUAAAAAFnQ__rDorWS0UEcGI7ml6BZg9xN',
               'response': recaptcha}
request = Request(url, urlencode(post_fields).encode())
response = urlopen(request).read().decode()
content = json.loads(response)

if not content['success']:
    print("Content-Type: text/html")
    print()
    print("<title>Sepideh &amp; Philippe</title>")
    print("<h1>You are a robot</h1>")
    sys.exit(1)

#with open('rsvp.csv', 'a') as fp:
#    writer = csv.writer(fp)
#    writer.writerow([name, email, attendance, guest, allergies])

from_addr = 'philippe@sepidehphilippe.com'
to_addrs = ['philippe.pinard@gmail.com', 'sebrahimi1988@gmail.com']
text = 'name: {}\nemail: {}\nattendance: {}\nguest: {}\nallergies: {}' \
    .format(name, email, attendance, guest, allergies)
msg = MIMEText(text)
msg['Subject'] = 'Wedding RSVP'
msg['From'] = from_addr
msg['To'] = ';'.join(to_addrs)

s = smtplib.SMTP()
s.connect('smtp.webfaction.com')
s.login('sepidehphilippe','ahprETDzDe2Huk3ekH4j')
s.sendmail(from_addr, to_addrs, msg.as_string())
s.quit()

print("Content-Type: text/html")
print()
print("<title>Sepideh &amp; Philippe</title>")
print("<h1>RSVP</h1>")
print("<p>We have received your information. Thank you</p>")

