# import uuid
# import requests
# import json
#
# # https://watch.plex.tv/live-tv/channel/euronews-espanol
# url = 'https://plex.tv/api/v2/users/anonymous'
# headers = {
#     'accept': 'application/json',
#     'X-Plex-Client-Identifier': str(uuid.uuid4()),
#     'X-Plex-Language': 'en',
#     'X-Plex-Product': 'Plex Mediaverse',
#     'X-Plex-Provider-Version': '6.3.0'
# }
# response = requests.post(url, headers=headers)
# response_json = json.loads(response.text)
# plex_token = response_json['authToken']
# print(plex_token)


