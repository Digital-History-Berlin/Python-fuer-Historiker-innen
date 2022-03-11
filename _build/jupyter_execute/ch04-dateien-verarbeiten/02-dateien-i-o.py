#!/usr/bin/env python
# coding: utf-8

# # Dateien öffnen, lesen und bearbeiten
# 
# Bislang haben wir Daten in Variablen gespeichert und Ergebnisse mit `print()` ausgegeben. In der Praxis wollen wir Daten natürlich dauerhaft (persistent) speichern, später wieder bearbeiten können, oder die Daten von Dritten weiterverarbeiten lassen.

# ## Grundlagen
# Zu Beginn ein paar basale Grundlagen, die Ihnen vermutlich weitestgehend vertraut vorkommen.
# 
# Eine Datei ist identifizierbar durch ihren Namen und ihren Dateityp. Außerdem lässt sich jede Datei irgendwo in einer Verzeichnisstruktur verorten (= sie ist in einem Ordner gespeichert, der zugleich ein Unterordner eines anderen ist).
# 
# Name, Dateityp und Speicherdatei lassen sich als *Pfad* angeben. Auf Ihrem Rechner können Sie sich im Explorer/Dateimanager/Finder den Dateipfad auch einblenden lassen. Ein Beispiel: Der Dateipfad für ein Notebook kann so aussehen:
# 
# für Linux und Mac:
# ```
# /Users/username/Documents/Lehre/Python/dateien_verarbeiten.ipynb
# ```
# 
# für Windows:
# ```
# C:\Users\username\Documents\Lehre\Python\dateien_verarbeiten.ipynb
# ```
# 
# Dies ist der *absolute* Dateipfad; unabhängig davon wo ich mich auf meinem Rechner befinde, zeigt er die genaue Position von `dateien_verarbeiten.ipynb` an. Die einzelnen Verzeichnisse sind dabei immer durch Slashes (/) getrennt. Beachten Sie bitte, dass das Betriebssystem Windows hier eine Ausnahme macht; dort werden Verzeichnisse durch Backslashes (\\) voneinander getrennt (hier beginnt der Pfad außerdem mit einem Laufwerksbuchstaben).
# 
# Wenn Sie dieses Notebook auf Ihrem Rechner speichern, wird dessen Dateipfad natürlich völlig anders als in dem Beispiel aussehen. Daher ist es wichtig, so oft wie möglich mit *relativen* Pfaden zu arbeiten. Relative Pfade bezeichnen den Dateipfad ausgehend von der Position (bzw. der Position Ihres Notebooks) in der Verzeichnisstruktur. Angenommen, ein Notebook liegt im Ordner "Lehre" auf einem Rechner. Der (relative) Dateipfad zum Notebook wäre dann:
# ```
# Python/dateien_verarbeiten.ipynb
# ```
# Durch Angabe von ".." ist es möglich in einem Dateipfad einen Wechsel zu einem übergeordneten Verzeichnis anzugeben. Auf einem Rechner gibt es im Ordner "Documents" z.B. neben "Lehre" auch einen Ordner "Publikationen". Angenommen ich hätte ein Python-Skript im Ordner "Publikationen" gespeichert, das ebenfalls auf das Notebook zugreifen soll. Hier wäre der relative Dateipfad zum Notebook dann:
# ```
# ../Lehre/Python/dateien_verarbeiten.ipynb
# ```

# Beachten Sie, dass Sie Dateien, mit denen Sie in einem Notebook arbeiten wollen, an einer geeigneten Stelle in Ihrem Dateisystem abzulegen, zum Beispiel dort, wo Sie Ihre Notebooks bearbeiten, dann können Sie ganz einfach darauf zugreifen. 

# ## Dateien öffnen, lesen und schreiben
# In dieser Einführung arbeiten wir ausschließlich mit textbasierten Dateiformaten (also z.B. txt, csv, json, html, tsv, md, tex, py, ...). Diese Dateien lassen sich einfach als String auslesen, der zugleich den Inhalt der Datei repräsentiert. Komplexe Formate, wie Bilder (jpgs, png, tiff, ...), PDFs, Worddokumente, Exceldateien oder Video- und Audioformate bestehen zwar letztlich auch nur aus Zeichenketten, sind aber auf eine bestimmte Weise *codiert*. Auch solche Dateien können Sie mit Python bearbeiten; hierfür werden aber bestimmte Programmbibliotheken benötigt. Falls Sie in einem eigenen Projekt mit einem dieser Formate arbeiten wollen, finden Sie die entsprechenden Bibliotheken meist nach einer kurzen Suche im Internet.
# 
# Das Bearbeiten einer Datei beginnt immer mit der Funktion `open()`. Im folgenden Codeblock erstellen wir eine Testdatei, in der wir den ersten Satz aus Kafkas *Prozess* speichern.

