#!/usr/bin/python
from Interswitch import *
from config import *
from response import *

def processRequest(txnId, siteCode, amount, returnUrl, description, keyInput):
        keyGenerated = txnId+siteCode+amount+returnUrl+description
        keyGenerated = hash_sha1(keyGenerated, get_config('SHA_KEY'))

        if keyGenerated != keyInput :
                response = getFailure('Invalid key')
                sendResponse(returnUrl, response['code'], amount, txnId, response['msg']);
                return None

	interswitch = Interswitch(txnId, description, amount, returnUrl)
	interswitch.initiateTransfer()
