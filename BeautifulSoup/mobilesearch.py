from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://gadgets.ndtv.com/mobiles/smartphones').text
soup = BeautifulSoup(html_text, 'lxml')
mobiles = soup.find_all('div', class_="_lpdwgt _flx")
for mobile in mobiles:
    mobile1 = mobile.find('div', class_ = "_lpdscn")
    mobile_name = mobile1.find('h3', class_ = "_hd").text
    mobile2 = mobile1.find('div', class_ = "_lrtngbuy _flx")
    mobile3 = mobile2.find('div', class_ = "_lpbuy _flx")
    mobile_price = mobile3.find('a', class_ = "_lprc").span.text
    mobile_link = mobile1.find('h3', class_ = "_hd").a['href']
    print(f'''
    Mobile Name: {mobile_name}
    Mobile Price: {mobile_price}
    Mobile Link: {mobile_link}
    ''')
