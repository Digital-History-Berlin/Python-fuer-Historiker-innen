#!/usr/bin/env python
# coding: utf-8

# # Arbeiten mit Strings
# 
# :::{index} String
# :name: string
# :::
# 
# :::{admonition} Information
# :class: note 
# Aus Gründen der Lesbarkeit haben wir lange Strings, die im folgenden den Variablen zugewiesen werden, in drei einfache Anführungszeichen gesetzt. Auf diese Weise kann der String über mehrere Zeilen verlaufen und bleibt daher direkt lesbar, ohne dass die Leiste zum Scrollen bemüht werden muss.
# :::
# 
# :::{index} Indizierung
# :name: indizierung
# :::
# 
# :::{index} Slicing
# :name: slicing
# :::

# ## Eingabe
# 
# Im vorherigen Kapitel haben Sie den grundlegenden Aufbau von Code kennengelernt, und anhand des Datentyps *string* gelernt, wie Werte Variablen zugewiesen und ausgegeben werden können. Lassen Sie uns das Hallo-Welt-Programm aus dem vorherigen Kapitel nun etwas interaktiver gestalten, indem es uns nach unserem Namen fragt und persönlich begrüßt.

# In[ ]:


# hello user program

"""These few lines of code are 
used to greet you."""

my_variable = "Hello, World!" # assign value to variable

name = input("What's your name? (press ENTER when finished)")
print(my_variable[:7] + name)


# **Was haben wir gemacht?**
# 
# ::::{margin}
# :::{admonition} Wichtig!
# :class: note
# Die `input()`-Funktion liefert immer einen String zurück!
# :::
# ::::
# 
# :::{index} single: Funktion ; input()
# :name: input_
# :::
# 
# Neben verschiedenen Ausgabemöglichkeiten bietet Python auch einige **Eingabeoptionen**. Eine davon ist die [`input()`-Funktion](https://docs.python.org/3/library/functions.html#input) (siehe Zeile 8). Wird diese [Funktion](../ch02-programmablaeufe-strukturieren/04-funktionen.ipynb) im Programmdurchlauf aufgerufen, dann bleibt der Prozess solange angehalten bis die Nutzer:innen eine Eingabe über die Tastatur getätigt und mit der Return-Taste bestätigt haben. Die `input()`-Funktion nimmt den optionalen {term}`Parameter` *prompt* an, wodurch spezifiziert werden kann, welche Informationseingabe erwartet wird - im obigen Beispiel ein Name. Die Eingabe wird dann in der Variablen `name` gespeichert.
# 
# Als Ausgabe zeigt uns die `print()`-Funktion anschließend die "Summe" aus der "Addition" der in den Variablen `my_variable` und `name` gespeicherten Zeichenketten. Die Zusammenfügung von Strings durch das **+**-Zeichen wird auch {term}`Konkatenierung` oder {term}`Verkettung` genannt. Zeichenketten in Python sind prinzipiell unveränderbar ({term}`immutable`). Operationen, die eine Zeichenkette verändern sollen, geben daher stets eine *neue* Zeichenkette zurück. Wollten wir also, statt die zusammengefügte Zeichenkette per `print()` direkt auszugeben, stattdessen mit ihr weiterarbeiten, dann müssten wir sie einer neuen Variablen zuweisen oder die alte überschreiben.

