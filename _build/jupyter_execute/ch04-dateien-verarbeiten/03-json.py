#!/usr/bin/env python
# coding: utf-8

# ## [JSON](https://de.wikipedia.org/wiki/JavaScript_Object_Notation)
# 
# Einfache Textdateien, wie wir sie soeben eingelesen und geschrieben haben, sind für zahlreiche Anwendungsfälle schon sehr nützlich. Sie sind aber vergleichsweise unstrukturiert. Sehr oft wollen wir im Rahmen historischer Forschungsarbeiten aber mit eindeutig organsierten und strukturierten Informationen arbeiten. Wir können bei einem Korpus mit Briefen zum Beispiel folgende Informationen zu jedem Brief haben: Datum, Ort, Verfasser:in, Adressat:in, Brieftext sowie weiter Informationen. In einfachen Textdateien könnten wir nicht so ohne Weiteres auf diese Informationen zugreifen. Für solche Anwedungsszenarien gibt es allerdings eine Reihe von Dateiformaten, von denen wir im folgenden zwei genauer in den Blick nehmen werden.
# 
# JSON ist ein verbreites Dateiformat zur textbasierten Speicherung strukturierter Daten. Ursprünglich wurde es im Rahmen der Programmiersprache [*JavaScript*](https://de.wikipedia.org/wiki/JavaScript) (JSON ist ein Akronym für "JavaScript Object Notation") zum Austausch von Daten verwendet. Inzwischen ist das Format zu einem wichtigen Standard zur maschinenbasierten Kommunikation zwischen unterschiedlichen Plattformen geworden. Es ist unabhängig von bestimmten Programmiersprachen. Die Strukturierung von JSON-Dateien unterliegt nur [wenigen Regeln](https://www.json.org/json-en.html). Lesen Sie sich die Inhalte der verlinkten Seite in Ruhe durch.
# 
# ## Aufbau einer JSON-Datei
# 
# Betrachten wir einmal den Inhalt der Datei "library.json" in unserem Ordner "data". Es handelt sich hier nicht um einen ausführbaren Code:

# ```
# {
#     "label": "My Library",
#     "books available": true,
#     "owner": null,
#     "books": [
#         {
#             "title": "Der Prozess",
#             "author": "Franz Kafka",
#             "year": 1935,
#             "editions": [
#                 1935,
#                 1946,
#                 1963,
#                 1990,
#                 2011,
#                 2012
#             ]
#         },
#         {
#             "title": "Half of a Yellow Sun",
#             "author": "Chimamanda Ngozi Adichie",
#             "year": 2006,
#             "editions": [
#                 2006,
#                 2007,
#                 2017
#             ]
#         },
#         {
#             "title": "Network Effect",
#             "author": "Martha Wells",
#             "year": 2020,
#             "editions": [
#                 2020
#             ]
#         }
#     ]
# }
# ```

# Mit dem Wissen aus dem letzten Notebook wird Ihnen wahrscheinlich auffallen, dass der Inhalt der Datei wie eine Kombination aus Dictionaries und Listen aussieht. Tatsächlich sind die zugrundeliegenden Konzepte identisch. Einzig die Benennung ist etwas anders -- in JSON-Dateien heißen Dictionaries *Objekte*, Listen heißen *Arrays*. Ein weiterer feiner Unterschied ist die Verwendung von `null` für ein leeres Element in JSON. In Python verwenden Sie dagegen `None`, wenn eine Variable keinen Wert haben soll. Strings und Integers funktionieren, wie Sie es aus Python kennen.
# 
# Der Inhalt der JSON-Datei "library.json" besteht demnach aus einem Dictionary mit vier Schlüssel-Wert-Paaren ("label", "books available", "owner", "books"). In "books" ist eine Liste bzw. - im JSON-Sprech - ein Array gespeichert, das weitere Dictionaries respektive Objekte enthält. Jedes Dictionary / Objekt modelliert dabei ein einzelnes Buch.
# 
# Wenn Sie mit den hier verwendeten Begriffen Probleme haben, gehen Sie am besten nochmal die Abschnitte zu *Listen* und *Dictionaries* im letzten Kapitel durch.

# ## JSONs in Python öffnen und speichern
# 
# Nun wollen wir ein Programm schreiben, mit dem wir die Datei "library.json" auslesen und um weitere Bücher erweitern können. Mit dem unten angeführten Code, den Sie bereits aus dem letzten Kapitel kennen, können Sie auch JSON-Dateien öffnen und bearbeiten. Allerdings können wir den Inhalt der Datei dann nur als String verarbeiten -- die Struktur aus Dictionaries und Listen geht verloren. Natürlich können wir auch ein Programm schreiben, dass an den richtigen Stellen die richtigen Klammern einfügt -- dies ist jedoch aufwändiger als den Inhalt der JSON-Datei in ein einzelnes Dictionary zu konvertieren. Hierzu stellt Python die Programmbibliothek `json` zur Verfügung. Um diese in Ihrem Programm verwenden zu können, muss diese zunächst importiert werden. Das geschieht, wenn Sie folgende Zeile ausführen:

