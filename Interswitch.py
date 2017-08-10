#!/usr/bin/python
from config import *
import hashlib

class Interswitch:
	
	normalizationFactor = None;
	productId = None;
	itemId = None;
	macKey = None;
	testMode = None;
	interUrl = None;
	queryUrl = None;
	userDescription = None;
	currency = None;
	reference = None;
	orderTotal = None;
	redirectUrl = None;

	def __init__(self, ref, desc, amount, returnParam):
		self.normalizationFactor = get_config('NORMALIZATION_FACTOR')
		self.productId = get_config('PRODUCT_ID')
		self.itemId = get_config('ITEM_ID')
		self.macKey = get_config('MAC_KEY')
		self.testMode = get_config('TEST_MODE')
		self.currency = get_config('CURRENCY_ID')
	
		if self.testMode == 'TRUE' :
			self.interUrl = get_config('TEST_URL')
			self.queryUrl = get_config('TEST_QUERY_URL')
		else:
			self.interUrl = get_config('LIVE_URL')
			self.queryUrl = get_confif('LIVE_QUERY_URL')

		self.userDescription = desc
        	self.reference = ref
		self.orderTotal = amount
		self.redirectUrl = get_config('BASE_DIR')+"/processResponse.py";

	def getWebpayArgs(self):
		orderTotal = int(self.orderTotal) * int(self.normalizationFactor)
		orderTotal = str(orderTotal)
		hash_val = self.reference+self.productId+self.itemId+orderTotal+self.redirectUrl+self.macKey
		hash_val = hashlib.sha512(hash_val).hexdigest()
		webpay_args = {}
		webpay_args['product_id'] = self.productId
		webpay_args['amount'] = orderTotal
		webpay_args['currency'] = self.currency
		webpay_args['site_redirect_url'] = self.redirectUrl
		webpay_args['txn_ref'] = self.reference
		webpay_args['hash'] = hash_val
		webpay_args['pay_item_id'] = self.itemId
		webpay_args['cust_name'] = 'Pending Payment'
		webpay_args['cust_name_desc'] = 'Customer Name'
		webpay_args['cust_id'] = self.reference
		webpay_args['cust_id_desc'] = 'Transaction Reference'

		return webpay_args

	def initiateTransfer(self):
		webpayArgs = self.getWebpayArgs()
		webpayArgsArray = []

		for key, value in webpayArgs.items():
			webpayArgsArray.append('<input type="hidden" name="'+key+'" value="'+value+'" />')

		html = '<form action="' + self.interUrl + '" method="post" id="webpay_payment_form" target="_top">' + ''.join(webpayArgsArray ) + '<!-- Button Fallback --><div class="payment_buttons"><input type="submit" class="button alt" id="submit_webpay_payment_form" value="Pay via Interswitch Webpay" /></div><script type="text/javascript"> $("document").ready(function () {$("#submit_webpay_payment_form").click();$(".payment_buttons").hide();});</script></form>'

		print(html)
