import requests
import time
from bs4 import BeautifulSoup

WEBHOOK_URL = "https://discord.com/api/webhooks/1500550335951802398/knhIQkVOj2B39_CQsrt49CT4WjTkNM3EaeATzOP2W5JMNd_xVh2N000qUejUOSyfUKDw"
USERNAME = "SrDAvincciYT"

last_tweet = ""

headers = {
    "User-Agent": "Mozilla/5.0"
}

while True:
    try:
        url = f"https://nitter.net/{USERNAME}"

        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code != 200:
            print("Error cargando Nitter:", r.status_code)
            time.sleep(300)
            continue

        soup = BeautifulSoup(r.text, "html.parser")

        tweets = soup.select(".timeline-item")

        if not tweets:
            print("No se encontraron tweets")
            time.sleep(300)
            continue

        first_tweet = tweets[0]

        tweet_text = first_tweet.select_one(".tweet-content").text.strip()

        tweet_link = first_tweet.select_one("a.tweet-link")["href"]

        full_link = f"https://nitter.net{tweet_link}"

        if tweet_text != last_tweet:

            data = {
                "content": (
                    f"🕊 Nuevo tweet de @{USERNAME}\n"
                    f"{full_link}"
                )
            }

            requests.post(WEBHOOK_URL, json=data)

            print("Nuevo tweet enviado")

            last_tweet = tweet_text

        else:
            print("Sin cambios")

        time.sleep(300)

    except Exception as e:
        print("Error:", e)
        time.sleep(300)