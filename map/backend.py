# Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
# Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
# Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

# Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
# Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

# Businesses, Total, Region

# Import the modules
import requests
import urllib.request
import json
import googlemaps
import pprint
import time
import requests

# Define the client
api_key = 'YOUR_GOOGLE_API_KEY'
gmaps = googlemaps.Client(key=api_key)


# Code only for testing. Will be removed once HTML feeds the addresses into get_lat_lng()
# user_address1 = input('Enter address: ').split()
# new_user_address1 = '+'.join(user_address1)
# user_city1 = input('Enter city: ').split()
# new_user_city1 = '+'.join(user_city1)
# user_state1 = input('Enter state: ').split()
# new_state_address1 = '+'.join(user_state1)
# final_address1 = 'address=' + new_user_address1 + ',+' + new_user_city1 + ',+' + new_state_address1 + '&key='
# user_address2 = input('Enter address: ').split()
# new_user_address2 = '+'.join(user_address2)
# user_city2 = input('Enter city: ').split()
# new_user_city2 = '+'.join(user_city2)
# user_state2 = input('Enter state: ').split()
# new_state_address2 = '+'.join(user_state2)
# final_address2 = 'address=' + new_user_address2 + ',+' + new_user_city2 + ',+' + new_state_address2 + '&key='


# from django.http import QueryDict
# Farshad - Addresses from Django HTML will be fed to this function.
def get_address(address):
    print("***********")
    # address = address.lists()
    # address = [i for i in address]
    # for i in address:
    #   print(i)

    if address.GET:
        address = address.GET
        address = address.urlencode()
        print(address)
        address = address.split("&")
        address1 = address[0].replace('your_name=', '')
        address2 = address[1].replace('your_name=', '')
        typeFood = address[2].replace('radio=', '')
        # print(address1)
        # print(address2)
        print(typeFood)
        coordinates_list = (coordinate_output(address1, address2))
        center_lat, center_lng = center_finder(coordinates_list)
        return dump_jason(center_lat, center_lng, typeFood)
        # address = address[1]
        # address = address.split('&')
        # address = str(address[0])
        # address = urllib.parse.unquote(address)
        # print(address)


def get_lat_lng(address):
    geocode_namespace = 'https://maps.googleapis.com/maps/api/geocode/json?'
    geocode_link = geocode_namespace + "address=" + address + '&key=' + api_key
    # print(geocode_link)
    geocode_response = urllib.request.urlopen(geocode_link).read()
    geocode = json.loads(geocode_response)
    # print(geocode)
    geocode_results = geocode.get('results')
    results_dict = geocode_results[0]
    lat_result = results_dict.get('geometry').get('location').get('lat')
    lng_result = results_dict.get('geometry').get('location').get('lng')
    print(lat_result, lng_result)
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
    dic = {}
    business_id = 'YOUR_BUSINESS_ID'
    unix_time = 1546047836

    # Define my API Key, My Endpoint, and My Header
    API_KEY = 'YOUR_YELP_API_KEY'
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'.format(business_id)
    HEADERS = {'Authorization': 'bearer %s' % API_KEY}

    # Define my parameters of the search
    # BUSINESS SEARCH PARAMETERS - EXAMPLE
    # PARAMETERS = {'term': 'food',
    #              'limit': 1,
    #              'offset': 50,
    #             'radius': 10000,
    #             'location': 'San Diego'}

    # coordinates_list = coordinate_output(final_address1, final_address2)
    # center_lat, center_lng = center_finder(coordinates_list)
    # # Define Paramters -  Autocomplete
    print(typeFood)
    PARAMETERS = {'text': 'good food',
                  'categories': typeFood,
                  'limit': 3,
                  'latitude': center_lat,
                  'longitude': center_lng}

    # # Make a request to the Yelp API
    response = requests.get(url=ENDPOINT,
                            params=PARAMETERS,
                            headers=HEADERS)

    # # Conver the JSON String
    business_data = response.json()

    # # print the response
    # print(json.dumps(business_data, indent=3))
    #
    # restaurants = []
    #
    # for i in range(0, PARAMETERS['limit']):
    #     dic = dict()
    #     restaurant_name = business_data['businesses'][i]['name']
    #     dic['name'] = restaurant_name
    #
    #     image_url = business_data['businesses'][i]['image_url']
    #     dic['image'] = image_url
    #
    #     is_closed = business_data['businesses'][i]['is_closed']
    #     dic['is_closed'] = is_closed
    #
    #     url = business_data['businesses'][0]['url']
    #     dic['url'] = url
    #
    #     food_type = business_data['businesses'][i]['categories'][0]['title']
    #     dic['food_type'] = food_type
    #
    #     rating = business_data['businesses'][i]['rating']
    #     dic['rating'] = rating
    #
    #     coordinates = business_data['businesses'][i]['coordinates']
    #     dic['coordinates'] = coordinates
    #
    #     price = business_data['businesses'][i]['price']
    #     dic['price'] = price
    #     # print(price)
    #
    #     location = business_data['businesses'][i]['location']
    #     dic['location'] = location
    #     # print(location)
    #
    #     phone = business_data['businesses'][i]['phone']
    #     # print(phone)
    #     dic['phone'] = phone
    #
    #     display_phone = business_data['businesses'][i]['display_phone']
    #     dic['display_phone'] = display_phone
    #     # print(display_phone)
    #
    #     distance = business_data['businesses'][i]['distance']
    #     dic['distance'] = distance
    #     restaurants.append(dic)
    #     # print(distance)
    #     # print(dic)
    # # print(type(business_data))

    # return business_data (dictionary)
    return business_data
