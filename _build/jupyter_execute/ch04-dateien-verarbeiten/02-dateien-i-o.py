#!/usr/bin/env python
# coding: utf-8

# ## Dateien öffnen, lesen und bearbeiten
# 
# Bislang haben wir Daten in Variablen gespeichert und Ergebnisse mit `print()` ausgegeben. In der Praxis wollen wir Daten natürlich dauerhaft (persistent) speichern, später wieder bearbeiten können, oder die Daten von Dritten weiterverarbeiten lassen.

# ### Grundlagen
# Zu Beginn ein paar basale Grundlagen, die Ihnen vermutlich weitestgehend vertraut vorkommen.
# 
# Eine Datei ist identifizierbar durch ihren Namen und ihren Dateityp. Außerdem lässt sich jede Datei irgendwo in einer Verzeichnisstruktur verorten (= sie ist in einem Order gespeichert, der zugleich ein Unterordner eines anderen ist).
# 
# Name, Dateityp und Speicherdatei lassen sich als *Pfad* angeben. (Auf Ihrem Rechner können Sie sich im Explorer/Dateimanager/Finder den Dateipfad auch einblenden lassen.) Ein Beispiel: Der Dateipfad für dieses Notebook sieht auf meinem Rechner so aus:
# ```
# /Users/pschneider/Documents/Lehre/Programmieren für Historiker*innen_WS_2020_21/Programmieraufgaben/4_Programmieren_f_Hist_Dateien_verarbeiten.ipynb.ipynb
# ```
# Dies ist der *absolute* Dateipfad; unabhängig davon wo ich mich auf meinem Rechner befinde, zeigt er die genaue Position von `4_Programmieren_f_Hist_Dateien_verarbeiten.ipynb.ipynb` an. Die einzelnen Verzeichnisse sind dabei immer durch Slashes (/) getrennt. Beachten Sie bitte, dass das Betriebssystem Windows hier eine Ausnahme macht; dort werden Verzeichnisse durch Backslashes (\\) voneinander getrennt (hier beginnt der Pfad außerdem mit einem Laufwerksbuchstaben).
# 
# Wenn Sie dieses Notebook auf Ihrem Rechner speichern, wird dessen Dateipfad natürlich völlig anders als bei mir aussehen. Daher ist es wichtig so oft wie möglich mit *relativen* Pfaden zu arbeiten. Relative Pfade bezeichen den Dateipfad ausgehend von meiner Position (bzw. der Position Ihres Python-Skripts) in der Verzeichnisstruktur. Angenommen, ich hätte ein Python-Skript im Ordner "Lehre" auf meinem Rechner liegen. Der (relative) Dateipfad des Notebooks wäre dann:
# ```
# Programmieren für Historiker*innen_SS_2020/Programmieraufgaben/4_Programmieren_fuer_Historiker_innen_Dateien_verarbeiten.ipynb
# ```
# Durch Angabe von ".." ist es möglich in einem Dateipfad einen Wechsel zu einem übergeordneten Verzeichnis anzugeben. Auf meinem Rechner gibt es im Ordner "Documents" z.B. neben "Lehre" auch einen Ordner "Publikationen". Angenommen ich hätte ein Python-Skript im Ordner "Publikationen" gespeichert, das ebenfalls auf das Notebook zugreifen soll. Hier wäre der relative Dateipfad dann:
# ```
# ../Lehre/Programmieren für Historiker*innen_SS_2020/Programmieraufgaben/4_Programmieren_fuer_Historiker_innen_Dateien_verarbeiten.ipynb
# ```
# 
# ### Wichtige Hinweise zur Verwendung von Google Colab
# Für den Fall, dass Sie Google Colab verwenden, können Sie sich einen Überblick über die Verzeichnisstruktur verschaffen, indem Sie links, in der Seitenleiste, auf das kleine Ordnersymbol klicken. Wenn Sie Python auf Ihrem Rechner ausführen, berücksichtigen Sie für diese Übung bitte Ihre lokale Ordnerstruktur. Die Angabe eigener Dateipfade hängt dann davon ab, wie Sie Ihre Festplatte organisiert haben. Damit alle Codeblöcke in diesem Notebook funktionieren, speichern Sie bitte alle Dateien im selben Verzeichnis, in dem sich auch das Notebook befindet. Um Dateien in Google Colab hochzuladen können Sie entweder auf der linken Seite auf *Upload* klicken ODER folgenden Code ausführen:

# In[1]:


# Option 1, wenn Sie Google Colab nutzen
from google.colab import files

uploaded = files.upload()

for filename in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(name=filename, length=len(uploaded[filename])))


# Alternativ können Sie Ihren Google Drive einbinden. Passen Sie in diesem Fall bitte alle Dateilinks in diesem Notebook entprechend an.

