import urllib.parse
from datetime import datetime, timedelta

import json
import logging
import requests
import time

############################################################################################################
pin_codes = [560037, 560048, 560066, 560077, 560067]  # Pin codes you would want to search for
vaccine = ["covaxin", "covishield"]  # Vaccine name(s) you are looking for
telegramToken = ""  # Telegram HTTP API token for Bot
chat_id = ""  # Telegram chat ID of the group including the '-'
days = 10  # No of days from today you want the data for
sleep_time = 1000  # Message interval in seconds
############################################################################################################

logging.basicConfig(filename="Vaccine_availability.log", filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def run_cowin_api(url):
    r = requests.get(url, headers={"Accept": "application/json", "Accept-Language": "hi_IN"})
    return r.text


def send_telegram_msg(msg):
    msg_txt = "\n".join(msg)
    telegram_url = "https://api.telegram.org/bot" + telegramToken + "/sendMessage?chat_id=" + chat_id + '&text=' + urllib.parse.quote(
        msg_txt)
    r = requests.get(telegram_url)


logging.info("Script Started...")

while True:
    now = datetime.now()
    message = []
    for day in range(days):
        date = (now + timedelta(days=day)).strftime("%d-%m-%Y")
        message.append("############# " + date + " ############ ")
        for pin in pin_codes:
            base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=" + str(
                pin) + "&date=" + str(date)
            resp = json.loads(run_cowin_api(base_url))
            if len(resp["sessions"]) == 0:
                continue
            message.append("----" + str(pin) + "----")
            for sess in resp["sessions"]:
                if str(sess["vaccine"]).lower() in vaccine:
                    message.append("Name : " + sess["name"])
                    message.append("Paid : " + sess["fee_type"] + " ; " + sess["fee"])
                    message.append("Vaccine : " + sess["vaccine"])
                    message.append("Available : " + str(sess["available_capacity"]))
                    message.append("Min Age :" + str(sess["min_age_limit"]))
                    slot_available = []
                    for slots in sess["slots"]:
                        slot_available.append(slots)
                    message.append("Slots : " + "; ".join(slot_available))
                    message.append("\n")

    logging.info("Sending Telegram Message...")
    send_telegram_msg(message)

    logging.debug("Sleep for " + str(sleep_time) + " secs ...")
    time.sleep(sleep_time)
