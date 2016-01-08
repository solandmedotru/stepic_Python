import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/050.txt')
a = 0
for i in r.text.splitlines():
    a=a+1
    print(a,i)