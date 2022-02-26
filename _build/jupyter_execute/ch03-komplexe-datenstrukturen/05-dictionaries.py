#!/usr/bin/env python
# coding: utf-8

# ## [Dictionaries](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries)
# 
# Eine weitere zentrale Datenstruktur in Python, mit der Daten auf mächtige Art und Weise organisiert werden können, ist das sogenannte Dictionary. Sie können sich die Funktionsweise vorstellen wie bei Glossaren, Wörterbüchern oder Lexika: Auf Basis eines Schlüsselbegriffs können Sie unterschiedlich detailreiche Informationen zu diesem Begriff abrufen. 
# 
# Wie bei einer Liste handelt es sich um eine veränderbare Sammlung von potentiell unterschiedlichen Werten. Anders als bei Listen allerdings erfolgt der Zugriff nicht automatisch über Integers als Positionsangabe, sondern über die sogenannten *keys*, denn Dictionaries bestehen aus Schlüssel-Wert-Paaren (*key-value pairs*). Die *keys* können aus unterschiedlichen Datentypen bestehen. Für das jeweilige Dictionary müssen Sie allerdings einzigartig sein, damit unmissverständlich die gespeicherten Informationen abgerufen werden können.
# 
# Ein weiterer Unterschied zu Listen ist, dass Dicitionaries nicht geordnet sind. Während die Ordnung bei Listen durchaus ein Kriterium dafür ist, ob zwei Listen identisch sind, spielt dies für Dictionaries keine Rolle.
# 
# Wie bei Sets werden Dicitionaries durch geschweifte Klammern interpretierbar. Sie unterscheiden sich aber hinsichtlich der Organisation der jeweils gespeicherten Daten. Ein Dictionary kann wie folgt aussehen:

# In[1]:


books = {"Franz Kafka":"Der Prozess", "Charles Dickens":"Eine Geschichte aus zwei Städten", "J. K. Rowling":["Harry Potter und der Stein der Weisen", "Harry Potter und die Kammer des Schreckens", "Harry Potter und der Gefangene von Askaban"]}


# Mit dieser Codezeile wird ein Dictionary der Variablen `books` zugewiesen. Die Schlüssel (*keys*) sind in diesem Beispiel die Namen der Autor\*innen und die ihnen jeweils zugewiesenen Werte (*values*) sind korrespondierende Buchtitel. Die Zuordnung der Werte zu einem Schlüssel wird durch Doppelpunkte signalisiert, einzelne Instanzen sind durch Kommata voneinander abgegrenzt. Diese Struktur müssen Sie zur Unterscheidung von Sets beibehalten.
# 
# Anhand des Eintrags zu "J. K. Rowling" wird ersichtlich, dass sich auch Dictionaries verschachteln lassen. Eine Liste als korrespondierender Wert zu einem Schlüssel bietet sich bspw. dann an, wenn Sie mit geordneten Daten arbeiten wollen. Ein *key* kann aber auch weitere Dictionaries enthalten. Das ermöglicht Ihnen, komplexe Datenstrukturen flexibel zu modellieren.
# 
# Zugreifen können Sie nun auf diese Werte durch die Angabe des Schlüssels. Wie bei der Indizierung bei den bisher kennengelernten sequenziellen Datentypen werden auch hierzu eckige Klammern verwendet:[1]

# In[2]:


"Ein populäres Buch von Franz Kafka ist \"" + books["Franz Kafka"] + "\"."


# In[3]:


"Der erste Teil in der Harry-Potter-Reihe heißt \"" + books["J. K. Rowling"][0] + "\"."


# Wenn Sie auf einen Schlüssel zugreifen wollen, der nicht im Dictionary hinterlegt ist, dann erhalten Sie eine `KeyError`-Fehlermeldung -- ganz ähnlich den *out of range* `IndexError`-Fehlermeldungen bei Listen:

# In[4]:


"Albert Camus \"" + books["Albert Camus"] + "\" wird in der Coronakrise wieder viel gelesen."


# Falls wir das nicht vorhandene Schlüssel-Wert-Paar nun hinzufügen wollen, dann können wir dieselbe Notation verwenden, die wir auch für den Zugriff gebrauchen, und in Kombination mit dem Zuweisungssymbol entsprechende Inhalte integrieren:

# In[ ]:


books["Albert Camus"] = "Die Pest"
print(books["Albert Camus"])


# Das Dictionary `books` enthält nun ein Schlüssel-Wert-Paar bestehend aus "Albert Camus" und "Die Pest". Auf diese Weise können beliebige Einträge hinzugefügt oder auch bearbeitet werden.
# 
# **Anmerkung:**
# 
# [1] Der Backslash in den Zeichenketten dient dazu, Zeichen, die in Python nicht nur für sich selbst stehen, sondern eine besondere Funktion besitzen, wie in diesem Fall Anführungszeichen, von dieser Funktionalität zu entbinden. Das zweite Anführungszeichen in dieser Zeichenfolge `"\""` wird vom Interpreter dann lediglich als Satzzeichen interpretiert und nicht als Abschluss des Datentyps *string*.

