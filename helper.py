#!/usr/bin/python

from config import *
import hmac
from Crypto.Hash import SHA, HMAC


def hash_sha1(inp, key=None):
	if key is None:
		key = get_config('SHA_KEY')
	hashed = HMAC.new(key, inp, SHA)
	hashval = hashed.digest().encode("base64").rstrip('\n')
	return hashval


def getFailure(msg):
	response = {}
	response['code'] = "ERROR"
	response['msg'] = msg
	return response

def getSuccess(msg):
	response = {}
	response['code'] = "OK"
	response['msg'] = msg
	return response

def getCancelled(msg):
	response = {}
	response['code'] = "CANCELLED"
	response['msg'] = msg
	return response

def getBaseDir():
	return get_config('BASE_DIR')
