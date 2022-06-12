#!/usr/bin/env python
# coding: utf-8

# # [Sets](https://docs.python.org/3.7/tutorial/datastructures.html#sets)
# 
# :::{index} Set
# :name: set
# ::: 
# 
# Auch für Mengen gibt es in Python einen Datentyp: das Set. Mengen sind ungeordnete Sammlungen von Objekten ohne doppelte Einträge. Sie sind dann relevant, wenn nicht die Position oder Anzahl eines Elements von Relevanz ist, sondern sein bloßes Vorkommen. Ein Anwendungsbeispiel: Wenn Sie zum Beispiel wissen möchten, wie viele einzigartige Wörter in einem Text enthalten sind, dann können Sie ihn in ein Set umwandeln. Im nachfolgenden Codeblock demonstrieren wir das einmal anhand unseres Beispieltextes.

# ## Sets erstellen

# In[ ]:


report = '''Die Editionswissenschaft erlebt nicht zuletzt wegen einer 
            erfolgreichen Kombination von traditionellen Arbeitsweisen 
            mit Methoden der Digital Humanities einen regelrechten Hype. 
            Digitale Methoden drängen sich besonders an den Stellen auf, 
            wo sie eine Überwindung der Beschränkungen des analogen Drucks versprechen. 
            Zugleich zeichnet sich ab, dass mit einem Wechsel zu digitalen Editionsformen 
            nicht nur neue Werkzeuge genutzt werden, sondern dass sich prinzipielle 
            strukturelle Änderungen ergeben: so können analoge Editionen angereichert 
            werden oder Editionen können als Hybrid durch eine gleichwertige digitale und 
            analoge Version repräsentiert werden. Editoren werden angesichts dieser neuen
            Möglichkeiten vor neue Herausforderungen gestellt. Gleiches gilt für Infrastrukturen, 
            die die Produkte der Editionswissenschaft publizieren und langfristig 
            verfügbar machen sollen. Grundlegende Fragen der Qualitätsmessung 
            und -bewertung, der Arbeitsorganisation, Vernetzung und Distribution 
            müssen bei der digitalen Editionswissenschaft anders bzw. neu gestellt 
            und bewertet werden. Die vom Forschungsverbund Marbach Weimar Wolfenbüttel 
            veranstaltete Tagung “Digitale Metamorphose: Digital Humanities und Editionswissenschaft” 
            betrachtete diese neuen Möglichkeiten kritisch und ging dabei auch der Frage nach, 
            welche Grenzen und Gefahren es jenseits der offensichtlichen Vorteile für 
            die Editionswissenschaft gibt.'''


# In[ ]:


# split text into list of words
tokenized_report = report.split()

# compute and print length of report
print(f'''Der Tagungsbericht "Digitale Metamorphose. Digital Humanities und Editionswissenschaft" 
enthält insgesamt {len(tokenized_report)} Wörter.''')

# transform list into set
unique_words_report = set(tokenized_report)

# compute and print length of set
print(f'''Der Tagungsbericht "Digitale Metamorphose. Digital Humanities und Editionswissenschaft" 
enthält {len(unique_words_report)} verschiedene Wörter.''')

# print set
print(unique_words_report)


# Ganz exakt ist die Liste der Wörter nicht. Dies liegt daran, dass wir eine ganz einfache Tokenisierung auf Basis der Whitespaces durchgeführt und einige vorverarbeitende Schritte noch nicht implementiert haben. So tauchen 'digitale', '"Digitale' und 'Digitale' als eigenständige Worteinheiten auf, gleiches gilt beispielsweise auch für 'Editionswissenschaft' (ohne Anführungszeichen) und 'Editionswissenschaft"' (mit Anführungszeichen).
# 
# Nachfolgend finden Sie daher ein kurzes Skript, dass mit den bisher bekannten Möglichkeiten auf Wortebene prüft, ob ein Token Zeichensetzung enthält und diese ggf. entfernt. Zugleich werden die Wörter in Kleinschreibung konvertiert und die Liste als Set umgewandelt, um dessen Länge dann genauer zu bestimmen. Für das Vorgehen, das hier mit Hilfe von zwei Schleifen und if-Abfragen gelöst ist, existieren in bestimmten Python-Libraries bereits vorgefertigte Funktionen, die Sie in späteren Kapiteln noch kennenlernen werden.

# In[ ]:


# create empty list
cleaned_tokenized_report = []

# check for every word if any character in word is punctuation
for word in tokenized_report:
    for character in word:
        if character == '”' or character =='“' or character ==':'         or character =='.' or character ==',':
            word = word.replace(character,'') # replace punctuation with empty string
    cleaned_tokenized_report.append(word.lower()) # append lowercased word to list


# In[ ]:


