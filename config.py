def get_config(inp):
	constant_val = {}
	constant_val['PRODUCT_ID'] = '6205' 
	constant_val['ITEM_ID'] = '101'
	constant_val['MAC_KEY'] = 'D3D1D05AFE42AD50818167EAC73C109168A0F108F32645C8B59E897FA930DA44F9230910DAC9E20641823799A107A02068F7BC0F4CC41D2952E249552255710F'
	constant_val['TEST_MODE'] = 'TRUE'
	constant_val['LIVE_URL'] = 'https://webpay.interswitchng.com/paydirect/pay'
	constant_val['TEST_URL'] = 'https://sandbox.interswitchng.com/webpay/pay'
	constant_val['LIVE_QUERY_URL'] = 'https://webpay.interswitchng.com/paydirect/api/v1/gettransaction.json'
	constant_val['TEST_QUERY_URL'] = 'https://sandbox.interswitchng.com/webpay/api/v1/gettransaction.json'
	constant_val['NORMALIZATION_FACTOR'] = '100'
	constant_val['SHA_KEY'] = 'TestKey'
	constant_val['CURRENCY_ID'] = '566'
	constant_val['RET_URL'] = 'http://www.jack-roe.co.uk:6785/websales/sales/master/tcpg_return/'
	constant_val['BASE_DIR'] = 'http://localhost/cgi_bin/interswitch_python/'
	constant_val['RET_URL'] = 'http://www.jack-roe.co.uk:6785/websales/sales/master/tcpg_return/'

	return constant_val[inp]
