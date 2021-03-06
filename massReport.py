
from colored import fg
import requests
import threading
import time
import random

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def start():
    token = input(f"\n {r2}[{b}?{r2}] Token: ")
    guildId = input(f" {r2}[{b}?{r2}] Server ID: ")
    channelId = input(f" {r2}[{b}?{r2}] Channel ID: ")
    messageId = input(f" {r2}[{b}?{r2}] Message ID: ")
    reason = input(f" {r2}[{b}?{r2}] Reason: ")

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : token,
        "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
    }

    payload = {"guild_id" : guildId, "channel_id" : channelId, "message_id" : messageId, "reason" : reason}

    def report():
        while True:
            response = requests.post(
                'https://discord.com/api/v6/report',
                headers = headers,
                json = payload
            )
            if response.status_code == 201:
                print(f" {r2}[{b}+{r2}] Report sent successfully")
            elif response.status_code == 429:
                print(f" {r2}[{b}!{r2}] Rate Limited, waiting 5 seconds")
                time.sleep(5)
            elif response.status_code == 401:
                print(f" {r2}[{b}!{r2}] Invalid Token")
                return
            else:
                print(f" {r2}[{b}!{r2}] Unknown Error: {response.status_code}")

    for i in range(500):
        threading.Thread(target = report).start()

if __name__ == '__main__':
    start()