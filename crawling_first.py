# Requests, bs4 module for crawling
import requests
from bs4 import BeautifulSoup

# Crawling : 데이터 수집하고 분류하는 것(그냥 탐색) / Scraping : 원하는 정보를 추출하는 기술(긁어오기)
# Parsing : 데이터를 정보로 가공

# 김해 cgv 상영시간표 페이지 스크래핑
# Date Query String 수정해서 날짜 지정 가능
url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=05,204&theatercode=0028&date=20200707'
html = requests.get(url)

# 크롤링한 자료 출력
# print(html.text)

# 크롤링한 자료 파싱
# .text : "하위 자식 태그" 텍스트까지 문자열로 파싱 가능(유니코드 형식) / .string : "only 해당 태그" 하위 문자열 객체화(문자열 없으면 None 반환)
soup = BeautifulSoup(html.text, 'html.parser')

# "살아있다" 영화 제목만 뽑아오기(크롬 개발자도구로 해당 부분의 CSS Selecter 복사)
# print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong'))

# 영화 정보 전체 가져오기 (info-movie : Class)
# print(soup.select('div.info-movie'))

# 영화 정보 전체를 리스트 형태로 저장 (div class="info-movie" 기준)
title_list = soup.select('div.info-movie')

# 태그 selecting 순서 : div class > a > strong > 영화 제목
# strip() : 양쪽 공백 제거 / rstrip() : 오른쪽 공백 제거 / lstrip() : 왼쪽 공백 제거
for i in title_list:
    print(i.select_one('a > strong').text.strip())
