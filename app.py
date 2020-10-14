import requests
import pprint
import sys

# See http://www.unixtimestamp.com/ to generate Unix timestamps online
payload = {
            'until': 1600560000, # Unix timestamps
            'since': 1600716977, # Unix timestamps
            'limit': 4, # number of posts
            'access_token':'token do facebook'

        }

base_api = 'https://graph.facebook.com'
posts_endpoint = base_api + '/me/posts/'

posts_response = requests.get(posts_endpoint, params=payload)

if posts_response.status_code != requests.codes.ok:
    print('Error: ' + posts_response.json()['error']['message'])
    sys.exit(0)

posts_dict = posts_response.json()['data']
#pprint.pprint(posts_dict)


for post in posts_dict:
    print("A eliminar [%s] %s" % (post['id'], post['name']))
    requests.delete(base_api + '/' + post['id'], params=payload)
    print("Eliminado [%s] %s\n" % (post['id'], post['name']))

print("Total de posts eliminados: %d" % len(posts_dict))
