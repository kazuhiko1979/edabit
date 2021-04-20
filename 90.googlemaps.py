import googlemaps
import pprint


def main():

    api_key = '********************************'
    gmaps = googlemaps.Client(key=api_key)

    # json = gmaps.geocode("東京都新宿区")
    # pprint.pprint(json)

    # json = gmaps.reverse_geocode((35.7298995, 139.7451386))
    # pprint.pprint(json)

    origin = (35.6869796, 139.7162792)
    destination = (35.6869489, 139.7472135)
    json = gmaps.directions(origin, destination)
    pprint.pprint(json)


    return


if __name__ == '__main__':

    main()