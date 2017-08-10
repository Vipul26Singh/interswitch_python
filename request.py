#!/usr/bin/python
from hashlib import sha1
import hmac
from helper import hash_sha1
import uuid
from processRequest import *
import cgi

print("Content-Type: text/html\n")

POST = cgi.FieldStorage()
txnid = POST['reference'].value
amount = POST['amount'].value
siteCode = POST['sitecode'].value
returnUrl = POST['returnurl'].value
description = POST['description'].value
key_input = POST['key'].value

processRequest(txnid, siteCode, amount, returnUrl, description, key_input)
