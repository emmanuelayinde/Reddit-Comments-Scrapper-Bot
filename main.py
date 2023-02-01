import time
from utils.date import now
from utils.format_comment import filter_comments_to_tweet
from utils.get_users_comments import get_comments_from_all_users

users = [
    "MyntCondytion",
    "HS_Celestalon",
    "ChakkiHS",
    "HS_Valerie_C",
    "IksarHS",
    "Cgsongbird",
    "HS_Liv",
    "cmdylux",
    "Kaeyoh",
]

i = 0

while True:
    print('Waking up......................... ', now())
    comments = get_comments_from_all_users(users)
    print("Comments", comments)
    filter_comments_to_tweet(comments)
    print('Done......................Sleep mode activated', now())

    # Sleep for 30secs, then continue
    time.sleep(60)

    
