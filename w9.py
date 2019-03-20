import re

def regEx():
    f1 = open('log.txt')
    f2 = open('log.txt')
    f3 = open('log.txt')
    f4 = open('log.txt')
    ver_list = []
    usr_list = []
    org_list = []
    date_list = []

    for line1 in f1:
        usr1 = re.findall('^Author: ([a-z]+)@*',line1)
        if len(usr1) != 1: continue
        usr2 = str(usr1[0])
        usr_list.append(usr2)
    f1.close()

    for line2 in f2:
        ver1 = re.findall('commit: ([r][0-9]+)',line2)
        if len(ver1) != 1 : continue
        ver2 = str(ver1[0])
        ver_list.append(ver2)
    f2.close()

    for line3 in f3:
        org1 = re.findall('^Author: .*@([^ ]*)',line3.rstrip('\n'))
        if len(org1) != 1 : continue
        org2 = str(org1[0])
        org_list.append(org2)
    f3.close()

    for line4 in f4:
        date1 = re.findall('^Date: (\d+\-\d+\-\d+ \d+\:\d+\:\d+)',line4)
        if len(date1) != 1 : continue
        date2 = str(date1[0])
        date_list.append(date2)
    
    for i in range(len(ver_list)):
        print('User ',usr_list[i],' committed version: ',ver_list[i])
        
    for j in range(len(ver_list)):    
        print('Version ',ver_list[j],' created by ',date_list[j])
    
    for k in range(len(ver_list)):
        print('Organization ',org_list[k],' commited version: ',ver_list[k])
# Organization aaaaa.edu committed version: r38xxx 
# From: rjlowe@iupui.edu  ‘使用者@組織名稱 ＋ 版本’

regEx()


