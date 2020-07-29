################
#扫描端口的小工具，某些特定情况不能带有nmap特征
###############
import socket
from optparse import OptionParser


def port_scan():
    #定义端口字典
    openfile = open("e:\\端口扫描.txt",'a+')
    portlist = [21,22,23,25,53,53,80,81,110,111,123,123,135,137,139,161,389,443,445,465,500,515,520,523,548,623,636,873,902,1080,1099,1433,1521,1604,1645,1701,1883,1900,2049,2181,2375,2379,2425,3128,3306,3389,4730,5060,5222,5351,5353,5432,5555,5601,5672,5683,5900,5938,5984,6000,6379,7001,7077,8080,8081,8443,8545,8686,9000,9042,9092,9100,9200,9418,9999,11211,27017,37777,50000,50070,61616]

    for port in portlist:      #端口在字典循环并与输入的ip拼接查询并输出
        try:
            usage = 'example：python -i 127.0.0.1'  #提示信息
            parse = OptionParser(usage)             #调用提示信息
            parse.add_option('-i',dest='ip',type='string',help="-i对应目标IP")      #增加-i参数，，定义str型，help对应帮助信息

            (options,args) = parse.parse_args()      #调用
            if options.ip == None:                  #如果未输入-i参数，提示上述的提示信息
                print(parse.usage)
                sys.exit(0)                         #正常退出
            else:
                ip = options.ip                     #给输入的ip定义
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #socket模块，IPV4，发送tcp请求
                s.settimeout(0.5)                   #设置超时时间0.05s
                code = s.connect_ex((str(ip),port)) #探测端口存活，端口存在即响应0
    
                if code == 0:                          #响应0打印ip+端口信息并提示存在
                    outtext = ("[+]" + ip + "   " + str(port) + "    " + "is open")
                    print(outtext)
                    openfile.writelines(outtext)
                else:                                   #其他情况就跳过，不打印不存在的端口信息
                    pass
                
        except Exception as e :
            print(e)
    openfile.close()
port_scan() #调用函数