# In[ ]:


# Option 2, wenn Sie Google Colab nutzen
from google.colab import drive
drive.mount('/content/drive')


# Vergessen Sie nicht die Dateien für diese Übung zu entpacken (üblicherweise über das sich per Rechtsklick auf die Zip-Datei öffnende Kontextmenü) und an einer geeigneten Stelle in Ihrem Dateisystem abzulegen (zum Beispiel dort, wo Sie Ihre Notebooks bearbeiten, dann können Sie ganz einfach auf den Ordner mit den Beispieldateien für dieses Notebook zugreifen). 
# 
# In Google Colab geht das Entpacken mit diesem Befehl - natürlich nachdem Sie die Beispieldaten auf Ihrem Drive abgelegt haben und mittels der vorangegangenen Codeblocks Zugriff auf Ihr Drive erteilt haben (wenn Sie Anaconda nutzen, müssen Sie das nicht ausführen):

# In[ ]:


get_ipython().system('unzip 4_Beispieldateien.zip')


# ### Dateien öffnen, lesen und schreiben
# In dieser Einführung arbeiten wir ausschließlich mit textbasierten Dateiformaten (also z.B. txt, csv, json, html, tsv, md, tex, py, ...). Diese Dateien lassen sich einfach als String auslesen, der zugleich den Inhalt der Datei repräsentiert. Komplexe Formate, wie Bilder (jpgs, png, tiff, ...), PDFs, Worddokumente, Exceldateien oder Video- und Audioformate bestehen zwar letztlich auch nur aus Zeichenketten, sind aber auf eine bestimmte Weise *codiert*. Auch solche Dateien können Sie mit Python bearbeiten; hierfür werden aber bestimmte Programmbibliotheken benötigt. Falls Sie in einem eigenen Projekt mit einem dieser Formate arbeiten wollen, finden Sie die entsprechenden Bibliotheken meist nach einer kurzen Suche im Internet.
# 
# Das Bearbeiten einer Datei beginnt immer mit der Funktion `open()`. Im folgenden Codeblock erstellen wir eine Testdatei, in der wir den ersten Satz aus Kafkas *Prozess* speichern.

# In[ ]:


first_sentence_prozess = "Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet."

prozess_file = open("4_Beispieldateien/Der Prozess.txt", "w")
prozess_file.write(first_sentence_prozess)
prozess_file.close()


# Die Funktion `open()` erzeugt ein Objekt, das quasi als Schnittstelle zwischen Ihrem Programm und dem Betriebssystem fungiert. `open()` benötigt als Parameter den Namen bzw. Dateipfad der Datei sowie die Angabe in welchem Modus die Datei geöffnet werden soll. Da wir eine noch nicht existierende Datei neu beschreiben wollen, wählen wir hier "w" (write). Das File-Objekt (hier als `prozess_file` gespeichert) verfügt über verschiedene Funktionen zum Lesen und Schreiben von Dateien. Mit `write()` geben wir an, dass wir den String `first_sentence_prozess` (den wir ja in Zeile 1 definiert haben) als Inhalt der Datei speichern wollen. Mit `close()` teilen wir dem File-Objekt mit, dass wir keine Änderungen an der Datei mehr vornehmen möchten. Dieser Schritt muss immer erfolgen, wenn Sie mit Dateien arbeiten (andernfalls könnten Sie versehentlich Ressourcen Ihres Computers für das Beschreiben einer Datei binden, obwohl sie an anderer Stelle benötigt werden). Damit `close()` auch im Falle eines Fehlers ausgeführt wird, verwenden Sie am besten so oft es geht folgendes Statement:

# In[ ]:


first_sentence_prozess = "Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet. "

with open("4_Beispieldateien/Der Prozess.txt", "w") as prozess_file:
    prozess_file.write(first_sentence_prozess)


# Wenn Sie "w" als zweiten Parameter für `open()` verwenden, wird der Inhalt der Datei immer komplett überschrieben. Je nachdem was Sie tun möchten, müssen Sie hier den richtigen Parameter wählen. Schauen Sie doch mal im Ordner "4_Beispieldateien" nach, ob Sie darin die Datei "Der Prozess" finden. 
# 
# Um etwas an einen bestehenden Dateiinhalt anzuhängen, verwenden Sie den Parameter "a" (append).

# In[ ]:


second_sentence_prozess = "Die Köchin der Frau Grubach, seiner Zimmervermieterin, die ihm jeden Tag gegen acht Uhr früh das Frühstück brachte, kam diesmal nicht."

with open("4_Beispieldateien/Der Prozess.txt", "a") as prozess_file:
    prozess_file.write(second_sentence_prozess)


