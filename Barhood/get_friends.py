"""
use Facebooks Graph API to get a list of a user's friends

To generate an access token for testing, go to Graph API Explorer
    * put token into configs.py

For generating a user's access token in production see
https://developers.facebook.com/docs/javascript/quickstart


Big Caveat:
    apps are no longer able to retrieve the full list of a user's friends (only those friends who have specifically authorized your app using the user_friends permission)

    see http://stackoverflow.com/questions/23417356/facebook-graph-api-v2-0-me-friends-returns-empty-or-only-friends-who-also-u
"""

import requests
import facebook
from configs import play_token


graph = facebook.GraphAPI(play_token)
friends = graph.get_object("me/friends")

for friend in friends['data']:
    print(friend['name'], friend['id'])
        
