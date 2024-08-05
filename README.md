# Pobieracz
Pobieracz Folderu CDA to bardzo przydatne narzędzie, które umożliwi pobranie zawartości folderu CDA, podając tylko link. 
# Wymagania
- pip
- Python 3.x
# Instalacja
1. pobierz skrypt
2. zainstaluj pip
   ```bash
   py -m ensurepip --upgrade
   ```
3. zaimplementuj biblioteki requests, bs4
   ```bash
   pip install requests
   pip install beautifulsoup4
   pip install yt_dlp
3. uruchom skrypt i pobieraj!
4. Pamiętaj, jeśli chcesz podać drugą/trzecią stronę folderu musisz dodać **/{strona}** na końcu odnośnika. 
# Jak to działa
W dużym uproszczeniu biblioteka bs4 najpierw znajduje tytuł folderu szukając w html-u klasy z nazwą folderu. Na witrynie szuka wszystkich klas z tytułem i odnośnikiem do filmu. Informacje te są potem przechowywane
i zaczyna się pobieranie filmów przy pomocy biblioteki **yt_dlp**, przechowane wcześniej informacje są wykorzystane, by nadać tytuł oraz link.
# Screenshoty
![obraz](https://github.com/user-attachments/assets/e0c396b4-f183-4490-a33d-9b07ce68fa53)
