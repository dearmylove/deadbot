import requests
from bs4 import BeautifulSoup


def get_ihtml(url):
    _ihtml = ""
    iresp = requests.get(url)
    if iresp.status_code == 200:
        _ihtml = iresp.text
    return _ihtml

def get_image(code):
    schCode = code
    URL = ("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=" + schCode)
    ihtml = get_ihtml(URL)
    isoup = BeautifulSoup(ihtml, 'html.parser')
    ielement = isoup.find_all('div', class_='detail')
    print("########################################")
    ielement = isoup.find_all('p', class_='text _cs_fortune_text')
    ielement = str(ielement)[str(ielement).find('text">') + 6: str(ielement).find('</p>')]

    return ielement