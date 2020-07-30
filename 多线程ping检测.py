import time
from subprocess import PIPE,Popen
import thread


def ping_check(ip):
    check = Popen(['/bin/bash','-c','ping -c 2 ' + ip],stdin=PIPE,stdout=PIPE)
    data = check.stdout.read()
    if 'ttl' in data:
        print '%s is UP'%ip

def main():
    for i in range(1,255):
        ip = '106.42.25.'+str(i)
        thread.start_new_thread(ping_check,(ip,))
        time.sleep(0.1)

if __name__ == "__main__":
    main()


# ping_check(ip)
