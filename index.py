import os
from dotenv import load_dotenv
from geocoding import geoCode_connection, direction_to_coordinates
from geocoding import query_neighborhood, recursive_neighboring_neighborhood


if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv('key')
    connection = geoCode_connection(api_key)

    target_address = '1300 SE Stark Street, Portland, OR 97214'

    target_latitude, target_longitude = direction_to_coordinates(target_address, connection)

    neighborhood_name = query_neighborhood(target_latitude, target_longitude)

    neighborhood = recursive_neighboring_neighborhood(target_address, connection, neighborhood_name)

    print("The neighborhood with coordinates X={} Y={} is {}. The adjacent neighborhood is {}."
      .format(target_longitude, target_latitude, neighborhood_name, neighborhood))

