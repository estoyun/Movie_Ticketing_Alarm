# Requests, bs4 module for crawling
import requests
from bs4 import BeautifulSoup

# 김해 cgv 상영시간표
# Date Query String 수정해서 날짜 지정 가능
url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=05,204&theatercode=0028&date=20200707'
html = requests.get(url)
print(html.text)