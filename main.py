import urllib.request
import re

def Search():
    print("entrer mot clé : ")
    query = input()
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+query)
    video = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(video)

Search()
