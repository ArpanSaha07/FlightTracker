import requests


def states_accessor():
    # Go through the doc api examples!
    url = f"https://opensky-network.org/api/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())


def tracks_accessor():
    url = f"https://opensky-network.org/api/tracks/all?icao24=3c4b26&time=0"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())
