import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

USERNAME = 'timmmmmmmmmmmmmmmm'
PASSWORD = 'awdoi12e3awd03'
GRAPH = 'graph1'

user_params = {
    "token": PASSWORD,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":'yes'
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id": "graph1",
    "name": "Russian Learning",
    "unit": "Hrs",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN":PASSWORD
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

current_date = str(datetime.now().strftime("%Y%m%d"))

body = {
    "quantity": "2",
    "date": current_date
}

# Creates the graph if already not existed
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# print(response.text)


full_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}'

response = requests.post(full_endpoint, json=body,headers=headers)
print(response.text)
#
# print(current_date)
# full_endpoint_put = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{current_date}'
#
#
# response = requests.put(full_endpoint_put,json=body,headers=headers)
# print(response.text)
#
# response = requests.delete(full_endpoint_put,headers=headers)
# print(response.text)