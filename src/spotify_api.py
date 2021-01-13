import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json, sys
import src.config as config

config = config.load()

def download_liked():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=config['spotify']['username'],
                                                       scope=config['spotify']['scope'],
                                                       client_id=config['spotify']['client_id'],
                                                       client_secret=config['spotify']['client_secret'],
                                                       redirect_uri=f'http://127.0.0.1:{config["spotify"]["redirect_uri_port"]}'))


    print('Fetching liked songs')
    # Load spotify liked songs object
    results = sp.current_user_saved_tracks()
    songs = results['items']
    idx = 1
    while results['next']:
        if idx % 50 == 0:
          print()
        sys.stdout.write(".")
        idx = idx +1
        #print(f'API hit: {idx}')
        results = sp.next(results)
        songs.extend(results['items'])

    print()

    ret = {}
    for s in songs:
        ret[s['track']['external_ids']['isrc']] = s

    with open(config['script']['paths']['liked_songs'], mode='w', encoding='utf-8') as f:
        json.dump(ret, f, indent=4, sort_keys=True)

