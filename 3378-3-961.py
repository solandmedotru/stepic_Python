import requests
url = "https://stepic.org/media/attachments/course67/3.6.3/699991.txt"
r = requests.get(url)

while "We" not in r.text:
    url = "https://stepic.org/media/attachments/course67/3.6.3/"+r.text
    r = requests.get(url)
    print(url)

print(r.text)