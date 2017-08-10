#!/usr/bin/python

from config import *
from helper import *
import uuid


def redirect_post(url, params, msg = None):
	html = ""
	html = html+'<!doctype html><html><body><form id="redirect_form" method="post" action="'+url+'" >'

	for k, v in params.items():
		html = html+"<input type='hidden' name='"+k+"' id='"+k+"' value='"+v+"' />"
	
	html = html+msg+"<br><input type='submit' value='continue'></form></body></html>"
	print(html)

def sendResponse(url, result, amount, reference, errmess):
	iid1 = str(uuid.uuid4())
	iid1 = iid1.replace("-","")
	iid2 = 'TAPOSSTA_'+iid1
	iid = iid2[:32]

	key = hash_sha1(result+iid+amount+reference+errmess)
	
	params = {}
	params['url'] = url
	params['result'] = result
	params['amount'] = amount
	params['reference'] = reference
	params['errmess'] = errmess
	params['key'] = key

	redirect_post(url, params, params['errmess']);
