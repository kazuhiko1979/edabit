import os
import requests
import math
from skimage import io
from io import BytesIO
import random
import warnings
import numpy as np

TOKEN = "1VDgnHj9u7SX3h32FB8dzd133M4DYlRl"
DOMAIN = 'tellusxdp.com'


def search_AVNIR2_scenes(min_lon, min_lat, max_lon, max_lat):
    url = 'https://gisapi.{}/api/v1/av2ori/scene'.format(DOMAIN)
    headers = {
        'Authorization': 'Bearer ' + TOKEN
    }
    payload = {'min_lat': min_lat, 'min_lon': min_lon,
               'max_lat': max_lat, 'max_lon': max_lon}

    r = requests.get(url, params=payload, headers=headers)
    # if r.status_code != 200:
    #     raise ValueError('status error({}).'.format(r.status_code))
    return r.json()


def get_AVNIR2_scene_tile(rsp_id, product_id, zoom, xtile, ytile,
                          opacity=1, r=3, g=2, b=1, rdepth=1, gdepth=1, bdepth=1, preset=None):
    # zoom = 8 - 14
    url = 'https://gisapi.{}/av2ori/{}/{}/{}/{}/{}.png'.format(
        DOMAIN, rsp_id, product_id, zoom, xtile, ytile)
    headers = {
        'Authorization': 'Bearer ' + TOKEN
    }

    payload = {'preset': preset, 'opacity': opacity, 'r': r, 'g': g,
               'b': b, 'rdepth': rdepth, 'gdepth': gdepth, 'bdepth': bdepth}

    r = requests.get(url, params=payload, headers=headers)
    if not r.status_code == requests.codes.ok:
        r.raise_for_status()
    return io.imread(BytesIO(r.content))


def get_tile_num(lat, lon, zoom):
    """
    緯度経度からタイル座標を取得する
    """
    # https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Python
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    xtile = int((lon + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)


def get_tile_bbox(z, x, y):
    """
    タイル座標からバウンディングボックスを取得する
    https://tools.ietf.org/html/rfc7946#section-5
    """

    def num2deg(xtile, ytile, zoom):
        # https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Python
        n = 2.0 ** zoom
        lon_deg = xtile / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
        lat_deg = math.degrees(lat_rad)
        return (lon_deg, lat_deg)

    right_top = num2deg(x + 1, y, z)
    left_bottom = num2deg(x, y + 1, z)
    return (left_bottom[0], left_bottom[1], right_top[0], right_top[1])


# 日本周辺のシーン情報を取得し、ランダムに30シーン絞り込み
scenes = search_AVNIR2_scenes(120.0, 24.0, 155.0, 46.0)
random_scenes = random.sample(scenes, 30)

# ズーム率12でそのシーンから切り出せるタイル画像をすべて取得する
zoom = 12
for scene in random_scenes:
    (xtile, ytile) = get_tile_num(scene['max_lat'], scene['min_lon'], zoom)

    x_len = 0
    while (True):
        bbox = get_tile_bbox(zoom, xtile + x_len + 1, ytile)
        tile_lon = bbox[0]
        if (tile_lon > scene['max_lon']):
            break
        x_len += 1

    y_len = 0
    while (True):
        bbox = get_tile_bbox(zoom, xtile, ytile + y_len + 1)
        tile_lat = bbox[3]
        if (tile_lat < scene['min_lat']):
            break
        y_len += 1

    for x in range(x_len):
        for y in range(y_len):
            try:
                img = get_AVNIR2_scene_tile(scene['rspId'], scene['productId'], zoom, xtile + x, ytile + y)
                if (np.sum(np.ravel(img))) > 0:
                    with warnings.catch_warnings():
                        warnings.simplefilter('ignore')
                        io.imsave(os.getcwd() + '/tile/{}_{}_{}.png'.format(zoom, xtile + x, ytile + y), img)
            except Exception as e:
                print(e)