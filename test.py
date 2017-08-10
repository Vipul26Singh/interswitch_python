#!/usr/bin/python
from hashlib import sha1
import hmac
from helper import hash_sha1
import uuid
from processRequest import *

print("Content-type: text/html\n\n")

txnid = str(uuid.uuid4())
amount = "1234";
siteCode = "TESTSITE";
returnUrl = "https://www.jack-roe.co.uk/websales/sales/master/payment_finished";
description = "TaPoS";
keyinput = "%s%s%s%s%s" % (txnid, siteCode, amount, returnUrl, description)
key_input = hash_sha1(keyinput);

processRequest(txnid, siteCode, amount, returnUrl, description, key_input);
