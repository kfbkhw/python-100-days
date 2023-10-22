from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

origin = "LON"
currency = "GBP"
recipient = "+821097565614"

data = DataManager()
sheet_data = data.get_values()

search = FlightSearch()
for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = search.find_code(city["city"])
        data.put_values(sheet_data)

notification = NotificationManager()
for city in sheet_data:
    data = search.search_flights(city["iataCode"], origin, currency)
    if city["city"] == data.to_city and city["lowestPrice"] >= data.price:
        print(notification.send_msg(data, recipient))
