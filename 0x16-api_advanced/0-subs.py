#!/usr/bin/python3
'''Returns number of subscibers in a subreddit'''
import requests
import sys


def number_of_subscribers(subreddit):
    '''If not a valid subreddit, return 0'''
    url = ('https://www.reddit.com/r/{}/about.json'.format(subreddit))
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return (data['data']['subscribers'])
    else:
        return 0
