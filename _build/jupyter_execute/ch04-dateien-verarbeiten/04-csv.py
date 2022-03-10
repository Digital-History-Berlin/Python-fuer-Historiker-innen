#!/usr/bin/env python
# coding: utf-8

# # CSV
# 
# ## Allgemeines
# 
# Ein weiteres Format zur strukturierten Speicherung von Daten, mit dem Sie als Historiker:innen oft zu tun haben, ist CSV (Comma Separated Values). Es dient der textbasierten Speicherung von Tabellen. Sicher sind Sie mit Exceldateien vertraut. "xls" ist jedoch ein proprietäres Format -- CSV-Daten sind wesentlich interoperabler. Wie folgendes Beispiel zeigt, sind CSVs so strukturiert, dass eine Tabellen*zeile* durch eine Zeile dargestellt wird. Tabellen*spalten* sind dagegen durch ein Trennzeichen getrennt.
# 
# **Darstellung als Tabelle**
# 
# | ID | Titel | Autor | Erscheinungsjahr |
# |:---|-------|-------|-----------------:|
# | 1 | Der Prozess | Franz Kafka  | 1935 |
# | 2 | Half of a Yellow Sun | Chimanda Ngozi Adichie  | 2006 |
# | 3 | Network Effect | Martha Wells  | 2020 |
# 
# **Darstellung als CSV**
# ```
# ID;Titel;Autor;Erscheinungsjahr
# 1;Der Prozess;Franz Kafka;1935
# 2;Half of a Yellow Sun;Chimanda Ngozi Adichie;2006
# 3;Network Effect;Martha Wells;2020
# ```
# (aus der Datei: data/books.csv)
# 
# 
# Als Trennzeichen werden meist Kommata verwendet, sehr oft aber auch Semikolons. Der Grund dafür liegt in der unterschiedlichen Notation von Kommazahlen im deutsch- und englischsprachigen Raum (Deutsch: 4,2 / Englisch: 4.2). Das Komma in einer Zahl würde dann als Trennzeichen erkannt werden; 4,2 würde nicht mehr als einzelne Zahl sondern als zwei Spalten mit den Zahlen 4 und 2 interpretiert werden. Letztlich kann bei CSV jedes beliebige Zeichen als Trennzeichen verwendet werden; meist haben Sie mit ";" die wenigsten Probleme.
# 
# Sie können CSV-Dateien in allen gängigen Tabellenkalkulationsprogrammen (z.B. Microsoft Excel) öffnen und bearbeiten oder auch aus solchen Programmen CSVs exportieren.

# ## CSVs in Python öffnen und speichern
# 
# Ähnlich wie für JSON gibt es auch für CSVs Python-Programmbibliotheken, mit denen Sie Daten auslesen und neue CSV-Dateien erstellen können. In dieser Einheit besprechen wir nur die [Standardbibliothek](https://docs.python.org/3/library/csv.html) von Python. Wie schon im vorherigen Abschnitt muss diese zuerst importiert werden.

# In[ ]:


import csv


# Mit dem folgenden Code können wir den Inhalt einer CSV-Datei auslesen:

# In[ ]:


with open("../data/books.csv", "r") as csv_file:
    books_reader = csv.reader(csv_file, delimiter = ";")

    for row in books_reader:
        print(row)


# Die Funktion `reader()` funktioniert ähnlich wie `readlines()`: Die Datei wird Zeile für Zeile ausgelesen; die einzelnen Zeilen können dann weiterverarbeitet werden. Wichtig ist hier der Paramter `delimiter`. Hier geben Sie an, welches Trennzeichen die CSV-Datei, die Sie öffnen wollen, verwendet. Wenn Sie mit fremden Daten arbeiten, öffnen Sie die CSV-Datei einfach kurz in einem Texteditor um herauszufinden, was Sie hier angeben müssen.
# 
# Wie Sie sehen, werden in diesem Fall die Zeilen als Listen ausgegeben, sodass Sie auf die einzelnen Zellen der Tabelle zugreifen können:

# In[ ]:


with open("../data/books.csv", "r") as csv_file:
    books_reader = csv.reader(csv_file, delimiter = ";")

    for row in books_reader:
        print(f"Buch-ID: {row[0]}")
        print(f"Titel: {row[1]}")
        print(f"Autor: {row[2]}")
        print(f"Erscheinungsjahr: {row[3]}")
        print("---")


# Wenn Sie den Header nicht berücksichtigen wollen, können Sie ihn z.B. mit `next()` überspringen:

# In[ ]:


with open("../data/books.csv", "r") as csv_file:
    books_reader = csv.reader(csv_file, delimiter = ";")

    next(books_reader)

    for row in books_reader:
        print(f"Buch-ID: {row[0]}")
        print(f"Titel: {row[1]}")
        print(f"Autor: {row[2]}")
        print(f"Erscheinungsjahr: {row[3]}")
        print("---")


# Das Schreiben neuer CSV-Dateien funktioniert ebenfalls Zeile für Zeile. Hierbei müssen Sie für jede Zeile eine Liste erstellen, die Sie mit der Funktion `writerow()` zu einem neuen Dateiobjekt hinzufügen können. Bei Windows-Rechner müssen Sie beim Öffnen der Datei den Parameter newline auf einen leeren String ("") setzen, sonst wir nach jeder Zeile eine Leerzeile geschrieben.

