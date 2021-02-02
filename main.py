import find_url
import save_url


start_url = input('Cho xin cái địa chỉ: ')
max = int(input('Số trang: '))
url_list = find_url.find_url(start_url, start_url)
history = find_url.find_next_url(url_list, start_url, max)
save_url.new_folder(input('Folder name: '))
save_url.save_all_file(history, max)