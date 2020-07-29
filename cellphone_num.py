# -*- coding: utf-8 -*-
#爬取不同地区手机号前7位，并填充后四位，生成针对不同地区的手机号字典工具


from bs4 import BeautifulSoup
import urllib.request
import re
import threading
def urlask(): #从网页爬取前七位，存到  E:\\left7.txt    
    try:
        url = "http://www.bixinshui.com/city/1"
        headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.360"
            }
        request = urllib.request.Request(url = url,headers = headers)
        response = urllib.request.urlopen(request)
        return response.read().decode("utf-8")
    except TabError as p :
        print(p)
html = urlask()
bs = BeautifulSoup(html,"lxml")
phones = bs.find_all('a')
for phone in phones:
    phone = phone.string
    print(phone)
    with open('E:\\left7.txt','a+',encoding='utf-8') as h:
        h.writelines(phone + '\n')


def xunhuan_num():     #循环and拼接
    try:
        openfile = open("E:\\left7.txt","r")
        # writefile = open("E:\\left11.txt","a+")
        #temp = []
        #hang_get = openfile.read()
        for line in openfile:
            line=line.strip('\n')
            for i in range(1,10000):
                fournum = str(("%04d" % i))
                end_num = str(line) + str(fournum)
                with open('C:\\Users\\52756\Desktop\\工作文件\\学习类\\python\\phone1.txt','a+') as f:
                    f.writelines(end_num + '\n')
                print(end_num)
                #print('endnum is',end_num)
                #writefile.write(end_num + '\n')
                #temp += end_num.strip('\n')
            if line == 1991001:
                break
        # for row in temp:
        #     writefile.write(row + '\n')
    #    with open("E:\\left11.txt", mode="w") as f:
    #        f.write(line + fournum)        
        openfile.close()
        # writefile.close()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    
    threads = []
    threads_count = 20
    #创建线程对象

    for i in range(0,threads_count):
        t1 = threading.Thread(target=xunhuan_num)
        t1.start()

        threads.append(t1)
        
    for i in threads:
        t1.join()