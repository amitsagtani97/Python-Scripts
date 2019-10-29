#!/usr/bin/python
"""
Python function to dynamically wait between requests calls
"""
#imports
import time
from random import randint, sample, choice
import requests

USER_AGENTS = [
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
]

def random_user_agent(user_agents):
    """(dict) -> str

    Takes in a dict of user_agents and returns one at random."""
    new_user_agent = choice(user_agents)
    return new_user_agent

def response_delay(t1):
    """(int) -> int

    Gets the response delay, based on the randomized wait times you provide and the websites response time.
    As of right now, we have the wait times set to wait ~7-8 seconds on average, and if the website responds in under 7 seconds,
    then wait ~5 seconds more. These numbers can be easily changed."""
    response_time = time.time() - t1
    wait_time = randint(5, 10) - response_time
    time.sleep(wait_time if wait_time > 7 else randint(3, 7))


def fetch_urls(urls):
    """(list) -> dict
    
    Fetches the fed in list of urls and applies the proper user_agents and dynamic wait time to the series of requests."""
    t0 = time.time()
    total_requests = 0
    for url in urls:
        try:
            t1 = time.time()
            response = requests.get(url, headers=random_user_agent(USER_AGENTS), timeout=60)
            response_delay(t1)
            total_requests += 1
            elapsed_time = time.time() - t0
            print(f'{total_requests}/{len(urls)}, {float(elapsed_time):.02f} requests/s')
            response = response.text  # Can do anything with this response. I usually turn it into a BeautifulSoup object before parsing the HTML.
        except Exception as e:
            print(e)

urls = ['https://google.com', 'https://cnn.com', 'https://netflix.com']
fetch_urls(urls)
