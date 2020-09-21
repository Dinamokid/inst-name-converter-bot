import requests

def nick_to_id(nickname, offset=None, timeout=30):  
    params = {'timeout': timeout, 'offset': offset}
    resp = requests.get("https://www.instagram.com/{}/?__a=1".format(nickname) , params)
    return resp.json()['graphql']['user']['id']

def id_to_nick(user_id, offset=None, timeout=30): 
    params = {'timeout': timeout, 'offset': offset}
    resp = requests.get("https://i.instagram.com/api/v1/users/{}/info/".format(user_id) , params)
    try: 
        return resp.json()['user']['username']
    except: 
        return "Json crush"
     