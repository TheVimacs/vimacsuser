# I think I might not be on the right track, but I love listening to HOT SINGLES on Spotify. - VintellX
import json
import requests
from base64 import b64encode
import os

xdimg = "static/assets/xdimg.png"
spotifyRefreshTokeno = os.environ.get("SPOTIFY_REFRESH_TOKEN")
currentlyPlayingURL = "https://api.spotify.com/v1/me/player/currently-playing"
recentlyPlayedURL = "https://api.spotify.com/v1/me/player/recently-played?limit=10"
spotifyTokeno = ""
refreshTokenURL = "https://accounts.spotify.com/api/token"
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET_ID = os.environ.get("SPOTIFY_SECRET_ID")

def getAuth():
    return b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_SECRET_ID}".encode()).decode(
        "ascii"
    )

def refreshToken():
    data = {
        "grant_type": "refresh_token",
        "refresh_token": spotifyRefreshTokeno,
    }

    headers = {"Authorization": "Basic {}".format(getAuth())}
    response = requests.post(
        refreshTokenURL, data=data, headers=headers).json()

    try:
        return response["access_token"]
    except KeyError:
        raise KeyError(str(response))   

def fetchresp(url):
    global spotifyTokeno

    if (spotifyTokeno == ""):
        spotifyTokeno = refreshToken()

    response = requests.get(
        url, headers={"Authorization": f"Bearer {spotifyTokeno}"})

    if response.status_code == 401:
        spotifyTokeno = refreshToken()
        response = requests.get(
            url, headers={"Authorization": f"Bearer {spotifyTokeno}"}).json()
        return response
    elif response.status_code == 204:
