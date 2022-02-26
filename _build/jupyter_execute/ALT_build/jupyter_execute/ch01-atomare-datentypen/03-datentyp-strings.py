#!/usr/bin/env python
# coding: utf-8

# # Vertiefung der Arbeit mit Strings
# 
# Sie haben bereits mit der Indizierung, Verkettung und dem Ausschneiden einige Möglichkeiten kennengelernt, mit Strings zu arbeiten. Hier werden Ihnen überblickshaft noch eine Reihe weiterer Funktionen vorgestellt, die Sie zum Abschluss dieses Unterkapitels in Ihr zuvor gestaltetes Programm nach eigenem Ermessen einbinden und ausprobieren können.

# ## Länge von Strings bestimmen
# 
# Mit der Funktion [len()](https://docs.python.org/3/library/functions.html#len) kann die Anzahl der Elemente in einer Zeichenkette ermittelt werden.

# In[1]:


example_text = "Jemand musste Josef K. verleumdet haben, denn ohne dass er etwas Böses getan hätte, wurde er eines Morgens verhaftet."
len(example_text)


# ## Zählen
# Mit der auf ein String-Objekt angewendeten Funktion [count()](https://docs.python.org/3/library/stdtypes.html#str.count) kann gezählt werden, wie oft ein Element in dem Objekt vorhanden ist. 

# In[2]:


example_text.count("u")


# In[3]:


example_text.count("e")


# ## Finden
# Mit der auf ein String-Objekt angewendeten Funktion [find()](https://docs.python.org/3/library/stdtypes.html#str.find) kann ermittelt werden, an welcher Position im Objekt sich ein Element befindet. Die [Index-Funktion](https://docs.python.org/3/library/stdtypes.html#str.index) funktioniert auf ganz ähnliche Weise, mit dem Unterschied, dass statt einer "-1" eine Fehlermeldung ausgegeben wird, wenn ein gesuchter String sich nicht in der Zeichenkette befindet.

# In[4]:


print(example_text.find("u"))
print(example_text.index("u"))


# In[5]:


print(example_text.find("e"))
print(example_text.index("e"))


# In[6]:


print(example_text.find("ß"))
print(example_text.index("ß"))


# **Was fällt Ihnen einschränkend bei diesen Funktionen auf?** *Ihre Antwort*
# 
# 
# 
# 

# ## Strings ersetzen
# 
# Strings sind wie eingangs erwähnt grundsätzlich unveränderbar. Mit der auf ein String-Objekt angewendeten Funktion [replace()](https://docs.python.org/3/library/stdtypes.html#str.replace) kann aber gewissermaßen ein zu definierender Substring durch einen anderen ersetzt werden. Genau genommen wird hierbei die ursprüngliche Zeichenkette nicht verändert, sondern eine Kopie generiert und entsprechend der angegebenen Parameter verändert. Diese veränderte Kopie kann entweder den Wert der alten Variablen überschreiben oder einer neuen zugewiesen werden. Optional kann noch ein dritter Parameter, *count*, angegeben werden, der bestimmt, wie oft ein alter Teilstring durch einen neuen ersetzt werden soll. 

# In[19]:


# replace old substring with new input
name = input("What's your name? (press ENTER when finished)")
new_text = example_text.replace("Jemand", name)
print(new_text)


# In[20]:


# replace character four times
new_text = new_text.replace("e", "a", 4)
print(new_text)


# ## Wiederholungen
# 
# Analog zur Verkettung können Strings auch multipliziert werden, also gewissermaßen mit sich selbst konkateniert. Dazu wird das Multiplikations-Symbol genutzt.

# In[ ]:


new_text[:10] * 3


# ## Konkatenierung 
# 
# Die Zusammenfügung von Strings durch die "Addition" und "Multiplikation" haben wir nun schon kennengelernt. Es gibt noch eine weitere Variante, mit der Sie Zeichenketten auf eine sehr spezifische Weise verknüpfen können: [join()](https://docs.python.org/3/library/stdtypes.html#str.join). Die Funktion wird auf ein Stringobjekt angewendet und gibt eine Zeichenkette zurück, die um die Elemente eines sequenziellen Objekts angereichert wurde.
# 
# 

# In[ ]:


# demonstrate join-function
some_string = "spam"
concat_some_string = some_string.join("IN SERT")
print(concat_some_string)


# **Frage an Sie: Was ist bei dem Join-Vorgang passiert?** *Ihre Antwort*

# Die Join-Funktion kann auch auf leere Strings angewendet werden:

# In[ ]:


# demonstrate join-function with empty string
first_sentence = "Es war die beste und die schlimmste Zeit, ein Jahrhundert der Weisheit und des Unsinns, eine Epoche des Glaubens und des Unglaubens, eine Periode des Lichts und der Finsternis: es war der Frühling der Hoffnung und der Winter der Verzweiflung; wir hatten alles , wir hatten nichts vor uns; wir steuerten alle dem Himmel zu und auch alle unmittelbar in die entgegengesetzte Richtung – mit einem Wort, diese Zeit war der unsrigen so ähnlich, dass ihre geräuschvollsten Vertreter im guten wie im bösen nur den Superlativ auf sie angewendet haben wollten."
concat = "".join("Der erste Satz in Franz Kafkas 'Der Prozeß': " + example_text + " Der erste Satz in Charles Dickens' 'Eine Geschichte aus zwei Städten': " + first_sentence)
print(concat)


# Nützlich: Die nun ausgegebene Zeichenkette ist sehr lang. Sie zu lesen ist umständlich. Sie können durch das Einfügen von "\n" Zeilenumbrüche in Ihre Strings einbauen. Wandeln Sie das vorherige Beispiel so ab, dass nach dem ersten Satz von Kafkas "Der Prozeß" ein Zeilenumbruch erfolgt.

# In[ ]:


# your code


# ## Strings formatieren - ein Einstieg

# ### Groß- und Kleinschreibung ändern
# 
# Führen Sie den nachfolgenden Codeblock aus und ergänzen Sie anhand der Inspektion der Ausgabe als Kommentar im Codeblock die Funktionsweise der jeweiligen Funktionen.

# In[ ]:


# describe
example_text_upper = example_text.upper()

# describe
example_text_lower = example_text.lower()

# describe
example_text_swap = example_text.swapcase()

# describe
example_text_title = example_text.title()

# describe
example_text_capitalized = example_text.capitalize()

print(example_text_upper)
print(example_text_lower)
print(example_text_swap)
print(example_text_title)
print(example_text_capitalized)


# ### Ausgabe formatieren
# 
# Bislang sah die Ausgabe unserer Ergebnisse mit der Print-Funktion recht schmucklos aus. Python bietet für String-Objekte umfangreiche und komplexe Formatierungsmöglichkeiten. Für diese Lektion soll uns eine ganz einfache Herangehensweise genügen, die es ermöglicht, unsere Datenausgabe einzuordnen beziehungsweise zu strukturieren. Durch das Einfügen von geschweiften Klammern ("{}") in einen String wird dem Python-Interpreter kenntlich gemacht, dass an diesen Stellen etwas eingefügt werden soll. In die geschweiften Klammern können wir Positionsargumente setzen, die sich auf die der Format-Funktion übergebenen Parameter beziehen. Wenn keine Positionsargumente angegeben werden, die geschweiften Klammern also leer bleiben, dann wird die Reihenfolge der Parameter als maßgeblich angenommen.
# 
# **Ein Beispiel:**

# In[21]:


print("Der Beispieltext '{0}'\nist {1} Zeichen lang.".format(example_text, len(example_text)))


# Eine alternative Schreibweise, um Ausgaben zu formatieren, sind die sog. f-strings. Dem ersten Anführungszeichen wird ein f vorangestellt und in den geschweiften Klammern können die Variablen einfügt werden.

# In[29]:


print(f"Der Beispieltext '{example_text}'\nist {len(example_text)} Zeichen lang.")


# Ausführliche Informationen zu den Möglichkeiten der Formatierung von Strings finden Sie in der [Python-Dokumentation](https://docs.python.org/3/library/string.html#format-string-syntax).

# ### Aufgabe:
# 
# Überarbeiten Sie das von Ihnen am Ende von Kapitel 1.2.2 konzipierte Programm und beziehen Sie einige der neu dazu gekommenen Funktionen ein. Nutzen Sie insbesondere die Möglichkeit, die Ausgabe zu formatieren.

# In[ ]:


# your code

