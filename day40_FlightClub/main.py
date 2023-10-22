from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user import Users

origin = "LON"
currency = "GBP"
recipient = "+821097565614"

user = Users()
data = DataManager()
data.post_users(user.user_info())

sheet_data = data.get_values()
search = FlightSearch()
for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = search.find_code(city["city"])
        data.put_code(sheet_data)

notification = NotificationManager()
for city in sheet_data:
    data = search.search_flights(city["iataCode"], origin, currency)
    if city["city"] == data.to_city and city["lowestPrice"] >= data.price:
        for user in user.user_list:
            notification.send_mail(data, user["email"])
