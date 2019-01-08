import billboard, spotipy
from datetime import date, timedelta
from credentials import my_client_id, my_client_secret
from spotipy.oauth2 import SpotifyClientCredentials

####################################
# Getting access to Spotify APIs with the credentials
client_credentials = SpotifyClientCredentials(client_id=my_client_id,
                                              client_secret=my_client_secret,
                                              proxies=None)
# Gets access token
token = client_credentials.get_access_token()
# Creates interactive API object
sp = spotipy.Spotify(auth=token, client_credentials_manager=client_credentials)
####################################
def r_b_chart(date_arg):
    """R&B chart for that date.
    """
    return billboard.ChartData('r-b-hip-hop-songs', date=date_arg)

week = timedelta(days=7)
most_recent = date.today() - week

chart = r_b_chart(str(most_recent))
song = chart[1]


def query_maker(title=None, artist=None):
    """Formats the query for the Spotify search API.
    API Docs for search: https://developer.spotify.com/documentation/web-api/reference/search/search/
    """
    return "track: {0} artist: {1}".format(title, artist)


featuring_len = len("featuring")


def no_features(artist):
    """Formats artist string to take out features and just contain principle
    artist
    """
    artist = artist.lower()
    for i in range(len(artist)):
        if artist[i] == "&" or (artist[i] == "f" and artist[i : i + featuring_len] == "featuring"):
            return artist[0 : i - 1]
    return artist



query = query_maker(song.title, no_features(song.artist))

search_results = sp.search(query, limit=5, offset=0, type='track', market=None)
search_results_tracks = search_results["tracks"]["items"]



def print_track(track):
    """Prints spotify Track object name and artists
    """
    print("Track Name:", track["name"])
    for artist in track["artists"]:
        print(artist["name"])
    print()
    return

print_track(search_results_tracks[0])
