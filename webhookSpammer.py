from colored import fg
import requests
import time

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def spammer():
    webhook = input(f"\n {r2}[{b}?{r2}] Webhook URL: ")
    message = input(f" {r2}[{b}?{r2}] Message: ")
    timer = input(f" {r2}[{b}?{r2}] Amount of time between attack(s): ")
    print("")

    timeout = time.time() + 1 * float(timer) + 2

    while time.time() < timeout:
        response = requests.post( # Send the webhook message
            webhook,
            json = {"content" : message},
            params = {'wait' : True}
        )

        if response.status_code == 204 or response.status_code == 200:
            print(f" {r2}[{b}+{r2}] Message Sent")
        elif response.status_code == 429:
            print(f" {r2}[{b}-{r2}] Rate Limited ({response.json()['retry_after']}ms)")
            time.sleep(response.json()["retry_after"] / 1000)
        else:
            print(f" {r2}[{b}-{r2}] Error Code: {response.status_code}")

        time.sleep(.5)