# ## Indizierung und Slicing
# 
# Um eine Begrüßung aus dem Hello-World-Programm zu erstellen - wie im letzten Abschnitt geschehen - benötigen wir jedoch nur einen Teil der `Hello, World!`-Zeichenkette. Als Zeichenkette gehören Strings zu den sequentiellen Datentypen, d.h., sie stellen eine geordnete Folge von Elementen dar, den einzelnen Zeichen (*characters*). Durch diese Ordnung und Rangfolge ist es möglich, jedes einzelne Element des Strings über **Indices** direkt anzusteuern, indem die gewünschte Indexposition durch eckige Klammern angegeben wird: das "e" beispielsweise durch den Ausdruck `my_variable[1]`. 
# 
# Wundern Sie sich darüber, warum der zweite Buchstabe in der Zeichenkette an der Indexposition '1' steht? Schauen wir uns den String genauer an:
# 
# ![alt text](https://i.imgur.com/gGDkY0P.png)
# 
# ::::{margin}
# :::{admonition} Wichtig!
# :class: note
# Die Index-Zählung beginnt immer bei 0.
# :::
# ::::
# 
# Ein String ist von links nach rechts durchnummeriert. Die Zählung beginnt allerdings bei 0! Zeichenketten können auch umgekehrt gelesen werden, also von rechts nach links. Dann fangen wir bei -1 an. Auf diese Weise ist jedes Zeichen direkt ansteuerbar - auch Satzzeichen oder Leerzeichen, sogenannte *whitespaces*. Für unsere interaktive Abwandlung des Hallo-Welt-Programms haben wir in der Ausgabefunktion nur einen ganz bestimmten Wertbereich ausgewählt und zwar `Hello, `. Diesen Wertebereich können wir durch Nutzung der Indexpositionen ausschneiden (*slicing*).
# 
# Wie bei der Indizierung benutzen wir für das **Slicing** eckige Klammern, statt einem Wert benötigen wir allerdings eine Start- und eine Endposition. Führen Sie die folgenden Slicing-Anweisungen aus und erklären Sie die Funktionsweise.
# 

# In[ ]:


my_variable[1:5]


# *Ihre Erklärung*

# In[ ]:


my_variable[:7]


# *Ihre Erklärung*

# In[ ]:


my_variable[4:]


# *Ihre Erklärung*

# In[ ]:


my_variable[:]


# *Ihre Erklärung*

# In[ ]:


my_variable[2:-6]


# *Ihre Erklärung*

# In[ ]:


my_variable[0:12:2]


# *Ihre Erklärung*

# Üben wir das Ausschneiden von Strings noch ein wenig.

# In[ ]:


example_text = '''Jemand musste Josef K. verleumdet haben, 
                  denn ohne dass er etwas Böses getan hätte, 
                  wurde er eines Morgens verhaftet.'''

# schneiden Sie die Zeichenfolge "Josef K." aus


# schneiden Sie das letzte Wort aus


# schneiden Sie ab "denn" (also mit d beginnend) jedes 3. Zeichen aus


# :::{index} single: Funktion ; len()
# :name: len_
# :::
# 
# ## Länge von Strings bestimmen
# 
# Nachdem Sie nun wissen, wie Strings aufgebaut sind und einzelne Elemente in ihnen angesteuert werden können, wollen wir uns nun einige Funktionen anschauen, mit denen die Zeichenketten beschrieben und bearbeitet werden können. Den Anfang macht die Funktion [`len()`](https://docs.python.org/3/library/functions.html#len). Sie wird genutzt, um die Anzahl der Elemente in einem sequenziellen Datentypen zu ermitteln.

# In[ ]:


example_text = '''Jemand musste Josef K. verleumdet haben, 
                  denn ohne dass er etwas Böses getan hätte, 
                  wurde er eines Morgens verhaftet.'''
len(example_text)


# :::{index} single: Funktion ; count()
# :name: count_
# :::
# 
# ## Zählen
# Mit der auf ein String-Objekt angewendeten Funktion [`count()`](https://docs.python.org/3/library/stdtypes.html#str.count) kann gezählt werden, wie oft ein Element in dem Objekt vorhanden ist. 

# In[ ]:


example_text.count("u")


# In[ ]:


example_text.count("e")


