import json
import requests
import tweepy

with open('line.json') as f:
    line_json = json.load(f)

with open('twitter.json') as f:
    twitter_keys = json.load(f)


def notify_message(message):
    url = 'https://notify-api.line.me/api/notify'
    LINE_NOTIFY_TOKEN = line_json['LINE_NOTIFY_TOKEN']

    headers = {
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
    }

    data = {
        'message': message
    }

    requests.post(
        url,
        headers=headers,
        data=data)


def get_n_followers():

    consumer_key = twitter_keys['consumer_key']
    consumer_secret = twitter_keys['consumer_secret']
    access_token = twitter_keys['access_token']
    access_token_secret = twitter_keys['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    """
    https://www.geeksforgeeks.org/python-tweepy-getting-the-number-of-followers-of-a-user/
    follow_count が取得できない状態　twitter API or 内部コード調査
    """



def main():
    n_followers = get_n_followers()
    message = message = f'本日のフォロワー数は{n_followers}です。'
    notify_message(message)


if __name__ == '__main__':
    main()

