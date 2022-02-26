#!/usr/bin/env python
# coding: utf-8

# ## [Sets](https://docs.python.org/3.7/tutorial/datastructures.html#sets)
# 
# Auch für Mengen gibt es in Python einen Datentyp: das `set`. Mengen sind ungeordnete Sammlungen von Objekten ohne doppelte Einträge. Sie sind dann relevant, wenn nicht die Position oder Anzahl eines Elements von Relevanz ist, sondern sein bloßes Vorkommen. Ein Anwendungsbeispiel: Wenn Sie zum Beispiel wissen möchten, wie viele einzigartige Wörter in Ihrem unter 3.2.7 bearbeiteten Text enthalten sind, dann können Sie ihn in ein Set umwandeln. Im nachfolgenden Codeblock demonstrieren wir das einmal anhand unseres Beispieltextes:

# In[1]:


# data
report = "Die Editionswissenschaft erlebt nicht zuletzt wegen einer erfolgreichen Kombination von traditionellen Arbeitsweisen mit Methoden der Digital Humanities einen regelrechten Hype. Digitale Methoden drängen sich besonders an den Stellen auf, wo sie eine Überwindung der Beschränkungen des analogen Drucks versprechen. Zugleich zeichnet sich ab, dass mit einem Wechsel zu digitalen Editionsformen nicht nur neue Werkzeuge genutzt werden, sondern dass sich prinzipielle strukturelle Änderungen ergeben: so können analoge Editionen angereichert werden oder Editionen können als Hybrid durch eine gleichwertige digitale und analoge Version repräsentiert werden. Editoren werden angesichts dieser neuen Möglichkeiten vor neue Herausforderungen gestellt. Gleiches gilt für Infrastrukturen, die die Produkte der Editionswissenschaft publizieren und langfristig verfügbar machen sollen. Grundlegende Fragen der Qualitätsmessung und -bewertung, der Arbeitsorganisation, Vernetzung und Distribution müssen bei der digitalen Editionswissenschaft anders bzw. neu gestellt und bewertet werden. Die vom Forschungsverbund Marbach Weimar Wolfenbüttel veranstaltete Tagung “Digitale Metamorphose: Digital Humanities und Editionswissenschaft” betrachtete diese neuen Möglichkeiten kritisch und ging dabei auch der Frage nach, welche Grenzen und Gefahren es jenseits der offensichtlichen Vorteile für die Editionswissenschaft gibt."

# split text into list of words
tokenized_report = report.split()

# compute and print length of report
print("Der Tagungsbericht zur Veranstaltung \"Digitale Metamorphose. Digital Humanities und Editionswissenschaft\" enthält insgesamt {} Wörter.".format(len(tokenized_report)))

# transform list into set
unique_words_report = set(tokenized_report)

# compute and print length of set
print("Der Tagungsbericht zur Veranstaltung \"Digitale Metamorphose. Digital Humanities und Editionswissenschaft\" enthält {} verschiedene Wörter.".format(len(unique_words_report)))

# print set
print(unique_words_report)


# Wie Sie sehen werden Sets durch geschweifte Klammern eingeleitet und abgeschlossen. Sie können mit der Funktion `set()` erstellt werden. Übergeben Sie der Methode keine Werte, wird eine leere Menge erstellt. 
# 
# **Wichtig:** Leere Sets können nicht einfach mit `{}` erstellt werden. Diese Art und Weise ist für Dictionaries vorgesehen, eine Datenstruktur, die wir im nächsten Abschnitt kennenlernen werden.
# 
# Sets eignen sich auch zur effizienten Prüfung, ob Elemente in einer Menge vorhanden sind. Dazu können wir wieder auf Operatoren wie `in` oder `not in` zurückgreifen:

# In[2]:


print("mining" in unique_words_report)
print("text" not in unique_words_report)


# ### Aufgaben: 
# Zum Abschluss wollen wir noch einen genaueren Blick auf unsere Textdaten werfen. Wir können mit den in diesem und dem letzten Notebook gelernten Inhalten für jedes Wort ermitteln, wie oft es im Text vorkommt und die sogenannte *Vocabulary Density* berechnen.
# 
# #### a) Anzahl der Wörter in einem Text ermitteln
# Für diese Aufgabe benötigen wir Ihren in der Zwischenaufgabe 3.2.7 tokenisierten Text. Schreiben Sie ein kleines Programm, das auf Basis dieses tokenisierten Textes zunächst ein Set generiert. Dann soll für jedes Wort in diesem Set ermittelt werden, wie oft es im von Ihnen tokenisierten Text vorkommt. Legen Sie das Wort zusammen mit seiner Vorkommenshäufigkeit als Tupel in einer Liste ab und geben Sie anschließend über eine formatierte `print`-Ausgabe diejenigen Wörter unter Angabe ihrer Vorkommenshäufigkeit aus, die häufiger als 5-mal im Text vorkommen.
# 
# Für die Bearbeitung dieser Aufgabe benötigen Sie `for`-Schleifen, `if`-Bedingungen und die Lerninhalte zu Listen und Tupeln.

# In[3]:


# your code


# #### b) Berechnung der Vocabulary Density auf Basis der Rohtextdaten
# 
# Die *Vocabulary Density* zeigt an, wie komplex ein Text ist. Die Dichte des Wortschatzes wird beispielsweise in der Computerlinguistik genutzt, um Texte zu analysieren. Sie beschreibt das Verhältnis der **Gesamtanzahl** der in einem Text enthaltenen Wörter zu den **einzigartigen Wörtern**.[1] Mit dieser Metrik können Sie bestimmen, wie vielfältig ein Text auf sprachlicher Ebene ist und so den Wortschatz verschiedener Texte miteinander vergleichen, wobei die Länge der Texte zu berücksichtigen ist. 
# 
# Das Ergebnis der Berechnung zeigt Ihnen an, wie viele Wörter durchschnittlich gelesen werden müssen, bis ein neues Wort auftritt. Das heißt, je kleiner der Wert ist, desto komplexer ist der Text auf sprachlicher Ebene. Je größer der Wert ist, desto einfacher zu lesen ist der Text.
# 
# Schreiben Sie ein kleines Programm, das eine Funktion enthält, mit der diese auf **Division** beruhende Berechnung für Ihren in 3.2.7 eingelesenen und tokenisierten Text durchgeführt werden kann.  

# In[4]:


# your code


# **Anmerkung:**
# 
# [1] Die Berechnung dieses Verhältnisses wird aussagekräftiger, wenn man die eingespeisten Inputdaten einer [*Lemmatisierung*](https://de.wikipedia.org/wiki/Lemma_(Lexikographie)) unterzieht, das heißt, dass alle in dem Text enthaltenen Wörter auf ihre Grundform reduziert werden. Ein Beispiel: i) aus "war", "werden" und "ist" wird "sein", ii) aus "historischer", "historisches", "historischem" oder "historische" wird "historisch". Für solche sprachverarbeitenden Aufgaben gibt es zusätzliche Python-Bibliotheken (bspw. `spaCy` oder `nltk`), die eine Reihe von Funktionen enthalten, die Sie einfach in Ihren Code einbauen können. Wie externe Bibliotheken in den Code integriert werden, werden wir in den kommenden Übungseinheiten lernen.
