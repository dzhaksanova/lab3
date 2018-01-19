from bs4 import BeautifulSoup
import requests



html = requests.get("https://www.tomsk.kp.ru/").text
soup = BeautifulSoup(html, "html.parser")
kek = []
for i in soup.find_all("div", "txt"):
    title = []
    desc = []

    for titles in i.find_all("div", "digestTitle"):
        title = titles.get_text()
    for descr in i.find_all("div", "digestDesc"):
        desc = descr.get_text()
    if title:
        kek.append({"Title:": title, "Annotation:": desc})
print(kek)

















