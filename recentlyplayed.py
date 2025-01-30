#import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your credentials
client_id = 'da23dea1effe47aa9a166aae9f75a940'
client_secret = '372afc0e83154ed2976330775037b61e'
redirect_uri = 'http://localhost:8888/callback'

# Set up Spotify OAuth
scope = 'user-read-recently-played' 
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, cache_path='.cache')

# Create a Spotipy client
sp = spotipy.Spotify(auth_manager=sp_oauth)

# Get current user's playlists
recent_tracks = sp.current_user_recently_played(limit=50)

# Print the track names, artist of each tracks and played times
for item in recent_tracks['items']:
    track = item['track']
    played_at = item['played_at']
    artist = track['artists'][0] 
    print(f"Track: {track['name']}")
    print(f"Played at: {played_at}")
    print(f"Artist: {artist['name']}")
    print("-------" * 10)



