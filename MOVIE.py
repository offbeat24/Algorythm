import urllib.request
import requests
import urllib.request as ul
import json


def weather(city):
    # city = "Busan"
    apikey = "a5f1fec9cece152a8e70ac30e51e900e"
    lang = "kr"
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
    response = requests.get(api)
    data = json.loads(response.text)
    temperature = data["main"]["temp"]
    return temperature


def movie(movieDate):
    # movieDate = "20230925"  #2023년 09월 25일 박스오피스 / 당일은 요청이 안됨 20230926(x)
    url = (
        f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=96683d574bf5ac1e5b63d50a44a4fb3a&targetDt=%s"
        % movieDate
    )
    request = ul.Request(url)
    response = ul.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        responseData = response.read()
    result = json.loads(responseData)
    rank = ""
    for i in range(10):
        rank += "{}위 : {}\n".format(
            i + 1, result["boxOfficeResult"]["dailyBoxOfficeList"][i]["movieNm"]
        )
    return rank


def output(keyword):  # 결과 출력하는 함수 작성
    ans = ""
    if (keyword == "Seoul") or (keyword == "Busan"):
        ans = weather(keyword)
    else:
        ans = movie(keyword)
    print(ans)


choice_input = input("1. 날씨정보   /   2. 영화정보 \n")
if choice_input == "1":
    choice_city = input("Seoul or Busan \n")

    output(choice_city)  # Seoul을 입력하면 서울 날씨,  Busan 이라고 입력하면 부산 날씨 출력

if choice_input == "2":
    choice_date = input("날짜 입력 \n")

    output(choice_date)  # 해당 날짜의 박스오피스 1~10 순위 출력