# In[ ]:


first_sentence_prozess = '''Jemand musste Josef K. verleumdet haben, 
denn ohne dass er etwas Böses getan hätte, 
wurde er eines Morgens verhaftet. '''

prozess_file = open("example_data/der_prozess.txt", "w")
prozess_file.write(first_sentence_prozess)
prozess_file.close()


# Die Funktion `open()` erzeugt ein Objekt, das quasi als Schnittstelle zwischen Ihrem Programm und dem Betriebssystem fungiert. `open()` benötigt als Parameter den Namen bzw. Dateipfad der Datei sowie die Angabe in welchem Modus die Datei geöffnet werden soll. Da wir eine noch nicht existierende Datei neu beschreiben wollen, wählen wir hier "w" (write). Das File-Objekt (hier als `prozess_file` gespeichert) verfügt über verschiedene Funktionen zum Lesen und Schreiben von Dateien. Mit `write()` geben wir an, dass wir den String `first_sentence_prozess` (den wir ja in Zeile 1 definiert haben) als Inhalt der Datei speichern wollen. Mit `close()` teilen wir dem File-Objekt mit, dass wir keine Änderungen an der Datei mehr vornehmen möchten. Dieser Schritt muss immer erfolgen, wenn Sie mit Dateien arbeiten (andernfalls könnten Sie versehentlich Ressourcen Ihres Computers für das Beschreiben einer Datei binden, obwohl sie an anderer Stelle benötigt werden). Damit `close()` auch im Falle eines Fehlers ausgeführt wird, verwenden Sie am besten so oft es geht folgendes Statement:

# In[ ]:


first_sentence_prozess = '''Jemand musste Josef K. verleumdet haben, 
denn ohne dass er etwas Böses getan hätte, 
wurde er eines Morgens verhaftet. '''

with open("example_data/der_prozess.txt", "w") as prozess_file:
    prozess_file.write(first_sentence_prozess)


# Wenn Sie "w" als zweiten Parameter für `open()` verwenden, wird der Inhalt der Datei immer komplett überschrieben. Je nachdem was Sie tun möchten, müssen Sie hier den richtigen Parameter wählen. Im Ordner "example_data" sollte sich nun die Datei "der_prozess" finden. 
# 
# Um etwas an einen bestehenden Dateiinhalt anzuhängen, verwenden Sie den Parameter "a" (append).

# In[ ]:


second_sentence_prozess = '''
Die Köchin der Frau Grubach, 
seiner Zimmervermieterin, 
die ihm jeden Tag gegen acht Uhr früh das Frühstück brachte, 
kam diesmal nicht.'''

with open("example_data/der_prozess.txt", "a") as prozess_file:
    prozess_file.write(second_sentence_prozess)


# Um den Inhalt einer Datei auszulesen verwenden Sie "r" (read) als zweiten Parameter für `open()` sowie die Funktion `read()`. Diese gibt Ihnen den Inhalt der Datei als String zurück.

# In[ ]:


with open("example_data/der_prozess.txt", "r") as prozess_file:
    prozess_content = prozess_file.read()

print(prozess_content)


# In einigen Fällen müssen Sie eine Datei Zeile für Zeile auslesen und weiterverarbeiten. In diesem Fall verwenden Sie die Funktion `readlines()`. Um den Unterschied zu `read()` besser erkennen zu können, geben wir noch die Länge des jeweiligen Strings aus:

# In[ ]:


file_name = "example_data/adliger_vergleich.txt"

with open(file_name, "r") as arbitration_file:
    arbitration_content = arbitration_file.readlines()

for line in arbitration_content:
    print("Textzeile: ", line)
    print(f"Die Zeile ist {len(line)} Zeichen lang.")
    print('*' * 20)


# In[ ]:


file_name = "example_data/adliger_vergleich.txt"

with open(file_name, "r") as arbitration_file:
    arbitration_content = arbitration_file.read()

print("Dateiinhalt:\n" + arbitration_content + "\n")
print(f"Der Dateiinhalt umfasst {len(arbitration_content)} Zeichen.")


