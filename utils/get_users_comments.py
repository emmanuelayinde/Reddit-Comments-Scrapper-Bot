import time
import requests

from utils.date import now

users = [
    "HS_Celestalon",
    "ChakkiHS",
    "HS_Valerie_C",
    "IksarHS",
    "Cgsongbird",
    "HS_Liv",
    "MyntCondytion",
    "cmdylux",
    "Kaeyoh",
]
subreddit_list = ["hearthstone", "bobstavern", "customhearthstone"]
recent_comments = []

# { id, subreddit, author, link_title, body, link_permalink }
def get_comments(user):
    print(f'Getting recent comments from user - {user}........')   
    r = requests.get(f'https://www.reddit.com/user/{user}/comments.json', headers = {'User-agent': 'reddit>comments>botv1.0'}, params = { 'sort': "top", 't': "month" })
    data = r.json()
    return data

def parse_data(data):
    c = data['data']['children']

    if len(data['data']['children']) != 0:
        for d in c:
            if d['data']['subreddit'] in subreddit_list:
                comment = {
                    'id': d['data']['id'],
                    'subreddit': d['data']['subreddit'],
                    'author': d['data']['author'],
                    'title': d['data']['link_title'],
                    'comment': d['data']['body'],
                    'post_url': d['data']['link_permalink']
                }
                recent_comments.append(comment)
            else: 
                print(f'The subreddit is not supported') 

    print('Done parsing data..............', now())            

    # return recent_comments 


def get_comments_from_all_users(users):
    print(len(users))
    for user in users:
        user_comments = get_comments(user)
        time.sleep(5)
        parse_data(user_comments)
        time.sleep(1)

    return recent_comments     


# print(get_comments_from_all_users(users))