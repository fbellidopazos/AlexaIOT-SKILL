from geopy.geocoders import Nominatim
def reverseGEO(long,lat):
    geolocator = Nominatim(user_agent="Skill")
    location = geolocator.reverse(str(long)+","+str(lat))
    Location=str(location.address)
    return(",".join(Location.split(",", 2)[:2]))
