import requests
import re
from bs4 import BeautifulSoup


def scrape_covid():
    print("[전국 코로나 현황]")
    url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    total_positive = soup.find("dd", attrs={"class":"ca_value"}).get_text()
    total_recovery = soup.find("table", attrs={"class":"num minisize"}).find("tbody").find("td")
    print(total_positive) #총 확진자
    print(total_recovery.next_sibling.next_sibling.get_text()) #격리해제 (총완치자)
    print("--------------------")
def scrape_covid_g():
    print("[경산 코로나현황]")
    url = "https://www.gbgs.go.kr/programs/corona/corona.do"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    

    Gyeongsan_total_positive = soup.find("table", attrs={"class":"table01"}).find("tbody").find("td").get_text()
    Gyeongsan_recovery = soup.find("table", attrs={"class":"table01"}).find("tbody").find("td")
    Gyeongsan_today_positive = soup.find("table", attrs={"class":"table01"}).find("tbody").find("tr")

    
    print(Gyeongsan_total_positive) #경산 확진자
    print(Gyeongsan_recovery.next_sibling.next_sibling.next_sibling.next_sibling.get_text()) #경산 완치자
    print(Gyeongsan_today_positive.next_sibling.next_sibling.find("td").get_text())  #경산 금일 확진자
    


 

if __name__ == "__main__":

    scrape_covid()
    scrape_covid_g()
    # 다른파일에 의해 호출될땐 실행 X