import requests
import json

def is_live_stream(client_id):
	twitch_api_stream_url = "https://api.twitch.tv/kraken/streams/overwatchleague?client_id=" + client_id
	request_body = requests.get(twitch_api_stream_url)
	stream_json = request_body.json()
	#body_list = stream_json["stream"]
	status = stream_json["stream"]["stream_type"]
	if status == "live":
		status = True
	else:
		status = False
	return status