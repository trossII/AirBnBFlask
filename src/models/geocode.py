from geopy import Nominatim

def gcodeadd(data):
    address = data['address']
    geolocator = Nominatim(user_agent="BnB Flask")
    location = geolocator.geocode(address)
    data_geo = (location.longitude,location.latitude)
    return data_geo