import googlemaps as maps
import requests

def geoCode_connection(api_key):
    return maps.Client(key=api_key)
"""Allows us to connect to our Google Maps Api
    api_key: comes from environmental variables
"""

def direction_to_coordinates(direction, connect_api):
    geoResult = connect_api.geocode(direction)
    latitude = geoResult[0]['geometry']['location']['lat']
    longitude = geoResult[0]['geometry']['location']['lng']
    return latitude, longitude
"""Calculates the address coordinates
    direction: address,
    connect_api: connection to us api.
"""

def query_neighborhood(latitude, longitude):
    link = "https://www.portlandmaps.com/arcgis/rest/services/Public/COP_OpenData/MapServer/125/query"
    parameters = {
        'where': '1=1',
        'geometry': f"{{'x':{longitude},'y':{latitude}}}",
        'f': 'json',
        'geometryType': 'esriGeometryPoint',
        'inSR':4326,
    }
    
    response = requests.get(link, params=parameters)
    return response.json()['features'][0]['attributes']['NAME']
"""Calculates the name of a neighborhood from a longitude and latitude.
    latitude, longitude: float,
"""

def modify_address(address, value=100):

    parts = address.split(" ")
    house_number = int(parts[0]) + value
    modified_address = " ".join([str(house_number)] + parts[1:])
    return modified_address
    
    return address
"""We made a change in the address that was requested by adding an amount.
"""

def recursive_neighboring_neighborhood(address, connection, neighboring):
    
    latitude, longitude = direction_to_coordinates(address, connection)
    neighborhood = query_neighborhood(latitude, longitude)
    if( neighborhood != neighboring ):
        return neighborhood
    else:
        address = modify_address(address)
        return recursive_neighboring_neighborhood(address, connection, neighboring)
"""The name of the adjacent neighborhood is found.
    address: address,
    connection: connection to us api.
    neighboring: Neighborhood name 
"""
