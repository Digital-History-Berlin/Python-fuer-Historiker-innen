#!/usr/bin/env python
# coding: utf-8

# # Lösungen zu den Aufgaben aus dem Abschnitt Komplexe Datenstrukturen

# ## Lösung: Aufgabe Text Preprocessing
# 
# **Aufgabenstellung:**
# 
# 1. Suchen Sie sich einen Beispieltext aus, den Sie im Rahmen dieser Übungseinheit basal verarbeiten und analysieren wollen. Weisen Sie ihn einer Variablen zu.
# 
# 2. Definieren Sie zwei Funktionen:
# - `tokenize_text()` soll folgende Operationen beinhalten: 
#  - Entferung von Interpunktionszeichen
#  - Lowercasing aller Großbuchstaben
#  - Tokenisierung der Textdaten anhand von Whitespaces
# - `segment_text()` soll die tokenisierten Textdaten zu Segmenten in folgender Art weiterverarbeiten:
#  - Segmente sollten nicht länger als 10 Wörter sein
#  - Der Text soll am Ende zeilenweise (`\n`) als zusammenhängende Zeichenkette ausgegeben werden.
# 
# **Hinweise:**
# - Ihre Funktionen sollten auf beliebige Texte anwendbar sein
# - nutzen Sie bedingte Anweisungen und Schleifen
# - machen Sie Gebrauch von den Listenfunktionen, Ranges und Konkatenierungs- oder auch Formatierungsmöglichkeiten von Zeichenketten

# In[10]:


report = '''Die Editionswissenschaft erlebt nicht zuletzt wegen einer erfolgreichen Kombination von traditionellen Arbeitsweisen mit Methoden der Digital Humanities einen regelrechten Hype. Digitale Methoden drängen sich besonders an den Stellen auf, wo sie eine Überwindung der Beschränkungen des analogen Drucks versprechen. Zugleich zeichnet sich ab, dass mit einem Wechsel zu digitalen Editionsformen nicht nur neue Werkzeuge genutzt werden, sondern dass sich prinzipielle strukturelle Änderungen ergeben: so können analoge Editionen angereichert werden oder Editionen können als Hybrid durch eine gleichwertige digitale und analoge Version repräsentiert werden. Editoren werden angesichts dieser neuen Möglichkeiten vor neue Herausforderungen gestellt. Gleiches gilt für Infrastrukturen, die die Produkte der Editionswissenschaft publizieren und langfristig verfügbar machen sollen. Grundlegende Fragen der Qualitätsmessung und -bewertung, der Arbeitsorganisation, Vernetzung und Distribution müssen bei der digitalen Editionswissenschaft anders bzw. neu gestellt und bewertet werden. Die vom Forschungsverbund Marbach Weimar Wolfenbüttel veranstaltete Tagung “Digitale Metamorphose: Digital Humanities und Editionswissenschaft” betrachtete diese neuen Möglichkeiten kritisch und ging dabei auch der Frage nach, welche Grenzen und Gefahren es jenseits der offensichtlichen Vorteile für die Editionswissenschaft gibt. Den Auftakt der Tagung bildeten die Eröffnungsvorträge von BODO PLACHTA (Amsterdam) und JOÃO DIONÍSIO (Lissabon). Plachta wies auf die Bedeutung von philologischen Standards für die Editionsarbeit hin und stellte diese in ihrer historischen Entwicklung dar. Die aus dieser Entwicklung hervorgegangen editorischen Praktiken sollten auch im digitalen Medium gepflegt und weiterentwickelt werden. Die Vorteile des Digitalen dürfen nicht zu einem blinden Technikvertrauen führen, sondern müssen mit den traditionellen Qualitätsansprüchen der Editionswissenschaft kombiniert werden. Dionísio betonte die stetig wachsende Internationalität der Editionswissenschaft, die durch digitale Methoden und insbesondere durch neue Kommunikationsformen gefördert wird. Er beschrieb dabei die digitale Transformation der Editionswissenschaft in verschiedensten Bereichen wie dem Akt des Lesens, der institutionellen Kooperation, der Konstruktion und Interpretation von Textbedeutung und Textverstehen. Diesen Wandel skizzierte der Beiträger an den Beispielen der Archive und Gedächtnisinstitutionen sowie an den philologischen Netzwerken und wissenschaftlichen Verlagen. Austausch und Kooperationen werden in Zukunft gänzlich neue Editionsvorhaben ermöglichen und die Vernetzung über Sprach- und Landesgrenzen hinweg fördern. HEINZ-WERNER KRAMSKI (Marbach) eröffnete das erste Panel mit einem Beitrag über die Bestanderhaltung von digitalen Archivalien am Beispiel des Nachlasses des Literaturwissenschaftlers und Medientheoretikers Friedrich Kittler. Dabei verdeutlichte der Beiträger die vielfältigen Herausforderungen, die digitale Nachlässe über veraltete oder proprietäre Datei- und Textformate hinaus mit sich bringen. Gebrauchsspuren an Hardware, verschmutzte Datenträger oder selbst geschriebene Software der ehemaligen Anwender sind einige der sehr anschaulichen Fallbeispiele, die im Beitrag erwähnt wurden. SYBILLE SÖRING (Göttingen) stellte Textgrid und DARIAH als Infrastrukturen für digitale Editionen vor.[1] Textgrid stellt eine Arbeitsoberfläche für das – auch kollaborative – Auszeichnen von Text nach XML/TEI-P5 ebenso zur Verfügung als auch zahlreiche dabei unterstützende und analysierende Tools. DARIAH-DE unterstützt digital arbeitende Geistes- und Kulturwissenschaftler mit Digital-Humanities-Tools und fachwissenschaftlichen Diensten. Anhand des Editionsprojektes “Theodor Fontane: Notizbücher. Digitale genetisch-kritische und kommentierte Edition” erläutere die Referentin das Zusammenspiel der Infrastrukturen in den Bereichen der Erstellung, Präsentation und der nachhaltigen Verfügbarkeit.[2] PETER ANDORFER (Wien) erläuterte am Beispiel seines Editionsprojektes zur Weltbeschreibung des Tiroler Bauerns Leonhard Millinger die Vor- und Nachteile der Wolfenbütteler Digitalen Bibliothek (WDB) als Infrastruktur für die Erstellung einer digitalen Edition.[3] Die Rolle der Infrastruktur sieht Andorfer in einer generellen Unterstützung des Editionsvorhaben. Infrastrukturen können aber dem Editor nicht alle technischen und Kodierungsfragen und -entscheidungen abnehmen, eine “One-fits-all”-Lösung wird es alleine aufgrund der Spezifika von digitalen Editionen nicht geben können. Darüber hinaus betonte Andorfer, dass es für Editionen viel wichtiger sei, technische Ansprechpartner zu haben, die das Editionsvorhaben im Rahmen der gewählten Infrastruktur betreuen. Im ersten Teil seines Vortrages stellte ROLAND S. KAMZELAK (Marbach) die Hybrid-Edition der Tagebücher Harry Graf Kesslers vor. Ausgehend von der Edition wurde im zweiten Teil des Vortrags die interne Normdatenbank AMIE des Deutschen Literatur Archivs Marbach vorgestellt.[4] Die editionsübergreifende Datenbank ermöglicht es, direkt von den in ihr verzeichneten Registern in die Textstelle der jeweiligen Edition zu springen. Darüber hinaus verzeichnet die Datenbank die einzelnen Editionsrichtlinien. Der Vortrag zeigte überzeugend auf, wie arbeitserleichternd eine zentrale Datenhaltung und -pflege in Verbindung mit Normdaten für Editionsprojekte sein kann. In ihrem Beitrag stellte URSULA KUNDERT (Wolfenbüttel) anhand des Forschungsprojekts “Mediengeschichte der Psalmen” das Zusammenspiel von verschiedenen Infrastrukturen, zentralen Nachweissystemen und Social-Media-Angeboten dar. So entstand ein Abbild eines virtuellen Arbeitsplatzes, der sich auf verschiedene digitale Angebote erstreckt und das digitale Forschungsvorhaben mit dem Forschungsprofil des jeweiligen Forschers und dessen Einspeisung in fachspezifische Netzwerke unterstützt. Darüber hinaus wurde die Wichtigkeit einer intellektuellen Verbindung ausgehend von digitalen Editionen thematisiert. Nach dem ersten Panel fanden Kurzvorstellungen aktueller digitaler Editionsprojekte statt. HARTMUT BEYER (Wolfenbüttel) stellte die Edition des Tagebuches von Christian II. von Anhalt-Bernburg (1599–1656) vor. Die digitale Neuedition der deutschsprachigen Schwesternbücher des 14. Jahrhunderts wurde von CARINA HOFF (Trier) präsentiert. Danach stellten JULIA SCHMIDT-FUNKE und MARTIN PRELL (beide Jena) die digitale Edition der Briefe Erdmuthe Benignas von Reuß-Ebersdorf (1670–1732) vor. Das zweite Panel der Tagung eröffnete INGA HANNA RALLE (Wolfenbüttel) mit einem Vortrag, der einerseits das digitale Editionsvorhaben des Tagebuchs von Herzog August dem Jüngeren von Braunschweig-Wolfenbüttel und das damit in Verbindung stehende Selbstzeugnis-Repertorium der Herzog August Bibliothek vorstellte. Anderseits thematisierte der Vortrag die Bedeutung der Benutzbarkeit, Nutzerführung und Lesbarkeit von digitalen Editionen. Diese für die Nutzung von digitalen Editionen elementaren Faktoren werden noch nicht ausreichend bei der Editionserstellung berücksichtigt und stehen häufig hinter der Implementierung neuer technischer Methoden zurück. In dem nächsten Beitrag stellte ULRIKE HENNY (Köln) Reviewingverfahren für digitale Editionen vor. Dabei wurde die Rezensionszeitschrift RIDE vorgestellt und der von der Fachredaktion der Zeitschrift entwickelte Kriterienkatalog zur Besprechung von digitalen Editionen zur Diskussion gestellt.[5] Während Qualitätskriterien, die auch bei gedruckten Editionen angewendet werden, bei der Bewertung von digitalen Editionen adaptiert werden können, kommen zusätzlich noch weitere Faktoren hinzu, die vor allem aus dem Bereich der technischen Standards stammen. Zu Beginn des dritten Panels zeigte GEORG VOGELER (Graz) am Beispiel mittelalterlicher Rechnungsbücher das Potential der Digital Humanities und der sematischen Modellierung auf. Durch die Repräsentation von Text im Bild, durch das Mark-up von sprachlichen Informationen und die Auszeichnung von Bedeutung können unterschiedliche Zugänge zu editionskritischen Inhalten ermöglicht werden. Je nach wissenschaftlichem Blickwinkel schließen sich divergierende Ebenen somit nicht aus, sondern eröffnen neue Potenziale. Der Vortrag von JÖRG WETTLAUFER (Göttingen) ging auf die Möglichkeiten des Semantic Webs für die digitale Editionswissenschaft ein. Anhand zahlreicher Tools und Initiativen (LOD, RDF/SPARQL, Wikidata) zeigte er beispielsweise, wie eine automatische Generierung von Verknüpfungen aussehen kann, wo aber auch gleichzeitig Defizite der Qualitätssicherung und Herausforderungen liegen. Mit einem musikwissenschaftlichen Beitrag brachte JOACHIM VEIT (Paderborn) eine weitere fachliche Facette der digitalen Editionswissenschaft ein. Anhand von ausgewählten Beispielen wurde die Umsetzung von Musikeditionen demonstriert und auch die verschiedenen Entwicklungsschritte von ersten Prototypen bis zum aktuellen Stand aufgezeigt. Es stellte sich heraus, dass insbesondere das Feld der Musikeditionen, hier vor allem im Bereich der Visualisierung, von den Digital Humanities profitiert. GERRIT BRÜNING (Frankfurt am Main) diskutierte in seinem Beitrag das Verhältnis von Material und dessen digitaler Aufbereitung anhand der digitalen Faust-Edition.[6] Er thematisierte dabei das Verhältnis von analoger und digitaler Edition hinsichtlich Standards und kanonischer Vorbilder, die hier beispielsweise im Fall der “Weimarer Ausgabe” vorliegen. Es wurde deutlich, dass das Digitale hier Lösungen für die differenzierte Darstellung (Text-Genese vs. Dokument-Genese) bieten kann. Auch das dritte Panel schloss mit der Kurzvorstellung aktueller Editionsprojekte. BRITTA KLOSTERBERG (Halle) präsentierte die Aufbereitung der Tagebücher im Francke-Portal. CLAUDIA BAMBERG und JOCHEN STROBER (beide Marburg) zeigten den aktuellen Stand und Perspektiven bei der Briefedition A. W. Schlegels. Den Abschluss markierte die Präsentation von FRANZISKA DIEHR (Göttingen) zu einem Editionsprojekt, das Maya-Hieroglyphentexte digital aufbereitet. Die Tagungsteilnehmer waren sich darin einig, dass die Editionswissenschaft auf vielfache Weise von den Digital Humanities profitiert und sich durch die digitalen Methoden neue Editionsvorhaben eröffnen. Die Plenumsdiskussionen zwischen der Tagungsleitung und den Keynotespeakern machte aber auch deutlich, dass die grundsätzlichen, an digitale Editionsvorhaben zu stellenden Qualitätsansprüche sich an den traditionellen Standards orientieren müssen. Diese Kombination stellt die Editoren aber auch die Infrastruktureinrichtungen vor neue Herausforderungen. Dabei wurden insbesondere in den Bereichen der Qualitätsmessung, der Nachhaltigkeit, der Dissemination und der Visualisierung noch weiteres Potenzial für zukünftige Tagungen ausgemacht. Aber gerade diese Ergebnisse zeigen, dass es keine Trennung von analogen und digitalen Editoren geben darf, sondern dass die erfolgreiche Metamorphose der Editionswissenschaft in das digitale Zeitalter eine gemeinsame Aufgabe ist.'''


