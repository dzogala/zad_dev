Niestety nie umiałem sobie poradzić z przesłaniem zlecenia bez przeładowania strony (udało mi się to przy formularzu stworzonym w PHP, jednak tutaj nie potrafiłem tego zaimplementować). Nie udało mi się także wykorzystać formatu JSON w komunikacji serwer - GUI.
Archiwizację, zrobiłem na miarę swoich umiejętności a więc trochę inaczej niż jest to opisane w teście.Mianowicie po kliknięciu na "Archiwizuj", przycisk znika i pojawia się komunikat "Trwa archiwizacja". Po chwili cały wiersz znika i pojawia się w zarchiwizowanych.

Aplikacja działa na frameworku Flask, a więc należy go zainstalować, Zainstalowałem również virtualenv.
Wersja Pythona, na której pracowałem to 2.7.3.

W pliku url_app.py w linii 7 należy ustawić ścieżkę, gdzie ma być utworzona baza danych.

Co aplikacja robi (z punktu widzenia użytkownika)?
	1. Wyświetla na ekranie numer, link oraz opis i przycisk Archiwizuj
	2. Po kliknięciu na przycisk Archiwizuj:
		a). Przycisk znika, pojawia się napis "Trwa archiwizacja..."
		b). Po chwili cały wiersz znika
		d). Wiersz, który zniknął z "Listy linków" pojawia się w "Zarchiwizowanych linkach"

Co aplikacja robi (z punktu widzenia programisty)?
	1. Na podstawie url_schema.db zostaje "utworzona" baza danych url.db
		a). tabela urls [id, url_link, url_name] jest uzupełniona kilkoma rekordami 
		b). tabela urls_arch  [id_arch, url_link_arch, url_name_arch] jest pusta 	
	2. GUI wyświetla na ekranie trójki z urls i/lub urls_arch
	3. Po kliknięciu Archiwizuj wstawiamy dane do tabeli urls_arch (z urls) jednocześnie usuwając je z tabeli urls. 
Użytkownik, może użyć przycisku tylko raz ponieważ po naciśnięciu nie ma możliwości powtórnego kliknięcia (przycisk, a po chwili cały wiersz znika).