# In[ ]:


with open("../data/more_books.csv", "w", newline="") as csv_file:
    books_writer = csv.writer(csv_file, delimiter = ",")

    header = ['ID', ' Titel', ' Autor', ' Erscheinungsjahr']
    books_writer.writerow(header)

    book_id = 1
    new_title = "Die Pest"
    new_author = "Albert Camus"
    new_year = "1947"
    new_book = [book_id, new_title, new_author, new_year]

    books_writer.writerow(new_book)

    book_id = book_id + 1
    new_book = [book_id, "The Hobbit", "John Ronald Reuel Tolkien", "1937"]

    books_writer.writerow(new_book)


# Schauen Sie wieder im Ordner "data" nach: Finden Sie die Datei "more_books.csv" und enthält sie die gewünschten Informationen?

# ## DictReader: Eine Alternative zum Lesen und Erstellen von CSVs
# Neben dieser Methode zum Bearbeiten von CSV-Dateien stellt die Python-Bibliothek noch die Möglichkeit bereit, CSVs als Dictionaries zu öffnen. Dies kann hilfreich sein, wenn Ihnen die genaue Position der Zellen nicht bekannt ist und Sie stattdessen mit den *Namen* der Spalten arbeiten möchten. Das Auslesen funktioniert dabei ähnlich wie oben:

# In[ ]:


with open("../data/books.csv", "r") as csv_file:
    books_reader = csv.DictReader(csv_file, delimiter = ";")

    for row in books_reader:
        print(row['Titel'])
        print(row['Erscheinungsjahr'])


# Ebenso können Sie neue CSVs erstellen. Hier gehen Sie so vor, dass Sie für jede Tabellenzeile ein eigenes Dictionary vorbereiten. Wichtig ist dabei, dass Sie die Kopfzeile der Tabelle (die ja die Spaltennamen enthält) vorher in einer Liste definieren und dem DictWriter-Objekt als Parameter übergeben.

# In[ ]:


with open("../data/more_books.csv", "w", newline="") as csv_file:
    header = ["ID",
            "Titel",
            "Autor",
            "Erscheinungsjahr",
            "verfügbar"]
    books_writer = csv.DictWriter(csv_file, fieldnames = header)
    books_writer.writeheader()

    more_input = True
    book_id = 1

    while(more_input == True):
        title = input("Geben Sie einen Titel ein: ")
        author = input("Geben Sie eine Autor*in ein: ")
        year = input("Geben Sie ein Erscheinungsjahr ein: ")
        available = input("Ist das Buch verfügbar? (ja|nein) ")
        more_input_answer = input("Möchten Sie weitere Titel eingeben? (j|n) ")

        new_book = {"ID": book_id,
            "Titel": title,
            "Autor": author,
            "Erscheinungsjahr": year,
            "verfügbar": available}

        books_writer.writerow(new_book)
        book_id = book_id + 1

        if more_input_answer == "n":
            more_input = False


# Neben der von Python bereitgestellten csv-Bibliothek, die wir hier behandelt haben, gibt es noch weitere Möglichkeiten der Verarbeitung. Eine ebenfalls viel genutzte Bibliothek ist z.B. [Pandas](https://pandas.pydata.org/). Diese ist zwar sehr mächtig, jedoch auch wesentlich komplexer als die hier vorgestellten Ansätze. Sie wird vor allem zur Datenanalyse verwendet. In vielen Fällen wird es ausreichen, auf die Bibliothek `csv` zurückzugreifen. Sollten Sie jedoch häufiger mit CSV-Dateien arbeiten und die Inhalte analysieren wollen, ist es gegebenenfalls empfehlenswert, sich Pandas einmal näher anzusehen.

# ## Aufgabe: Daten strukturiert speichern
# Nun haben Sie gelernt Daten zu strukturieren und dauerhaft verfügbar zu halten. In dieser Aufgabe sollen Sie den Programmcode aus dem [vorherigen Kapitel](aufgabe-einfache-frequenzanalyse-mit-python) nachnutzen nachnutzen. Falls Sie diese Aufgaben in der letzten Einheit nicht lösen konnten, können Sie den Code aus der Musterlösung verwenden. Passen Sie das Programm wie folgt an:
# * Der zu verarbeitende Text soll dem Programm nun nicht mehr als Variable übergeben werden, sondern aus einer Textdatei extrahiert werden.
# * Die Ausgabe soll nun nicht mehr mit `print()`, sondern als CSV-Datei erfolgen. Anstatt eines Zeilenumbruchs, soll jede Zeile nun in einer eigenen Tabellenzeile gespeichert werden. Jede Tabellenzeile soll dabei auf folgende Weise strukturiert sein:
# 
# | id | text | anzahl_zeichen|
# |:---|------|--------------:|
# |    |      |               |
# 
# `id` entspricht dabei der Nummerierung der einzelnen Zeilen des von Ihnen in der Aufgabe verwendeten Textes. Die Zeilennummerierung müssen Sie hier noch ergänzen. `text` enthält die aus maximal zehn Wörtern bestehende tokenisierte Zeile. `anzahl_zeichen` soll die Anzahl der Buchstaben in der jeweiligen Zeile enthalten.
# 
# Führen Sie das Programm für mindestens einen Text Ihrer Wahl aus.

# In[ ]:


import csv

# Ihr Code

