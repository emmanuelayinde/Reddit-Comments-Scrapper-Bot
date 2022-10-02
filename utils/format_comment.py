import os
from utils.date import now
from utils.formatter import format_description_text

from utils.tweet import tweet
file_path = os.getcwd() + '/data/tweeted_comments.txt'


def format_comment(comment):
    title = "📢 Reddit comment spotted 📢"
    comment_author = comment['author']
    comment_text = comment['comment']
    comment_post_title = comment['title']
    # comment_post_url = comment['post_url']
    comment_url = comment['comment_url']

    # t_len = f'{title}\n\n🔴 {comment_post_title}\n🕵️‍♂️{comment_author}\n📝\n\n🌐{comment_post_url}'
    # formatted_comment_text = format_description_text(comment_text, len(t_len))
    # text = f'{title}\n\n🔴 {comment_post_title}\n🕵️‍♂️{comment_author}\n📝"{formatted_comment_text}"\n\n🌐{comment_post_url}'

    t_len = f'{title}\n\n🔴 {comment_post_title}\n🕵️‍♂️ {comment_author}\n📝 \n\n🌐 https://www.reddit.com{comment_url}'
    formatted_comment_text = format_description_text(comment_text, len(t_len))
    text = f'{title}\n\n🔴 {comment_post_title}\n🕵️‍♂️ {comment_author}\n📝 {formatted_comment_text}\n\n🌐 https://www.reddit.com{comment_url}'

    return text

def check_if_tweeted(comment_id):
    t = False
    with open(file_path) as f:
        for line in f:
            if line.strip() == comment_id:
                print(
                    f'Comment with the id "{comment_id}" already tweeted... ')
                t = True
                break
    return t


def write_comment_id(comment_id):
    with open(file_path, "a") as file:
        file.write(comment_id + '\n')

    return print(f'Comment_id "{comment_id}" successfully written... ')


def filter_comments_to_tweet(comments):
    print(len(comments))
    for comment in comments:
        tweeted = check_if_tweeted(comment['id'])
        if tweeted:
            continue
        else:
            write_comment_id(comment['id'])
            text = format_comment(comment)
            print(text)
            tweet(text)        
    print('Done...................................###################################', now())
