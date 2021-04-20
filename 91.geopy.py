from geopy.geocoders import Nominatim
from geopy.geocoders import Bing
from geopy.geocoders import ArcGIS
from geopy.distance import geodesic
from geopy.extra.rate_limiter import RateLimiter

import pprint
import pandas as pd


def main():

    # geolocator = Nominatim(user_agent="Some_app")
    # location = geolocator.reverse("35.6937632, 139.7036319")
    #
    # # geolocator = ArcGIS()
    # # geolocator = Bing("api_key")
    # # location = geolocator.geocode("東京都新宿区")
    #
    #
    # print(location.address)
    # print((location.latitude, location.longitude))
    # pprint.pprint(location.raw)

    # origin = (41.49008, -71.312796)
    # destination = (41.499498, -81.695391)
    # print(geodesic(origin, destination).km)
    # print(geodesic(origin, destination).meters)
    # print(geodesic(origin, destination).miles)

    df = pd.DataFrame({'name':['ベルリン', 'London', '東京都新宿区']})
    geolocator = Nominatim(user_agent="some_app")

    geocode = RateLimiter(geolocator.geocode)
    df['location'] = df['name'].apply(geocode)
    f = lambda loc: tuple(loc.point) if loc else None
    df['point'] = df['location'].apply(f)

    print(df.head())
    df.to_csv('geo.csv')









    return


if __name__ == '__main__':
    main()