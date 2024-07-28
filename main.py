from bs4 import BeautifulSoup
import requests
import yt_dlp
import os
#"https://www.cda.pl/SzowskiCDA/folder/62663177" - tak powinien wyglądać link.
url = input("URL >> ")
def get_tytul(url): # funkcja, która odpowiada za zgarnięcie tytułu folderu
    titles = []
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    span_elements = soup.find_all("span", class_="folder-one-line")
    for span in span_elements:
        a_tag = span.find("a")
        if a_tag:
            title = a_tag.text.strip()
            titles.append(title)
    return titles 
def get_link(url): # ta funkcja odpowiada za zgarnięcie wszystkich filmów w folderze CDA, wraz z tytułami.
    links = {}
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all("a", class_="link-title-visit")
    for element in elements:
        text = element.text.strip()
        href = element.get("href") 
        link = f"https://www.cda.pl{href}"
        links[link] = text
    return links
def pobierz(url, sciezka): # funkcja dla biblioteki ydl, która pobiera film ze strony, z jak najlepszą możliwą jakością.
    ydl_opts = {
        'format': 'best', 
        'outtmpl': sciezka
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
# wszystko zaczyna się dziać tutaj!

tytul = get_tytul(url)[1] # do stringa "tytul" przypisuje wartość, którą zwraca funkcja get_titles() (zwraca listę więc biorę drugi element z listy).
os.mkdir(tytul) # tworzę folder, który nosi nazwę folderu CDA
for link, title in get_link(url).items(): # w pętli for z funkcji get_link(), która zwraca dictionary biorę link wraz z tytułem. 
    sciezka = f"{tytul}\\{title}.mp4" 
    pobierz(link, sciezka) # pobieranie filmu
