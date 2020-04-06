import requests
import os
import json

from Constants import ProPublicaFileLocation, Debugging, houseMembersURL

def get_key():
	key = ''
	with open(ProPublicaFileLocation(), 'r') as f:
		key = f.read()
		key = key.strip('\n').strip()
	if not key:
		raise ValueError

	os.environ['ProPublicaAPIKey'] = key
	return key 


def authenticationHeaders():
	ApiKey = get_key()
	return {'X-API-Key': ApiKey}


def houseMembers():
	url = houseMembersURL()
	headers = authenticationHeaders()

	r = requests.get(url, headers=headers)
	r.raise_for_status()

	json_dict = json.loads(r.text)
	members_list =  []
	try: 
		members_list = json_dict["results"][0]["members"]
	except Exception:
		print("Error processing JSON")

	return members_list



