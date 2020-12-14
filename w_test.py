import requests
from bs4 import BeautifulSoup


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%98%EC%96%91%EC%9D%8D+%EB%82%A0%EC%94%A8&oquery=%ED%95%98%EC%96%91%EC%9D%8D+%EB%82%A0%EC%8B%9C&tqi=UINIflprvhGss6ygbBNssssssQ4-118715"
    res = requests.get(url)
    res.raise_for_status() #문제 발생 시 종료
    soup = BeautifulSoup(res.text, "lxml")
    # cast = soup.find("p", attrs={"class":"cast_txt"}).get_text() #맑음, 어제보다 0도 높/낮아요

    curr_temp = soup.find("span", attrs={"class":"todaytemp"}).get_text().replace("도씨", "") #현재온도
    min_temp = soup.find("span", attrs={"class":"num"}).get_text() #최저 온도 
    max_temp = soup.find("span", attrs={"class":"num"}).get_text() #최고온도

    # morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip() #오전강수확률
    # afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip() #오후강수확률

    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("span")[0].get_text().replace("㎍/㎥","")#미세먼지
    pm25 = dust.find_all("span")[2].get_text().replace("㎍/㎥","")

    #출력
    # print(cast)
    print("{} ( {} /  {})".format(curr_temp, min_temp, max_temp)) #현재 , 최저, 최고
    # print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))

    print("{}".format(pm10)) #미세먼지
    print("{}".format(pm25)) #초미세먼지
    print()


if __name__ == "__main__":
    
    scrape_weather() # 다른파일에 의해 호출될땐 실행 X