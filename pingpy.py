import os
import sys
ips = ["usny2-cn.sslwonders.com", "uswdc2-cn.sslwonders.com", "usla2-cn.sslwonders.com", "usut2-cn.sslwonders.com", "ussf2-cn.sslwonders.com", "us2-cn.sslwonders.com", "ukman2-cn.sslwonders.com", "ukl2-cn.sslwonders.com", "ukm2-cn.sslwonders.com", "cato2-cn.sslwonders.com",
       "nl2-cn.sslwonders.com", "se2-cn.sslwonders.com", "ch2-cn.sslwonders.com", "my2-cn.sslwonders.com", "sg2-cn.sslwonders.com", "lu2-cn.sslwonders.com", "au2-cn.sslwonders.com", "fr2-cn.sslwonders.com", "hk2-cn.sslwonders.com", "it2-cn.sslwonders.com", "be2-cn.sslwonders.com", "in2-cn.sslwonders.com"]
iplist = list()
ipbest = ["us2", "ch2", "lu2", "ussf2", "my2", "sg2", "in2", "fr2"]
for i in range(len(ipbest)):
    ipbest[i] = ipbest[i] + "-cn.sslwonders.com"

#ip = '192.168.1.11'
# ip = '172.24.186.191'
# 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒
for ip in ipbest[:]:
    backinfo = os.system('ping -c 40 -W 1 %s' % ip)
    if backinfo:
        print('no')
    else:
        iplist.append(ip)
# print(iplist)