# ### `keys()`, `values()` und `items()`
# 
# Mit den drei Methoden `keys()`, `values()` und `items()` werden listenähnliche Objekte erzeugt, die allerdings nicht modifizierbar sind. Sie bieten einen einfachen Zugriff auf die im Dictionary gespeicherten Daten. Notieren Sie im Kommentarbereich, was die Methoden im jeweiligen For-Loop machen:

# In[ ]:


#
print(type(books.keys()))
for key in books.keys():
    print(key)


# In[ ]:


#
print(type(books.values()))
for value in books.values():
    print(value)


# In[ ]:


# 
print(type(books.items()))
for item in books.items():
    print(item)


# Diese Methoden können auch genutzt werden, um zu prüfen, ob bestimmte Werte oder Schlüssel in einem Dictionary vorhanden sind. Dazu können wieder, wie schon bei der Arbeit mit Listen, die Operatoren `in` und `not in` genutzt werden. Prüfen Sie jeweils für *keys* und *values*, ob Inhalte im `books`-Dictionary enthalten sind:

# In[ ]:


# your code


# Sollten Sie mit richtigen Listen weiterarbeiten wollen, dann können Sie die listenähnlichen Rückgabewerte einfach `list()` übergeben:

# In[ ]:


authors = list(books.keys())
print(type(authors))


# ### `get()`
# 
# Die `get()`-Methode gibt den Wert für einen angegebenen Schlüssel zurück, wenn dieser im Dictionary existiert. Optional kann ein zweites Argument angegeben werden, das zurückgegeben werden soll, wenn der entsprechend angegebene Schlüssel fehlt. Per *default* wird `None` zurückgegeben, wenn kein Rückgabewert für diesen Fall spezifiziert wurde. 

# In[ ]:


print(books.get("Charles Dickens"))
print(books.get("Edgar Allan Poe"))
print(books.get("Edgar Allan Poe", "kein Eintrag"))


# ### Einträge entfernen
# 
# Auch für Dictionaries stehen mit dem `del`-Statement und `clear()` Möglichkeiten zur Verfügung, um einzelne Elemente eines Dictionaries zu entfernen oder den gesamten Inhalt zu löschen:

# In[ ]:


# delete entry on Albert Camus
del books["Albert Camus"]
print(books)


# In[ ]:


# remove all entries from dictionary
books.clear()
print(books)


# ### Aufgabe: Einfache Frequenzanalyse mit Python
# 
# Abschließend wollen wir auf Basis Ihres in 3.2.7 tokenisierten Textes ein kleines textanalytisches Programm gestalten, mit dem Sie die [absolute](https://de.wikipedia.org/wiki/Absolute_H%C3%A4ufigkeit) und [relative Frequenz](https://de.wikipedia.org/wiki/Relative_H%C3%A4ufigkeit) der in Ihrem Text enthaltenen Wörter ermitteln können. Die absolute Häufigkeit haben Sie bereits in der Zwischenaufgabe zu den Sets ermittelt. Jetzt wollen wir die Funktionalitäten von Dictionaries dafür nutzen.
# 
# Als Basis benötigen Sie dazu wieder Ihren in 3.2.7 tokenisierten Text. Für die Berechnung der Frequenzen definieren Sie zwei Funktionen:
# - `count_absolute_frequency()`: Diese Funktion sollte ein Dictionary zurückgeben, das pro Wort (*key*) die Anzahl seines Vorkommens im Text (*value*) abspeichert.
# - `count_relative_frequency()`: Diese Funktion sollte ein Dictionary zurückgeben, das die ermittelten absoluten Häufigkeiten ins Verhältnis zur Gesamtlänge des Textes setzt und zusätzlich bspw. mit 1000 multipliziert, um eine potentielle Vergleichbarkeit der ermittelten Werte zwischen verschieden langen Texten zu gewährleisten.
# 
# Geben Sie sowohl die absoluten als auch die relativen Häufigkeiten für Ihren Text aus.
# 
# **Hinweise:**
# - Nutzen Sie Schleifen und Bedingungen 
# - Für die Berechnung bei der ersten Funktion können Sie sich an Ihrer Herangehensweise in 3.4 orientieren; bei der zweiten Funktion helfen Division und Multiplikation

# In[ ]:


# your code


# 
# 
# ---
# 
# 

# **Abschlussbemerkung:** 
# 
# In diesem Notebook konnten wir Ihnen lediglich einen ersten Eindruck von der Arbeit mit Listen, Tupeln, Sets und Dictionaries vermitteln. Wenn Sie sich durch die Dokumentation zu den einzelnen Datenstrukturen durcharbeiten, werden Sie feststellen, dass die Möglichkeiten noch sehr viel umfangreicher sind. Es bietet sich an, sich bedarfsweise und anwendungsorientiert immer tiefer einzuarbeiten.
# 
# ![alt text](https://res.cloudinary.com/practicaldev/image/fetch/s--AHhADEXH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://pics.me.me/trying-to-learn-any-programming-language-100-just-a-little-7917454.png)
