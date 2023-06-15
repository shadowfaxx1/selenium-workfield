import requests
from bs4 import BeautifulSoup
import random
import time
import re

def rotate_proxy():
    proxy_list = [
        
        '178.32.116.232:57123',
        '109.75.34.152:59341',
        '176.126.136.74:5678',
        # Add more proxy IPs if available
    ]
    return random.choice(proxy_list)

def scrape_twitter_profile(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}


    proxy = rotate_proxy()
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }

    try:
        response = requests.get(url, headers=headers, proxies=proxies ,verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Error occurred:', e)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    profile_data = {}

    profile_data['biography'] = soup.find('div', {'class': 'ProfileHeaderCard-bio'}).text.strip()
    profile_data['followers_count'] = int(soup.find('a', {'href': '/followers'}).find('span', {'class': 'ProfileNav-value'}).text.replace(',', ''))
    profile_data['following_count'] = int(soup.find('a', {'href': '/following'}).find('span', {'class': 'ProfileNav-value'}).text.replace(',', ''))
    profile_data['likes_count'] = int(soup.find('a', {'href': '/likes'}).find('span', {'class': 'ProfileNav-value'}).text.replace(',', ''))
    profile_data['user_id'] = int(re.search(r'data-user-id="(\d+)"', response.text).group(1))

    return profile_data


profile_url = 'https://twitter.com/sachin_rt'
scraped_data = scrape_twitter_profile(profile_url)

if scraped_data:
    print(scraped_data)