# ## Zeichenkodierung
# 
# Möglicherweise haben Sie bei der Durchsicht der Ausgabeergebnisse festgestellt, dass manche Wörter etwas seltsam aufgelöst werden. Statt "gräflich" finden wir im Output bspw. die Zeichenfolge "grÃ¤flich". Hierbei handelt es sich um einen Konflikt bezüglich der Kodierung des Textbestandes. Die Daten sind anders kodiert als es unser Interpreter standardmäßig vermutet. 
# 
# Was heißt das konkret?
# Alles, was Ihnen auf dem Bildschirm Ihres Laptops, PCs, Handys oder Tablets angezeigt wird beruht im Kern auf einer Kombination von Nullen und Einsen, also auf dem Binärcode. Das heißt, dass alle Zeichen, die wir visuell auf dem Bildschirm wahrnehmen, aus einem solchen [Binärcode](https://de.wikipedia.org/wiki/Bin%C3%A4rcode) zusammengesetzt sind. Zur Repräsentation der verschiedenen Sprachfamilien haben sich im Laufe der Zeit verschiedene Kodierungssysteme herausgebildet, die das Konzept eines Zeichens mit einer graphischen Repräsentation verknüpfen. Ein früher Standard war [ASCII](https://de.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange), der aber beispielsweise keine Umlaute kodieren konnte. Heute ist vor allem [UTF-8](https://de.wikipedia.org/wiki/UTF-8) als Speicherformat für Unicode etabliert, mit dem theoretisch über eine Millionen Zeichen kodiert werden können. [Unicode](https://de.wikipedia.org/wiki/Unicode) basiert auf dem Konzept, jedes sinntragende Schriftzeichen oder Textelement aller Schriftkulturen und Zeichensysteme durch einen digitalen Code zu repräsentieren. Bei der konkreten Arbeit werden Sie aber feststellen, dass nicht alle Textdaten einer einheitlichen Kodierung entsprechen, was eben unter anderem an der Historizität von Kodierungssystemen und zum Teil sich verändernden Standards liegt.
# 
# Wenn Sie Dateien einlesen oder schreiben, dann empfiehlt es sich, die Kodierung direkt zu spezifizieren. Das tun Sie, indem Sie bei Funktionen wie `open()`, `read()` oder `write()` etc. einen weiteren Parameter definieren: `encoding=""`. Schauen Sie sich im folgenden Codeblock an, wie der Parameter verwendet wird:

# In[ ]:


file_name = "example_data/adliger_vergleich.txt"

with open(file_name, "r", encoding="utf8") as arbitration_file:
    arbitration_content = arbitration_file.read()

print("Dateiinhalt:\n" + arbitration_content + "\n")
print(f"Der Dateiinhalt umfasst {len(arbitration_content)} Zeichen.")


# ## Aufgabe: Textdaten speichern
# 
# Für diese Aufgabe müssen Sie auf Ihren Code aus einem früheren Notebook zurückgreifen: Passen Sie den Programmcode aus der [Aufgabe zur Berechnung](aufgabe-primzahlen-ausgeben) der Primzahlen so an, dass die Ergebnisse nicht mehr mit `print()` ausgegeben, sondern in einer Textdatei gespeichert werden. Nach jeder Primzahl soll dabei ein Zeilenumbruch erfolgen. Falls Sie die Primzahlaufgabe nicht lösen konnten, orientieren Sie sich an der zur Verfügung gestellten Musterlösung.

# In[ ]:


# Ihr Code


# In[ ]:


# hidden cell creates content for using with Thebe Live-Code
# >>>change paths, when Jupyter Book is published<<<

import requests
import os

data_folder = 'example_data'

try:
    os.mkdir(data_folder)
except:
    pass

iiif_folder = 'example_data/iiif-manifests'

try:
    os.mkdir(iiif_folder)
except:
    pass  
  
file_list_1 = [('adliger_vergleich.txt', 'https://raw.githubusercontent.com/martindroege/jb-example-data/main/adliger_vergleich.txt'),
             ('books.csv', 'https://raw.githubusercontent.com/martindroege/jb-example-data/main/books.csv'),
             ('library.json', 'https://raw.githubusercontent.com/martindroege/jb-example-data/main/library.json')]

for file_name, url in file_list_1:
    response = requests.get(url)

    with open(f'example_data/{file_name}', 'w', encoding='UTF8') as f:
        f.write(response.text)
        
file_list_2 = [1950, 2228, 2608, 2170, 2187, 2196]
base_url = 'https://raw.githubusercontent.com/martindroege/jb-example-data/main/iiif-manifests/BnF.%20Departement%20des%20Manuscrits.%20Francais%20'
base_file_name = 'BnF. Departement des Manuscrits. Francais '

for i in file_list_2:
    response = requests.get(f'{base_url}{str(i)}.json')

    with open(f'{iiif_folder}/{base_file_name}{str(i)}.json', 'w', encoding='UTF8') as f:
        f.write(response.text)

