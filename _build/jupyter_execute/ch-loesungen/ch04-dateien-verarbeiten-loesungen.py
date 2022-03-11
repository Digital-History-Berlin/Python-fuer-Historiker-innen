#!/usr/bin/env python
# coding: utf-8

# # Lösungen zu den Aufgaben aus dem Abschnitt Dateien verarbeiten

# ## Lösung: Aufgabe Textdaten speichern
# 
# Für diese Aufgabe müssen Sie auf Ihren Code aus einem früheren Notebook zurückgreifen: Passen Sie den Programmcode aus der [Aufgabe zur Berechnung](aufgabe-primzahlen-ausgeben) der Primzahlen so an, dass die Ergebnisse nicht mehr mit `print()` ausgegeben, sondern in einer Textdatei gespeichert werden. Nach jeder Primzahl soll dabei ein Zeilenumbruch erfolgen. Falls Sie die Primzahlaufgabe nicht lösen konnten, orientieren Sie sich an der zur Verfügung gestellten Musterlösung

# In[3]:


# Ihr Code

file_name = 'prime_numbers.txt'
# Dieser String ersetzt unsere print-Ausgabe in der alten Lösung. 
# Er wird später nur noch in eine Datei geschrieben.
prime_numbers = ''

# Musterlösung Aufgabe Primzahlen
is_prime = False

for number in range(3, 201):
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
        else:
            is_prime = True
    
    if is_prime:  
        prime_numbers += str(number) + '\n'     # das \n sorgt für einen Zeilenumbruch

with open(file_name, 'w') as prime_file:
    prime_file.write(prime_numbers)


# ## Lösung: Aufgabe JSON-Daten verarbeiten
# 
# Schreiben Sie ein Programm zur Vorbereitung eines automatischen Downloads aller Bilddateien der Scans einer Reihe von vorgegebenen mittelalterlichen Handschriften. Die IIIF-Manifeste der einzelnen Handschriften finden Sie in im Ordner data/iiif-manifests. Ihr Programm sollte die folgenden Aufgaben durchführen:
# * Die Links zu den Bilddateien der Scans sollten in einer Textdatei (.txt) gespeichert werden. Nach jedem Link soll ein Zeilenumbruch erfolgen. Die Links werden also zeilenweise in der Datei aufgelistet.
# * Es soll für jede Handschrift jeweils eine eigene Textdatei erstellt werden, die die Links zu ihren Scans enthält.
# * Der Name jeder Textdatei soll der Titel der jeweiligen Handschrift sein (also z.B. "Grandes Chroniques de France.txt").
# * *Optional: Extrahieren Sie nur die Links aus den IIIF-Manifesten, deren Handschriften irgendwann zwischen den Jahren 1300 und 1400 datiert sind.*

# In[2]:


import json
import pprint 
# Das ist nur eine Möglichkeit den print-Befehl zu ersetzen -- 
# hiermit werden z.B. JSONs strukturierter dargestellt (pprint steht für "pretty print")

folder_path = '../ch04-dateien-verarbeiten/example_data/iiif-manifests/'
manifests = [
      'BnF. Departement des Manuscrits. Francais 2170.json',
      'BnF. Departement des Manuscrits. Francais 2187.json',
      'BnF. Departement des Manuscrits. Francais 1950.json',
      'BnF. Departement des Manuscrits. Francais 2196.json',
      'BnF. Departement des Manuscrits. Francais 2228.json',
      'BnF. Departement des Manuscrits. Francais 2608.json'       
]

# Ihr Code

