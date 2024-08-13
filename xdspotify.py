# I think I might not be on the right track, but I love listening to HOT SINGLES on Spotify. - VintellX
import json
import requests
from base64 import b64encode
import os

xdimg = "assets/xd.png"
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
        raise Exception(f"{url} returned nothing.")
    else:
        return response.json()

def ms2time(xd):
    xd = int(xd)
    seconds = int((xd/1000)%60)
    minutes = int((xd/(1000*60))%60)
    hours = int((xd/(1000*60*60))%24)
    if hours == 0:
        return f"{minutes:02d}:{seconds:02d}"
    else:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

class Vinify:
    def __init__(self):
        try:
            self.data = fetchresp(currentlyPlayingURL)
        except Exception:
            self.data = fetchresp(recentlyPlayedURL)
    def fetchplaying(self):
        data = self.data
        if not "is_playing" in self.data:
            xd = {'status': "not_playing"}
        elif data["currently_playing_type"] != 'track':
            xd = {'status': "episode"}
        else:
            item = data["item"]
            artistName = item["artists"][0]["name"]
            songName = item["name"]
            xdstatus = f'playing:{songName}:{artistName}'
            if item["album"]["images"] == []:
                image = xdimg
            else:
                image = item["album"]["images"][1]["url"]
            duration = ms2time(float(item["duration_ms"]))
            songLink = item["external_urls"]["spotify"]
            artistLink = item["artists"][0]["external_urls"]["spotify"]
            xd = {'status': "is_playing", 'song': songName, 'artist': artistName, 'image': image, 'duration': duration, 'songLink': songLink, 'artistLink': artistLink}
        return xd
    def fetchhtml(self):
        notplaying = """
        <br><br><br><h3 class="nosong"><b>Vin</b> ain't listening to anything :(</h3>
        """ 
        episode = """
        <br><br><br><h3 class="nosong"><b>Vin</b> is listening to podcasts ;)</h3>
        """ 
        xdimage = """<img src="static/assets/xdimg.png" alt="Spotify Playing" width="200" height="200">"""
        xd = self.fetchplaying()
        if xd['status'] == "not_playing":
            texto = notplaying
            return texto, xdimage
        elif xd['status'] == "episode":
            texto = episode
            return texto, xdimage
        song = xd['song']
        artist = xd['artist']
        image = xd['image']
        duration = xd['duration']
        songLink = xd['songLink']
        artistLink = xd['artistLink']
        xdimage = f"""<img src="{image}" alt="Spotify Playing" width="271" height="271">"""
        texto = f"""<h2 class="song-title">Song: <a href="{songLink}" style="text-decoration: None;">{song}</a></h2><h3 class="song-artist">Artist: <a href="{artistLink}" style="text-decoration: None;">{artist}</a></h3><h4 class="song-ln">Duration: {duration}</h4>"""
        return texto, xdimage