# In[ ]:


# Definition der Funktion zur Tokenisierung
def tokenize_text(source_text):
    
    for each in [".", ",", ";", "\"", "'", "/", "\\", "!", ":", "?", "(", ")", "[", "]"]:
        source_text = source_text.replace(str(each), "")
            
    lowered_text = source_text.lower()
    
    tokenized_text = lowered_text.split()
    
    return tokenized_text

print(tokenize_text(report))


# In[ ]:


# Definition der Funktion zur Segmentierung
def segment_text(text, segments):
    # segmentation
    segmented_text = []
    for i in range(0, len(tokenized_text), segments):
        segmented_text.append(tokenized_text[i:i + segments]) # i=0, 10, ...
    print('''Das Ergebnis der Segmentierung ist eine Liste von Sublisten, 
    die maximal so lang sind wie per Parameter \"segments\" spezifiziert: " , "\n" , segmented_text''')  
    print("\n")

    # insert newlines 
    for each in segmented_text:
        separator = "\n"
        each.append(separator)

    print("Das Ergebnis der Einfügung der Newlines sieht wie folgt aus: " , "\n" , segmented_text)  
    print("\n")

    # transform list into single string     
    segments = [] 
    for each in segmented_text:
        segments.append(" ".join(each[:]))
    output_text = "".join(segments[:])  

    return output_text

