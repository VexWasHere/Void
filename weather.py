import requests
from bs4 import BeautifulSoup
from getloc import rt

def get_weather(city_name):
    url = f"https://www.google.com/search?q=weather+{city_name}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    temp_div = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
    if temp_div is not None:
        temp = temp_div.text
        print(f"Temperature is {temp}")
    else:
        print("Temperature not found")

    strd_div = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
    if strd_div is not None:
        strd = strd_div.text
        data = strd.split('\n')
        time = data[0]
        sky = data[1]
        print(f"Time: {time}")
        print(f"Sky Description: {sky}")
    else:
        print("Time and Sky Description not found")

    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    if len(listdiv) > 5:
        strd = listdiv[5].text
        pos = strd.find('Wind')
        other_data = strd[pos:]
        print(other_data)
    else:
        print("Other data not found")

city_name = rt
get_weather(city_name)