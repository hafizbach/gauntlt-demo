#! /usr/bin/python
# Prints "Exploit succeded", "Exploit failed", or "Error" (for when something doesn't work)
import requests

PREFIX = "http://127.0.0.1:8080/WebGoat/"

s = requests.Session()

r1 = s.get(PREFIX + "/login.mvc")
print s.cookies["JSESSIONID"]

r2 = s.post(PREFIX + "j_spring_security_check", data={"username": "guest", "password": "guest"})
if "Logout" not in r2.text:
     print "Error (login failed)"
     exit()
print s.cookies["JSESSIONID"]


