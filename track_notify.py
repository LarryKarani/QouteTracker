import requests

from bs4 import BeautifulSoup

from pygame import mixer

import time

url = input("Enter the url of the stock: ")

target_price = input("Enter the target price: ")

target_price = float(target_price)

mixer.init()
mixer.music.load('alarm.mp3')

while True:
	html = requests.get(url).text

	soup = BeautifulSoup(html, "html.parser")

	current_price = soup.find('span', attrs={"class": "pr"}).text

	current_price = float(current_price)

	print(current_price)

	if current_price > target_price:

		print("raeched your target price")

		mixer.music.play()
		time.sleep(15)

		break

	time.sleep(10)


 