# :::{index} single: Funktion ; find()
# :name: find_
# :::
# 
# :::{index} single: Funktion ; index()
# :name: index_
# :::
# 
# ## Finden
# Mit der auf ein String-Objekt angewendeten Funktion [`find()`](https://docs.python.org/3/library/stdtypes.html#str.find) kann ermittelt werden, an welcher Position im Objekt sich ein Element befindet. Die [`index()`-Funktion](https://docs.python.org/3/library/stdtypes.html#str.index) funktioniert auf ganz ähnliche Weise, mit dem Unterschied, dass statt einer '-1' eine Fehlermeldung ausgegeben wird, wenn ein gesuchter String sich nicht in der Zeichenkette befindet.

# In[ ]:


print(example_text.find("u"))
print(example_text.index("u"))


# In[ ]:


print(example_text.find("e"))
print(example_text.index("e"))


# In[ ]:


print(example_text.find("ß"))
print(example_text.index("ß"))


# **Was fällt Ihnen einschränkend bei diesen Funktionen auf?** 
# 
# *Ihre Antwort*

# In[ ]:


# your answer


# :::{index} single: Funktion ; replace()
# :name: replace_
# :::
# 
# ## Strings ersetzen
# 
# Strings sind wie eingangs erwähnt grundsätzlich unveränderbar. Mit der auf ein String-Objekt angewendeten Funktion [`replace()`](https://docs.python.org/3/library/stdtypes.html#str.replace) kann aber gewissermaßen ein zu definierender Substring durch einen anderen ersetzt werden. Genau genommen wird hierbei die ursprüngliche Zeichenkette nicht verändert, sondern eine Kopie generiert und entsprechend der angegebenen {term}`Parameter` verändert. Diese veränderte Kopie kann entweder den Wert der alten Variablen überschreiben oder einer neuen Variablen zugewiesen werden. Optional kann noch ein dritter Parameter, *count*, angegeben werden, der bestimmt, wie oft ein alter Teilstring durch einen neuen ersetzt werden soll. 

# In[ ]:


# replace old substring with new input
name = input("What's your name? (press ENTER when finished)")
new_text = example_text.replace("Jemand", name)
print(new_text)


# In[ ]:


# replace character four times
new_text = new_text.replace("e", "a", 4)
print(new_text)


# ## Wiederholungen
# 
# Analog zur Verkettung können Strings auch multipliziert, also gewissermaßen mit sich selbst konkateniert werden. Dazu wird das Multiplikations-Symbol genutzt.

# In[ ]:


new_text[:10] * 3


# :::{index} single: Funktion ; join()
# :name: join_
# :::
# 
# ## Konkatenierung 
# 
# Die Zusammenfügung von Strings durch die "Addition" und "Multiplikation" haben wir nun schon kennengelernt. Es gibt noch eine weitere Variante, mit der Sie Zeichenketten auf eine sehr spezifische Weise verknüpfen können: [`join()`](https://docs.python.org/3/library/stdtypes.html#str.join). Die Funktion wird auf ein String-Objekt angewendet und gibt eine Zeichenkette zurück, die um die Elemente eines sequenziellen Objekts angereichert wurde.
# 
# 

# In[ ]:


# demonstrate join-function
some_string = "spam"
concat_some_string = some_string.join("IN SERT")
print(concat_some_string)


# **Frage an Sie: Was ist bei dem Join-Vorgang passiert?**

# Die `join()`-Funktion kann auch auf leere Strings angewendet werden:

# In[ ]:


# demonstrate join-function with empty string
first_sentence = '''Es war die beste und die schlimmste Zeit, 
                    ein Jahrhundert der Weisheit und des Unsinns, 
                    eine Epoche des Glaubens und des Unglaubens, 
                    eine Periode des Lichts und der Finsternis: 
                    es war der Frühling der Hoffnung und der Winter der Verzweiflung; 
                    wir hatten alles, wir hatten nichts vor uns; 
                    wir steuerten alle dem Himmel zu und auch alle unmittelbar in die 
                    entgegengesetzte Richtung – mit einem Wort, 
                    diese Zeit war der unsrigen so ähnlich, 
                    dass ihre geräuschvollsten Vertreter im guten wie im bösen nur 
                    den Superlativ auf sie angewendet haben wollten.'''
