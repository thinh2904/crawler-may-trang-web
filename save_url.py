# Các thư viện cần thiết
import os
import requests
import codecs


#Hàm tạo tên thư mục để lưu file
def new_folder(name):
    os.mkdir(name)
    os.chdir(name)


#Hàm để lưu 1 file
def save_1_file(url, stt):
    file = codecs.open('link' + str(stt) + '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()


#Dựa vào hàm lưu 1 file để lưu tất cả các file
def save_all_file(history, max):
    for (stt, url_set) in enumerate(history):
        if stt >= max:
            break
        save_1_file(url_set, max)
        print(f'{stt} {url_set}')
