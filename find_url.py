#Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import re


#Hàm tìm các URL dựa trên URL gốc
#Kết quả là một tập hợp các URL
def find_url(url, start_url):
    url_list = set()
    link = requests.get(url)
    link_soup = BeautifulSoup(link.text, 'html.parser')
    content = link_soup('a', attrs={'href': True})
    for i in content:
        a = i['href']
        th1 = '^{url_goc}.*(html|epi)'
        th2 = '^/.*(html|epi)'
        if re.match(th1, a):
            url_list.add(a)
        else:
            if re.match(th2, a):
                b = f'{start_url}{a}'
                url_list.add(b)
    return url_list


#Tiếp tục tìm thêm URL cho đến khi đủ yêu cầu
def find_next_url(queue, start_url, max):
    history = queue
    while (len(queue) > 0) and (len(history) < max):
        url_list = find_url(queue.pop(), start_url)
        queue = queue | (url_list - history)
        history = history | url_list
    return history