concat = "".join("Der erste Satz in Franz Kafkas 'Der Prozeß': "                     + example_text +                     " Der erste Satz in Charles Dickens' 'Eine Geschichte aus zwei Städten': "                     + first_sentence)
print(concat)


# Die nun ausgegebene Zeichenkette ist sehr lang. Sie zu lesen ist umständlich. Sie können durch das Einfügen von `\n` Zeilenumbrüche in Ihre Strings einbauen. Wandeln Sie das vorherige Beispiel so ab, dass zwischen dem ersten Satz von Kafkas "Der Prozeß" und dem ersten Satz von Dickens zwei Zeilenumbrüche erfolgen.

# In[ ]:


# your code


# :::{index} single: Funktion ; upper()
# :name: upper_
# :::
# 
# :::{index} single: Funktion ; lower()
# :name: lower_
# :::
# 
# 
# :::{index} single: Funktion ; swapcase()
# :name: swapcase_
# :::
# 
# :::{index} single: Funktion ; title()
# :name: title_
# :::
# 
# :::{index} single: Funktion ; capitalize()
# :name: capitalize_
# :::
# 
# ## Strings formatieren
# 
# ### Groß- und Kleinschreibung ändern
# 
# Führen Sie den nachfolgenden Codeblock aus und ergänzen Sie anhand der Inspektion der Ausgabe als Kommentar im {term}`Codeblock` die Funktionsweise der jeweiligen Funktionen.

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


# :::{index} Ausgabe formatieren
# :name: ausgabe_formatieren
# :::
# 
# ## Ausgabe formatieren
# 
# Bislang sah die Ausgabe unserer Ergebnisse mit der `print()`-Funktion recht schmucklos aus. Python bietet für String-Objekte umfangreiche und komplexe Formatierungsmöglichkeiten. Für diesen Abschnitt soll uns eine ganz einfache Herangehensweise genügen, die es ermöglicht, unsere Datenausgabe einzuordnen beziehungsweise zu strukturieren. Durch das Einfügen von geschweiften Klammern (`{}`) in einen String wird dem Python-Interpreter kenntlich gemacht, dass an diesen Stellen etwas eingefügt werden soll. In die geschweiften Klammern können wir Positionsargumente setzen, die sich auf die der Format-Funktion übergebenen Parameter beziehen. Wenn keine Positionsargumente angegeben werden, die geschweiften Klammern also leer bleiben, dann wird die Reihenfolge der Parameter als maßgeblich angenommen.
# 
# **Ein Beispiel:**

# In[ ]:


print("Der Beispieltext '{0}'\nist {1} Zeichen lang.".format(example_text, len(example_text)))


# ::::{margin}
# :::{admonition} Hinweis
# :class: note
# In diesem Jupyter Book werden f-strings zur Formatierung von Strings genutzt.
# :::
# ::::
# 
# :::{index} f-strings
# :name: f-strings
# :::
# 
# **f-strings**
# 
# Eine alternative Schreibweise, um Ausgaben zu formatieren, sind die sog. f-strings. Dem ersten Anführungszeichen wird ein `f` vorangestellt und in den geschweiften Klammern können die Variablen direkt eingefügt werden. 

# In[ ]:


print(f"Der Beispieltext '{example_text}'\nist {len(example_text)} Zeichen lang.")


# Ausführliche Informationen zu den Möglichkeiten der Formatierung von Strings finden Sie in der [Python-Dokumentation](https://docs.python.org/3/library/string.html#format-string-syntax).

# ## Aufgabe: Skript überarbeiten
# 
# Überarbeiten Sie das von Ihnen am Ende des letzten Abschnitts [konzipierte Skript](aufgabe-skript-schreiben) und beziehen Sie einige der neu dazu gekommenen Funktionen ein. Nutzen Sie insbesondere die Möglichkeit, die Ausgabe zu formatieren.

# In[ ]:


# your code

