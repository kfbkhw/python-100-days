import requests
from datetime import datetime

TOKEN = "tokenforkfbkhw"
USER = "kfbkhw"

# 1. Create User Account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# 2. Create Graph
graph_endpoint = "/<username>/graphs".replace("<username>", USER)
graph_config = {
    "id": "graph01",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}
header = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=pixela_endpoint+graph_endpoint, json=graph_config, headers=header)
# print(response.text)

# 3. Post Value
date = datetime.now().strftime("%Y%m%d")
record = [
    {
        "date": date,
        "quantity": "15"
    },
]
pixel_endpoint = "/<graphID>".replace("<graphID>", graph_config["id"])
pixel_config = {
    "date": record[0]["date"],
    "quantity": record[0]["quantity"],
}
# response = requests.post(url=pixela_endpoint+graph_endpoint+pixel_endpoint, json=pixel_config, headers=header)
# print(response.text)

# 4. Get Date Value
# now_time = datetime.now()
# time = datetime(2023, 10, 4)
# print(str(time.date()).replace("-", ""))
# print(time.strftime("%Y%m%d"))

# 5. Update Pixel Value
update_date = datetime(2023, 10, 10).strftime("%Y%m%d")
update_quantity = "10"
update_endpoint = "/<yyyyMMdd>".replace("<yyyyMMdd>", update_date)
update_param = {
    "quantity": update_quantity
}
# response = requests.put(url=pixela_endpoint+graph_endpoint+pixel_endpoint+update_endpoint, json=update_param, headers=header)
# print(response.text)

# 6. Delete Pixel Value
delete_date = datetime(2023, 10, 8).strftime("%Y%m%d")
delete_endpoint = "/<yyyyMMdd>".replace("<yyyyMMdd>", delete_date)
# response = requests.delete(url=pixela_endpoint+graph_endpoint+pixel_endpoint+delete_endpoint, headers=header)
# print(response.text)
