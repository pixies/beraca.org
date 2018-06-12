import requests
import json
from enum import Enum
#api - fd12293b-b0f5-47d2-b55d-bc73b1ce3f7f - me
#	apiKey = '13fbc116-f2e9-4698-b192-12beec07342b' - simpson
class ApiClient:
	apiUri = 'https://api.elasticemail.com/v2'
	apiKey = "" #'fd12293b-b0f5-47d2-b55d-bc73b1ce3f7f'

	def Request(method, url, data):
		data['apikey'] = ApiClient.apiKey
		if method == 'POST':
			result = requests.post(ApiClient.apiUri + url, params = data)
		elif method == 'PUT':
			result = requests.put(ApiClient.apiUri + url, params = data)
		elif method == 'GET':
			attach = ''
			for key in data:
				attach = attach + key + '=' + data[key] + '&'
			url = url + '?' + attach[:-1]
			result = requests.get(ApiClient.apiUri + url)

		jsonMy = result.json()

		if jsonMy['success'] is False:
			return jsonMy['error']

		return jsonMy['data']

def SendElastic(subject, to_list, html_body, mail_from="contato@institutoberaca.org"):
	return ApiClient.Request('POST', '/email/send', {
		'subject': subject,
		'from': mail_from,
		'to': to_list,
		'bodyHtml': html_body,
		'bodyText': "bodyText",
		'isTransactional': True})

# testing
#print(Send("ReparteBR :: Apoio a Projeto", "cleyton.flb@gmail.com", "cleytonfabio@tagi.com.br; hjaysimpsoncoorp@gmail.com", "<h1>Ola</h1>" ))
#print(Send("Your Subject", "cleyton.flb@gmail.com", "atalapitecos coorp", "<h1>Html Body</h1>", "Text Body", True))