# Aufruf der Funktionen
tokenized_text = tokenize_text(report)
segmented_text = segment_text(tokenized_text, 10)
print("Der segmentierte Text sieht dann so aus:\n" + segmented_text)


# ## Lösung: Aufgabe Interaktives Programm gestalten
# 
# Schreiben Sie ein kleines interaktives Programm, das eine Liste von Namen erstellt, solange der:die Nutzer:in einen Eintrag hinzufügen möchte. Die Namen sollen als Tupel strukturiert sein und jeweils Vor- und Nachnamen enthalten. Zum Abschluss des Programms soll dem:der Nutzer:in die Liste bestehend aus Tupeln ausgegeben werden.
# 

# In[ ]:


# start programm with user input
input_data = input("Möchten Sie ein Namensverzeichnis erstellen? (J = ja, N = nein) ").lower()

# initialize empty list
list_of_names = []

# add names to list if and as long as input_data equals yes
if input_data == "j":
    while input_data == "j":
        first_name = input("Wie lautet der Vorname? ").lower()
        last_name = input("Wie lautet der Nachname? ").lower()
        names = (first_name, last_name) # create immutable tuple 
        list_of_names.append(names) # add tuple to list
        input_data = input("Möchten Sie einen weiteren Namen hinzufügen? (J = ja, N = nein) ").lower()
  # final notice
    print(f"Ihre Namensliste enthält die folgenden Einträge: {list_of_names}.\nVielen Dank! ")
