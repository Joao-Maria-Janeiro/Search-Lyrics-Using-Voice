import requests
import json
import re
import keys

def execute(artist, track):
    base_url = 'https://api.musixmatch.com/ws/1.1/'
    lyrics_matcher = 'matcher.lyrics.get'
    format_url = "?format=jsonp&callback=callback"
    track_parameter = '&q_track='
    artist_parameter = "&q_artist="
    api_key = '&apikey=' + keys.musixmatch_key

    artist_name = artist
    track_name = track

    api_call = base_url + lyrics_matcher + format_url + track_parameter + track_name + artist_parameter + artist_name + api_key

    data = requests.get(api_call)
    data = data.text
    data = data[9:-2]
    data = json.loads(data)
    try:
        data = data['message']['body']
        print()
        print(data['lyrics']['lyrics_body'])
    except:
        print("The artist or song is not in the database or does not exist")