# Wir gehen die einzelnen IIIF-Manifestdateien der Reihe nach durch, 
for manifest_name in manifests:
    
    # öffnen der Datein
    with open(f'{folder_path}{manifest_name}', "r", encoding="UTF-8") as json_file:
        
        # einlesen JSON-Datei als JSON-Objekt mit der JSON-Bibliothek 
        manifest_content = json.load(json_file)

        # Extraktion des Titels für den Namen der Textdatei aus dem Schlüssel-Element "description"
        manuscript_title = manifest_content.get('description')
        
        # Dateipfad und -name der Textdatei
        file_name = f'{folder_path}{manuscript_title[:15]}.txt' 
        # in der Musterlösung musste die Titel abgekürzt werden, 
        # da sie in einem Fall nicht korrekt als Dateiname ausgelesen werden konnten

        # Extraktion des Elements, in dem die Links zu den Bildern enthalten sind
        canvas_list = manifest_content['sequences'][0]['canvases']

        # Leerer String, in dem die Links für das Speichern abgelegt werden sollen
        image_link_collection = ''

        # Wir gehen nun nach und nach die Dictionaries der Liste, 
        # die im Schlüssel-Element "canvases" enthalten ist durch
        for canvas in canvas_list:
            
            # In den Dictionaries interessieren uns die Werte, 
            # die dem Schlüssel "images" zugeordnet sind, 
            # hierbei handelt es sich wiederum um eine Liste von Dictionaries
            single_image_element = canvas['images'][0] 
            # Beachten Sie die eckige Klammer in den JSON-Dateien der Manifeste hinter 'images'. 
            # Das verweist ja darauf, dass 'images' eine Liste ist; 
            # mit [0] in dieser Codezeile greifen Sie dann auf das erste Element dieser Liste zu
            
            # Der Link zur Bilddatei befindet sich im Wert zum Schlüssel "resource", 
            # der wiederum einem Dictionarie entspricht
            # Genau verbirgt sich der Link hinter dem Wert "@id",
            # das erkennen Sie an der Dateiendung .jpg
            single_image_link = single_image_element['resource']['@id']
            
            # Will man die oberen beiden Zeilen in einer zusammenfassen wäre das:
            # single_image_link = image_link['images'][0]['resource']['@id']
            # #pprint.pprint(single_image_link)
                  
            # #####################
            # # Eine Alternative zum obgien Code ist dieser hier. Denken Sie daran, 
            # die Auskommentierungen des Codes umzustellen, wenn Sie die Alternative ausführen möchten.
            # # (Damit berücksichtigen Sie den Sonderfall, dass die Liste 'images' (siehe oben) 
            # auch mehrere Elemente haben könnte)

            #for single_image_element in canvas['images']:
            #    single_image_link = single_image_element['resource']['@id']
            #    pprint.pprint(single_image_link)

            # Alternative Ende
            # #####################

            # Abschließend fügen wir den Link mit einem Zeilenumbruch zu unserem Output-String hinzu
            image_link_collection += single_image_link + '\n'

        # Hier wird der Output-String, wenn die For-Schleife beendet ist, 
        # mit der Linkliste in eine Textdatei geschrieben
        with open(f"{file_name}", 'w') as text_file:
            text_file.write(image_link_collection)


# ## Lösung: Aufgabe Daten strukturiert speichern
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

# In[4]:


import csv

# Ihr Code

# Zur Vorbereitung müssen Sie sicher stellen, 
# dass die zu verarbeitenden Texte in Textdateien gespeichert sind. 
# In dieser Lösung wird davon ausgegangen, dass der Text in einem  
#  relative zum Notebook liegenden Ordner 'example_data' gespeichert ist.

# Definiton der Funktionen

# Hilfsfunktion zum Lesen der Dateien:
def get_file_content(file_path):
    with open(file_path, "r", encoding="UTF-8") as file_to_open:
        file_content = file_to_open.read()
        
        return file_content

# Diese Funktion wird aus segment_text() heraus aufgerufen 
# und speichert die segmentierte Liste als CSV. 
# In jedem Segment werden außerdem die Zeichen gezählt.
def store_list_to_csv(segmented_text, csv_path):
    with open(csv_path, "w", encoding="UTF-8", newline='') as csv_file:
        header = ["id", "text", "anzahl_zeichen"]

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)

        # Zusammenführen der Sublistensegmente zu vollständigen Strings 
        # und Hinzufügen zum CSV-Writer
        current_id = 1

        for each in segmented_text:
            current_segment_text = " ".join(each[:])
            current_length = len(current_segment_text)

            csv_writer.writerow([str(current_id), current_segment_text, str(current_length)])

            current_id += 1

def tokenize_text(source_text):
    """Parameter: string
    The function tokenizes a string using whitespaces and returns a list object.
    Lowercasing is included."""

    # replace punctuation based on list
    for each in [".", ",", ";", "\"", "'", "/", "\\", "!", ":", "?", "(", ")", "[", "]"]:
        source_text = source_text.replace(str(each), "")

    # lower text
    lowered_text = source_text.lower()

    # tokenize by whitespace
    tokenized_text = lowered_text.split()

    return tokenized_text

def segment_text(tokenized_text, segments, output_path):
    """Parameters: list of strings and segment size (integer)
    A tokenized text is preprocessed by segmentation.
    The function returns a string object."""

    # segmentation
    segmented_text = []
    for i in range(0, len(tokenized_text), segments):
        segmented_text.append(tokenized_text[i:i + segments]) # i=0, 10, ...

    store_list_to_csv(segmented_text, output_path)

# Aufruf der Funktionen

# String aus Textdateien auslesen
source_exampletxt = get_file_content("example_data/beispieltext.txt")

# tokenize input data
tokenized_exampletxt = tokenize_text(source_exampletxt)

# segment input data
segment_text(tokenized_exampletxt, 10, "example_data/beispieltext.csv")


# In[ ]:




