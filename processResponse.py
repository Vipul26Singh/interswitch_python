#!/usr/bin/python
import cgi
from config import *
from response import *
from helper import *
from Interswitch import *
from processRequest import *

print("Content-Type: text/html\n")

POST = cgi.FieldStorage()

amount = POST['amount']
txnId = POST['txnref']

response = getSuccess(POST['resp'])
returnUrl = get_config('RET_URL')

sendResponse(returnUrl, response['code'], amount, txnId, response['msg'])

print("done")
