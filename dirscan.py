import requests
import socket
import threading
import time

# usage = 'example：python -u http://www.xxx.com'  #提示信息
# parse = OptionParser(usage)             #调用提示信息
# parse.add_option('-u',dest='url',type='string',help="-u对应目标URL")      #增加-u参数，，定义str型，help对应帮助信息

# (options,args) = parse.parse_args()      #调用
# if options.ip == None:                  #如果未输入-u参数，提示上述的提示信息
#     print(parse.usage)
#     sys.exit(0)



def scan_dir():
    url = "https://www.xingtai123.com/"
    headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.360"
            }
    e =  open("E:\\vlc\\dic.txt",'r')
    for line in e:
        line = e.readline()
        # print(line)
        url2 = str(url)+str(line)
        # print(url2)
        res = requests.get(url=url2,headers=headers,timeout=3)
        time.sleep(0.5)
        code = res.status_code
        # print(code)
        if code == 200 or code == 403:
            with open("e:\\dir.txt",'a+') as d:
                d.writelines(url2+'\n')
                print('\033[1;35;46m [+++] \033[0m',url2,'    ',code,'\033[1;35;46m 目录存在 \033[0m')
        else:
            print("[---]","目录不存在      响应码",code)
            
            

def main():
    thread = []

    for i in range(1,2):
        t = threading.Thread(target=scan_dir)
        thread.append(t)
        t.start()

# scan_dir()       
if __name__ == "__main__":
    main()