else:
    print("Okay, dann nicht.")


# ## Lösungen: Aufgaben Sets 
# Zum Abschluss wollen wir noch einen genaueren Blick auf unsere Textdaten werfen. Wir können mit den in diesem und dem letzten Notebook gelernten Inhalten für jedes Wort ermitteln, wie oft es im Text vorkommt und die sogenannte *Vocabulary Density* berechnen.
# 
# ### a) Anzahl der Wörter in einem Text ermitteln
# Für diese Aufgabe benötigen wir Ihren in der [vorherigen Zwischenaufgabe tokenisierten Text](aufgabe-text-preprocessing). Schreiben Sie ein kleines Programm, das auf Basis dieses tokenisierten Textes zunächst ein Set generiert. Dann soll für jedes Wort in diesem Set ermittelt werden, wie oft es im von Ihnen tokenisierten Text vorkommt. Legen Sie das Wort zusammen mit seiner Vorkommenshäufigkeit als Tupel in einer Liste ab und geben Sie anschließend über eine formatierte `print`-Ausgabe diejenigen Wörter unter Angabe ihrer Vorkommenshäufigkeit aus, die häufiger als 5-mal im Text vorkommen.
# 
# Für die Bearbeitung dieser Aufgabe benötigen Sie `for`-Schleifen, `if`-Bedingungen und die Lerninhalte zu Listen und Tupeln.

# In[ ]:


# transform list into set
unique_words_report = set(tokenized_text) 
word_frequency_list = []

for word in unique_words_report:
    word_count = tokenized_text.count(word)
    word_frequency = (word, word_count)
    word_frequency_list.append(word_frequency)

for item in word_frequency_list:
    if item[1] >= 5:
        print(f"Das Wort \"{item[0]}\" kommt insgesamt {item[1]}-mal im Tagungsbericht vor.")


# ### b) Berechnung der Vocabulary Density auf Basis der Rohtextdaten
# 
# Die *Vocabulary Density* zeigt an, wie komplex ein Text ist. Die Dichte des Wortschatzes wird beispielsweise in der Computerlinguistik genutzt, um Texte zu analysieren. Sie beschreibt das Verhältnis der **Gesamtanzahl** der in einem Text enthaltenen Wörter zu den **einzigartigen Wörtern**. Mit dieser Metrik können Sie bestimmen, wie vielfältig ein Text auf sprachlicher Ebene ist und so den Wortschatz verschiedener Texte miteinander vergleichen, wobei die Länge der Texte zu berücksichtigen ist. 
# 
# Das Ergebnis der Berechnung zeigt Ihnen an, wie viele Wörter durchschnittlich gelesen werden müssen, bis ein neues Wort auftritt. Das heißt, je kleiner der Wert ist, desto komplexer ist der Text auf sprachlicher Ebene. Je größer der Wert ist, desto einfacher zu lesen ist der Text.
# 
# Schreiben Sie ein kleines Programm, das eine Funktion enthält, mit der diese auf **Division** beruhende Berechnung für Ihren im vorherigen Abschnitt eingelesenen und tokenisierten Text durchgeführt werden kann.