# compute and print length of set
print(f'''Der gesäuberte Tagungsbericht "Digitale Metamorphose. Digital Humanities und Editionswissenschaft" 
enthält {len(set(cleaned_tokenized_report))} verschiedene Wörter.''')

# print set
print(set(cleaned_tokenized_report))


# :::{index} single: Funktion ; set()
# :name: set_
# :::
# 
# ::::{margin}
# :::{admonition} Wichtig!
# :class: note
# Leere Sets können nicht einfach mit `{}` erstellt werden. Diese Art und Weise ist für Dictionaries vorgesehen.
# :::
# ::::
# 
# Wie Sie jedoch sehen, werden Sets durch geschweifte Klammern `{}` eingeleitet und abgeschlossen. Sie können mit der Funktion `set()` erstellt werden. Übergeben Sie der Methode keine Werte, wird eine leere Menge erstellt. 
# 
# Sets eignen sich auch zur effizienten Prüfung, ob Elemente in einer Menge vorhanden sind. Dazu können wir wieder auf Operatoren wie `in` oder `not in` zurückgreifen:

# In[ ]:


print("mining" in unique_words_report)
print("text" not in unique_words_report)


# (aufgaben-sets)=
# ## Aufgaben Sets
# 
# Abschliessend wollen wir noch einen genaueren Blick auf unsere Textdaten werfen. Wir können mit den in diesem und dem letzten Abschnitt gelernten Inhalten für jedes Wort ermitteln, wie oft es im Text vorkommt und die sogenannte *Vocabulary Density* berechnen.
# 
# ### a) Anzahl der Wörter in einem Text ermitteln
# Für diese Aufgabe benötigen wir Ihren in der [vorherigen Zwischenaufgabe tokenisierten Text](aufgabe-text-preprocessing). Schreiben Sie ein kleines Programm, das auf Basis dieses tokenisierten Textes zunächst ein Set generiert. Dann soll für jedes Wort in diesem Set ermittelt werden, wie oft es im von Ihnen tokenisierten Text vorkommt. Legen Sie das Wort zusammen mit seiner Vorkommenshäufigkeit als Tupel in einer Liste ab und geben Sie anschließend über eine formatierte `print()`-Ausgabe diejenigen Wörter unter Angabe ihrer Vorkommenshäufigkeit aus, die häufiger als 5-mal im Text vorkommen.
# 
# Für die Bearbeitung dieser Aufgabe benötigen Sie [`for`-Schleifen](for-schleife), [`if`-Bedingungen](bedingte_abfragen) und die Lerninhalte zu [Listen](liste) und [Tupeln](tupel).

# In[ ]:


# your code


# :::{index} Vocabulary Density
# :name: vocabulary_density
# :::
# 
# ### b) Berechnung der Vocabulary Density auf Basis der Rohtextdaten
# 
# Die *Vocabulary Density* zeigt an, wie komplex ein Text ist. Die Dichte des Wortschatzes wird beispielsweise in der Computerlinguistik genutzt, um Texte zu analysieren. Sie beschreibt das Verhältnis der **Gesamtanzahl** der in einem Text enthaltenen Wörter zu den **einzigartigen Wörtern**.[^fn1] Mit dieser Metrik können Sie bestimmen, wie vielfältig ein Text auf sprachlicher Ebene ist und so den Wortschatz verschiedener Texte miteinander vergleichen, wobei die Länge der Texte zu berücksichtigen ist. 
# 
# Das Ergebnis der Berechnung zeigt Ihnen an, wie viele Wörter durchschnittlich gelesen werden müssen, bis ein neues Wort auftritt. Das heißt, je kleiner der Wert ist, desto komplexer ist der Text auf sprachlicher Ebene. Je größer der Wert ist, desto einfacher ist der Text zu lesen.
# 
# Schreiben Sie ein kleines Programm, das eine Funktion enthält, mit der diese auf **Division** beruhende Berechnung für Ihren im vorherigen Abschnitt eingelesenen und tokenisierten Text durchgeführt werden kann.  

# In[ ]:


# your code


# [^fn1]: Die Berechnung dieses Verhältnisses wird aussagekräftiger, wenn man die eingespeisten Inputdaten einer [*Lemmatisierung*](https://de.wikipedia.org/wiki/Lemma_(Lexikographie)) unterzieht, das heißt, dass alle in dem Text enthaltenen Wörter auf ihre Grundform reduziert werden. Dazu zwei Beispiele zur Veranschaulichung: 1) aus "war", "werden" und "ist" wird "sein", 2) aus "historischer", "historisches", "historischem" oder "historische" wird "historisch". Für solche sprachverarbeitenden Aufgaben gibt es zusätzliche Python-Bibliotheken (bspw. `spaCy` oder `nltk`), die eine Reihe von Funktionen enthalten, die Sie einfach in Ihren Code einbauen können. Wie externe Bibliotheken in den Code integriert werden, werden wir in den kommenden Kapiteln lernen.
