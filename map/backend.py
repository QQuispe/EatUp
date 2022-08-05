import requests
import urllib.request
import json
import googlemaps
import requests
from django.conf import settings

# Define the client
GOOGLE_API_KEY = settings.GOOGLE_MAPS_KEY
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

# Addresses from Django HTML will be fed to this function.
def get_address(address):
    if address.GET:
        address = address.GET
        address = address.urlencode()
        print(address)
        address = address.split("&")
        address1 = address[0].replace('your_name=', '')
        address2 = address[1].replace('your_name=', '')
        typeFood = address[2].replace('radio=', '')
        coordinates_list = (coordinate_output(address1, address2))
        center_lat, center_lng = center_finder(coordinates_list)
        return dump_jason(center_lat, center_lng, typeFood)


def get_lat_lng(address):
    geocode_namespace = 'https://maps.googleapis.com/maps/api/geocode/json?'
    geocode_link = geocode_namespace + "address=" + address + '&key=' + GOOGLE_API_KEY
    geocode_response = urllib.request.urlopen(geocode_link).read()
    geocode = json.loads(geocode_response)
    geocode_results = geocode.get('results')
    results_dict = geocode_results[0]
    lat_result = results_dict.get('geometry').get('location').get('lat')
    lng_result = results_dict.get('geometry').get('location').get('lng')
    return lat_result, lng_result


# Farshad - Replace final_address1 and final_address2. NOte that the format has to follow this: final_address1 = 'address=' + new_user_address1 + ',+' + new_user_city1 + ',+' + new_state_address1 + '&key='
def coordinate_output(final_address1, final_address2):
    coordinates_list = [get_lat_lng(final_address1),
                        get_lat_lng(final_address2)
                        ]
    return coordinates_list


def get_center_geometry(coordinates_list):
    latitude = []
    longitude = []
    for l in coordinates_list:
        latitude.append(l[0])
        longitude.append(l[1])

    center_lat = sum(latitude) / len(latitude)
    center_lng = sum(longitude) / len(longitude)
    return center_lat, center_lng


# center point of users
def center_finder(coordinates_list):
    center_lat, center_lng = get_center_geometry(coordinates_list)
    return center_lat, center_lng


# Define a business ID
def dump_jason(center_lat, center_lng, typeFood):
    # Define my API Key, My Endpoint, and My Header
    YELP_KEY = settings.YELP_KEY
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'bearer %s' % YELP_KEY}

    # Define Paramters -  Autocomplete
    PARAMETERS = {'text': 'good food',
                  'categories': typeFood,
                  'limit': 4, # How many restuarants are returned to front end
                  'latitude': center_lat,
                  'longitude': center_lng}

    # # Make a request to the Yelp API
    response = requests.get(url=ENDPOINT,
                            params=PARAMETERS,
                            headers=HEADERS)

    # # Conver the JSON String
    business_data = response.json()
    return business_data