# In[ ]:


# your code
def compute_vocabulary_density(tokenized_text):
    """Parameter: list of strings
    The function returns float indicating the vocabulary density of a given tokenized text."""
    vocabulary_density =  len(set(tokenized_text)) / len(tokenized_text)
    return vocabulary_density

print(compute_vocabulary_density(tokenized_text))


# ## Lösung: Aufgabe Einfache Frequenzanalyse mit Python
# 
# Abschließend wollen wir auf Basis Ihres tokenisierten Textes ein kleines textanalytisches Programm gestalten, mit dem Sie die [absolute](https://de.wikipedia.org/wiki/Absolute_H%C3%A4ufigkeit) und [relative Frequenz](https://de.wikipedia.org/wiki/Relative_H%C3%A4ufigkeit) der in Ihrem Text enthaltenen Wörter ermitteln können. Die absolute Häufigkeit haben Sie bereits in der [Zwischenaufgabe zu den Sets](aufgaben-sets) ermittelt. Jetzt wollen wir die Funktionalitäten von Dictionaries dafür nutzen.
# 
# Als Basis benötigen Sie dazu wieder Ihren tokenisierten Text. Für die Berechnung der Frequenzen definieren Sie zwei Funktionen:
# - `count_absolute_frequency()`
#   - Diese Funktion sollte ein Dictionary zurückgeben, das pro Wort (*key*) die Anzahl seines Vorkommens im Text (*value*) abspeichert.
# - `count_relative_frequency()`
#   - Diese Funktion sollte ein Dictionary zurückgeben, das die ermittelten absoluten Häufigkeiten ins Verhältnis zur Gesamtlänge des Textes setzt. Zusätzlich können Sie die so ermittelten Werte mit 1000 (zur Ermittlung der Häufigkeit pro 1000 Token) oder 100 (zur Ermittlung des prozentualen Anteils) multiplizieren, was die Vergleichbarkeit der ermittelten Werte zwischen verschieden langen Texten erleichtert.
# 
# Geben Sie sowohl die absoluten als auch die relativen Häufigkeiten für Ihren Text aus.
# 
# **Hinweise:**
# - Nutzen Sie Schleifen und Bedingungen 
# - Für die Berechnung bei der ersten Funktion können Sie sich an Ihrer Herangehensweise im Abschnitt über Sets orientieren; bei der zweiten Funktion helfen Division und Multiplikation

# In[ ]:


# your code

# Funktionen definieren

def count_absolute_frequency(tokenized_text):
    """Parameter: list of strings
    The function returns a dictionary object containing the absolute frequency for
    each unique token in a given text."""

    # initialize empty dictionary
    frequencies = {}

    # compute absolute frequency
    for token in tokenized_text:
        if token in frequencies:
            frequencies[token] = frequencies[token] + 1
        else:
            frequencies[token] = 1
            
    print(frequencies)

    return frequencies

def count_relative_frequency(frequency_dict, tokenized_text, multiplyer):
    """Parameters: dictionary object of absolute frequencies; list of strings;
    integer, which determines the value for calculating the relative frequency
    (e.g. 100 for percentage or 1000 for "per 1000 words") 
    The function returns a dictionary object containing the relative frequency for
    each unique token in a given text."""

    # compute relative frequency
    for key in frequency_dict:
        frequency_dict[key] = (frequency_dict[key] / len(tokenized_text)) * multiplyer
    return frequency_dict

# Aufruf der Funktionen

absolute_frequencies_report = count_absolute_frequency(tokenized_text)
print("Ergebnis der Berechnung der absoluten Häufigkeit:\n", absolute_frequencies_report, "\n")

relative_frequencies_report = count_relative_frequency(absolute_frequencies_report, tokenized_text, 100)
print("Ergebnis der Berechnung der relativen Häufigkeit (in diesem Fall Prozent):\n", relative_frequencies_report)