# In[ ]:


import json


# Anschließend können wir den Inhalt der Datei mit der Funktion `load()` auslesen und als Dictionary in einer Variable speichern:

# In[ ]:


with open("../data/library.json", "r") as json_file:
    library_content = json.load(json_file)

print(type(library_content))
print(library_content)


# Ab jetzt können wir die Daten weiterverarbeiten, wie im letzten Kapiteö behandelt: Sie können damit wie mit jedem anderen Dictionary arbeiten. Mit folgendem Code können Sie etwa alle in der Bibliothek gespeicherten Buchtitel, Autor:innen und das Jahr der letzten Auflage auslesen:

# In[ ]:


book_list = library_content['books']

for book in book_list:
    print(f'''Das Buch '{book['title']}' von '{book['author']}' 
    wurde zuletzt im Jahr {book['editions'][-1]} aufgelegt.\n''')


# Änderungen an der *Datei* "library.json" können Sie ähnlich, wie im vorherigen Abschnitt beschrieben, vornehmen. Bereiten Sie zuerst die Dictionary-Variable vor, die den Inhalt der JSON-Datei speichert. Anschließend kann die Variable mit der Funktion `dump()` in eine JSON-Datei exportiert werden. Ähnlich wie die Funktion `write()`, die Sie weiter oben kennen gelernt haben, benötigt `dump()`, die Dictionary-Variable und ein Datei-Objekt als Parameter. Hier aktualisieren wir die fehlende Information unter "owner".

# In[ ]:


library_content['owner'] = "Max Mustermann"

with open("../data/library_version_2.json", "w") as json_file:
    json.dump(library_content, json_file)


# Wenn Sie die JSON-Datei aus dem Ordner "data" heraus öffnen (zum Beispiel mittels Editor) werden Sie feststellen, dass der Inhalt nun in einer einzigen Zeile gespeichert ist. Insbesondere bei sehr großen JSON-Dateien lässt sich so Speicherplatz sparen.Zur Erinnerung: Zeilenumbrüche und Tabstobs werden durch "\\n" bzw. "\\t" repräsentiert; auch einzelne Zeichen verbrauchen Speicherkapazität. Oft müssen Sie bei der Arbeit mit JSON-Dateien aber auch in die Dateien reinschauen; hier helfen dann Zeilenumbrüche und Einrückungen. Sie können der Funktion `dump()` einen weiteren Parameter (`indent`) mit der Anzahl der Einrückungen nach einem Zeilenumbruch übergeben. Auf diese Weise wird die JSON-Datei lesbarer:

# In[ ]:


library_content['owner'] = "Maxine Musterfrau"

with open("../data/library_version_2", "w") as json_file:
    json.dump(library_content, json_file, indent = 4)


# Wenn Sie die JSON-Datei nun noch einmal öffnen, dann sollte sie sich schon sehr viel übersichtlicher darstellen.