# Um den Inhalt einer Datei auszulesen verwenden Sie "r" (read) als zweiten Parameter für `open()` sowie die Funktion `read()`. Diese gibt Ihnen den Inhalt der Datei als String zurück.

# In[ ]:


with open("4_Beispieldateien/Der Prozess.txt", "r") as prozess_file:
    prozess_content = prozess_file.read()

print(prozess_content)


# In einigen Fällen müssen Sie eine Datei Zeile für Zeile auslesen und weiterverarbeiten. In diesem Fall verwenden Sie die Funktion `readlines()`. Um den Unterschied zu `read()` besser erkennen zu können, geben wir noch die Länge des jeweiligen Strings aus:

# In[ ]:


file_name = "4_Beispieldateien/Adliger Vergleich.txt"

with open(file_name, "r") as arbitration_file:
    arbitration_content = arbitration_file.readlines()

for line in arbitration_content:
    print("Textzeile", line)
    print("Die Zeile ist {} Zeichen lang.".format(len(line)))


# In[ ]:


file_name = "4_Beispieldateien/Adliger Vergleich.txt"

with open(file_name, "r") as arbitration_file:
    arbitration_content = arbitration_file.read()

print("Dateiinhalt:\n" + arbitration_content + "\n")
print("Der Dateiinhalt umfasst {} Zeichen.".format(len(arbitration_content)))


# ### Zeichenkodierung
# 
# Möglicherweise haben Sie bei der Durchsicht der Ausgabeergebnisse festgestellt, dass manche Wörter etwas seltsam aufgelöst werden. Statt "gräflich" finden wir im Output bspw. die Zeichenfolge "grÃ¤flich". Hierbei handelt es sich um einen Konflikt bezüglich der Kodierung des Textbestandes. Die Daten sind anders kodiert als es unser Interpreter standardmäßig vermutet. 
# 
# Was heißt das konkret?
# Alles, was Ihnen auf dem Bildschirm Ihres Laptops, PCs, Handys oder Tablets angezeigt wird beruht im Kern auf einer Kombination von Nullen und Einsen, also auf dem Binärcode. Das heißt, dass alle Zeichen, die wir visuell auf dem Bildschirm wahrnehmen, aus einem solchen [Binärcode](https://de.wikipedia.org/wiki/Bin%C3%A4rcode) zusammengesetzt sind. Zur Repräsentation der verschiedenen Sprachfamilien haben sich im Laufe der Zeit verschiedene Kodierungssysteme herausgebildet, die das Konzept eines Zeichens mit einer graphischen Repräsentation verknüpfen. Ein früher Standard war [ASCII](https://de.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange), der aber beispielsweise keine Umlaute kodieren konnte. Heute ist vor allem [UTF-8](https://de.wikipedia.org/wiki/UTF-8) als Speicherformat für Unicode etabliert, mit dem theoretisch über eine Millionen Zeichen kodiert werden können. [Unicode](https://de.wikipedia.org/wiki/Unicode) basiert auf dem Konzept, jedes sinntragende Schriftzeichen oder Textelement aller Schriftkulturen und Zeichensysteme durch einen digitalen Code zu repräsentieren. Bei der konkreten Arbeit werden Sie aber feststellen, dass nicht alle Textdaten einer einheitlichen Kodierung entsprechen, was eben unter anderem an der Historizität von Kodierungssystemen und zum Teil sich verändernden Standards liegt.
# 
# Wenn Sie Dateien einlesen oder schreiben, dann empfiehlt es sich, die Kodierung direkt zu spezifizieren. Das tun Sie, indem Sie bei Funktionen wie `open()`, `read()` oder `write()` etc. einen weiteren Parameter definieren: `encoding=""`. Schauen Sie sich im folgenden Codeblock an, wie der Parameter verwendet wird:

# In[ ]:


file_name = "4_Beispieldateien/Adliger Vergleich.txt"

with open(file_name, "r", encoding="UTF-8") as arbitration_file:
    arbitration_content = arbitration_file.read()

print("Dateiinhalt:\n" + arbitration_content + "\n")
print("Der Dateiinhalt umfasst {} Zeichen.".format(len(arbitration_content)))


# #### **Zwischenaufgabe: Textdaten speichern**
# Für diese Aufgabe müssen Sie auf Ihren Code aus einem früheren Notebook zurückgreifen: Passen Sie den Programmcode aus der Aufgabe zur Berechnung der Primzahlen aus dem zweiten Notebook so an, dass die Ergebnisse nicht mehr mit `print()` ausgegeben, sondern in einer Textdatei gespeichert werden. Nach jeder Primzahl soll dabei ein Zeilenumbruch erfolgen. (Falls Sie die Primzahlaufgabe nicht lösen konnten, orientieren Sie sich an der in Moodle zur Verfügung gestellten Musterlösung.)

# In[ ]:


# Ihr Code

