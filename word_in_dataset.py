import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

import csv


fl = open('test_dataset.csv', 'w', encoding='UTF8')

header = ['source_url', 'access_datetime', 'content', 'word']
writer = csv.writer(fl, delimiter='&')
writer.writerow(header)

urls = ['https://kun.uz/uz/news/2022/12/01/uch-tomonlama-ittifoq-tashqi-kuchlar-qolidagi-ozbek-gazi-va-volodinning-hurmatsizligi-siyosatshunoslar-bilan-suhbat', 'https://stadion.uz/uz/news/detail/359943', 'https://qalampir.uz/uz/news/2050-yilga-borib-5-milliarddan-kup-odam-suv-tank-isligiga-uchraydi-bmt-73059', 'https://daryo.uz/2022/12/02/ozbekistonda-dam-olish-kunlari-qanday-ob-havo-boladi-3/']
for url in urls:
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	page = soup.findAll('p')
	content = []
	acc_time = datetime.now().strftime("%m-%d-%Y, %H:%M")
	for pg in page:
		content.append(pg.get_text())
	words = ' '.join(content)
	word = words.split(" ")
	data = [url, acc_time, content, word]
	writer.writerow(data)



	