# ## JSON in den Digitalen Geschichtswissenschaften: IIIF
# 
# Ein zunehmend wichtig werdender Datenstandard im Cultural-Heritage-Bereich ist das [*International Image Interoperability Framework (IIIF)*](https://iiif.io/) (Aussprache: Triple-I-F). Es wurde ursprünglich von verschiedenen GLAM-Einrichtung (Galleries, Libraries, Archives, Museums) entwickelt. Ziel war es, ein standardisiertes Framework für ein Datenmodell zu schaffen, um bildbasiertes Kulturgut interoperabel, also unabhängig von den sich unterscheidenden Standards unterschiedlicher Kultureinrichtungen, online präsentieren und austauschen zu können. Dabei sollten nicht nur Metadaten zur Beschreibung des Kontextes der einzelnen Kulturgutobjekte gespeichert werden können, sondern insbesondere bei Werken, die aus mehreren Bilddateien bestehen, logische Zusammenhänge zwischen den Einzelbildern für das Gesamtwerk erhalten werden. Die Anwendungsmöglichkeiten von IIIF sind sehr vielfältig; [zahlreiche Einrichtungen und Projekte](https://github.com/IIIF/awesome-iiif) greifen mittlerweile darauf zurück.
# 
# Sie müssen sich für diese Einführung nicht intensiv in IIIF einarbeiten. In der folgenden Übungsaufgabe werden wir uns ausschließlich auf die [Presentation API](http://ronallo.com/iiif-workshop/presentation/) konzentrieren. In aller Kürze beschrieben definiert die *Presentation API* einen Standard zur Strukturierung einer JSON-Datei um die Zusammenhänge eines bildbasierten Werkes beschreiben zu können ([Vollständige Dokumentation der *Presentation API*](https://iiif.io/api/presentation/3.0/)). Eine solche Datei wird *Manifest* genannt.
# 
# In der folgenden Aufgabe werden wir mit mittelalterlichen Handschriften arbeiten. Eine einzelne Handschrift kann als ein einzelnes, bildbasiertes Werk verstanden werden. Beachten Sie dabei, dass es hier um das tatsächliche Buch, das in irgendeiner Bibliothek liegt, geht -- nicht um den Text der Handschrift oder um Faksimiles. Eine Handschrift kann somit durch ein IIIF-Manifest repräsentiert werden. Betrachten wir z.B. das Manuskript "Grandes Chroniques de France"; Sie finden es im Ordner im Pfad "data/iiif-manifests" unter "BnF. Departement des Manuscrits. Français 2608.json". Wir müssen an dieser Stelle nicht auf jedes Detail genau eingehen. Metadaten der Handschrift sind in der Liste "metadata" gespeichert. Hier finden Sie z.B. den Titel, die Datierung oder die Sprache, in der der Text verfasst ist. Das Manifest enthält außerdem die Links zu den Bilddateien der Scans der einzelnen Seiten. Diese sind im Manifest in der Liste "canvases" gespeichert (die ein Dictionary in der Liste "sequences" ist). Jede Seite der Handschrift wird dabei durch ein "canvas"-Dictionary repräsentiert. Um den Link zur Bilddatei der jeweiligen Seite zu finden, suchen Sie in der Liste "images" nach dem Schlüssel "@id".[^fn1] Der Link zur Bilddatei der ersten Seite der "Grandes Chroniques de France" ist z.B. [https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/f1/full/full/0/native.jpg](https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/f1/full/full/0/native.jpg). Schauen Sie sich die JSON-Datei gut an und vollziehen Sie ihren Aufbau nach.
# 
# Angenommen, Sie wollen nun die Scans aller Seiten der Handschrift herunterladen. In diesem Fall können Sie natürlich auch die Handschrift im [Viewer der französischen Nationalbibliothek](https://gallica.bnf.fr/ark:/12148/btv1b8451604g) aufrufen und die Digitalisate dort herunterladen. Wollen Sie das jedoch für mehrere Dutzend oder gar Hundert Handschriften tun, bieten Ihnen die IIIF-Manifeste eine Möglichkeit den Download automatisiert durchzuführen.

# ## Aufgabe: JSON-Daten verarbeiten
# Schreiben Sie ein Programm zur Vorbereitung eines automatischen Downloads aller Bilddateien der Scans einer Reihe von vorgegebenen mittelalterlichen Handschriften. Die IIIF-Manifeste der einzelnen Handschriften finden Sie in im Ordner data/iiif-manifests. Ihr Programm sollte die folgenden Aufgaben durchführen:
# * Die Links zu den Bilddateien der Scans sollten in einer Textdatei (.txt) gespeichert werden. Nach jedem Link soll ein Zeilenumbruch erfolgen. Die Links werden also zeilenweise in der Datei aufgelistet.
# * Es soll für jede Handschrift jeweils eine eigene Textdatei erstellt werden, die die Links zu ihren Scans enthält.
# * Der Name jeder Textdatei soll der Titel der jeweiligen Handschrift sein (also z.B. "Grandes Chroniques de France.txt").
# * *Optional: Extrahieren Sie nur die Links aus den IIIF-Manifesten, deren Handschriften irgendwann zwischen den Jahren 1300 und 1400 datiert sind.*

# In[ ]:


folder_path = "../data/iiif-manifests/"
manifests = [
      "BnF. Departement des manuscrits. Francais 2170.json",
      "BnF. Departement des manuscrits. Francais 2187.json",
      "BnF. Departement des Manuscrits. Francais 1950.json",
      "BnF. Departement des manuscrits. Francais 2196.json",
      "BnF. Departement des Manuscrits. Francais 2228.json",
      "BnF. Departement des Manuscrits. Francais 2608.json"       
]

# Ihr Code


# [^fn1]: "images" muss eine Liste sein, da ein IIIF-"canvas" auch aus mehreren Bilddateien bestehen kann. So kann etwa im Manifest abgebildet werden, dass zu einer Seite einer Handschrift nur Fragmente existieren; jedes Fragment kann durch eine eigene Bilddatei dargestellt werden. Das nur als kleines Beispiel für die Flexibilität von IIIF.
