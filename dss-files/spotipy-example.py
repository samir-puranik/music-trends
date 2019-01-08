# SPOTIPY DOCS: https://spotipy.readthedocs.io/en/latest/

import spotipy
from credentials import my_client_id, my_client_secret
from spotipy.oauth2 import SpotifyClientCredentials

print(my_client_id)

client_credentials = SpotifyClientCredentials(client_id=my_client_id, client_secret=my_client_secret, proxies=None)

token = client_credentials.get_access_token()
print(token)

sp = spotipy.Spotify(auth=token, client_credentials_manager=client_credentials)

track_id = "spotify:track:0cjvRZVV217eDcZXXTHxBl"
print(sp.track(track_id))
