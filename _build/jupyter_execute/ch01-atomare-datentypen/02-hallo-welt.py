#!/usr/bin/env python
# coding: utf-8

# # Hallo, Welt!
# 
# :::{admonition} Wichtiger Hinweis!
# :class: note
# **Führen Sie bitte alle Beispiel-Codeblöcke aus, da diese aufeinander aufbauen.**
# 
# Wenn Sie die Codezellen des Jupyter Book mit {term}`Live Code` aktiviert haben, dann klicken Sie auf die Schaltfläche 'run'.
# 
# Wenn Sie die Notebooks mit {term}`Binder` bearbeiten, können Sie die ausgewählte Codezelle ausführen, indem Sie 'SHIFT' und 'ENTER' drücken oder auf die Playtaste klicken.
# :::

# In[ ]:


# hello world program

"""These few lines of code are 
used to display the text "Hello, World!"."""

my_variable = "Hello, World!" # assign value to variable
print(my_variable)


# Anhand des obigen, obligatorischen [Hallo-Welt-Programms](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program), das in keiner Programmier-Einführung fehlen darf, können wir schon einige grundlegende Funktionsweisen von Python ablesen und zugleich testen, ob die Programmierumgebung ordnungsgemäß funktioniert. Das Programm macht im Prinzip nichts anderes, als Ihnen die Zeichenkette `Hello, World!` auf dem Bildschirm auszugeben. 

# **Funktionsweise**
# 
# Der Code wird vom Rechner Zeile für Zeile ausgeführt. Jede Zeile kann potentiell eine {term}`Anweisung` (*statement*) enthalten, die dem Rechner sagt, was zu tun ist. Die Reihenfolge der einzelnen Anweisungen ist zentral. Es gibt einfache und komplexe Anweisungen, die Sie nach und nach in den nachfolgenden Abschnitten und Lektionen kennenlernen werden.
# 
# :::{index} Kommentar
# :name: kommentar
# :::
# 
# Neben den Anweisungen können Programmcodes **Kommentare** enthalten, wie in den Zeilen 1, 3 und 4 unseres Beispielcodes zu sehen. Kommentare können und sollten dazu genutzt werden, Code-Schnipsel hinsichtlich ihrer Funktionalität zu erläutern. Mit der Raute (`#`) kann ein einfacher einzeiliger Kommentar geschrieben werden. Sobald der Interpreter auf die Raute stößt, wird der Text nicht mehr als auszuführender Code interpretiert und von der Maschine ignoriert. Möchte man über mehrere Zeilen kommentieren, dann kann man entweder in jede Zeile eine Raute setzen oder man nutzt dreimal einfache (`'`) beziehungsweise dreimal doppelte (`"`) Anführungszeichen. Die letzte Variante wird üblicherweise für die {term}`Dokumentation` genutzt. Als {term}`docstrings` werden sie Ihnen in späteren Übungseinheiten wiederbegegnen, wenn **Funktionen** oder **Klassen** definiert und erklärt werden müssen. Die Kommentare dienen zur Kommunikation mit den Codeleser:innen.
# 
# :::{index} Variable
# :name: variable
# :::
# 
# :::{index} single: Variable ; Wert
# :name: variable_wert
# :::
# 
# (variablen-definieren)=
# ## Variablen definieren und ausgeben
#  
# Mit der Anweisung in Zeile 6 beginnt der eigentliche Programmcode. Zuerst wird einer **Variable** mit dem Namen `my_variable` ein **Wert** zugewiesen.[^fn1] Die {term}`Zuweisung` des Werts zur Variablen wird durch das Gleichheitszeichen (=) indiziert. Es ist nicht mit dem mathematischen Gleichheitszeichen gleichzusetzen. Sie können sich eine Variable als eine Art Behälter (*container*) vorstellen, der für die Zeit des Programmdurchlaufs bestimmte Werte aufbewahrt und ansteuerbar macht. Anders als bei {term}`statisch typisierten` Programmiersprachen wie [C](https://en.wikipedia.org/wiki/C_(programming_language)) oder [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) werden Variablen in Python {term}`dynamisch typisiert`. Das heißt, Variablen müssen nicht ausdrücklich dahingehend deklariert werden, ob es sich etwa um ein [*string*](https://docs.python.org/3/library/stdtypes.html#textseq) (Zeichenkette) oder *integer* (Ganzzahl) handelt. Durch die doppelten (`"Hello, World"`) oder einfachen (`'Hello, World'`) Anführungszeichen wird in Python automatisch der Datentyp *string* ermittelt. Beide Varianten sind möglich, bleiben Sie innerhalb eines Programmierprojekts aber bitte immer einheitlich![^fn2] Konkret heißt das für unser Beispiel, dass wir in Zeile 6 den Wert `Hello, World!` vom Typ *string* der Variable `my_variable` zugewiesen haben. Solange wir die Variable während eines Programmdurchlaufs nicht mit einem anderen Wert überschreiben, rufen wir immer diese Zeichenkette auf, wenn wir die Variable benutzen.
# 
# Es gibt noch weitere Formen von Zuweisungen, die in unterschiedlichen Kontexten gebräuchlich sein können. Sie können beispielsweise mehrere Zuweisungen auf einen Schlag durchführen, wie im nachfolgenden {term}`Codeblock`.

# In[ ]:


# assign multiple variables at once
fruit, vegetable = "apple", "cucumber"
breakfast = lunch = "egg"

print(fruit)
print(vegetable)
print(breakfast)
print(lunch)


# In Zeile 2 haben wir platzsparend einerseits den Wert `apple` der Variable `fruit` zugewiesen, andererseits `cucumber` der Variable `vegetable`. Beachten Sie die Reihenfolge der einzelnen Elemente. Dagegen wurde in Zeile 3 der Wert `egg` sowohl der Variable `lunch` als auch der Variable `breakfast` zugewiesen. 
# 
# :::{index} single: Funktion ; print()
# :name: print_
# :::
# 
# Geprüft werden kann die richtige {term}`Zuweisung` indem die in den Variablen gespeicherten Werte der Reihe nach ausgeben werden. Die runden Klammern hinter einem Wort, wie bei `print()`, zeigen an, dass es sich um einen {term}`Funktionsaufruf` handelt. Die [`print()`-Funktion](https://docs.python.org/3/library/functions.html#print) ist eine vordefinierte **Ausgabe-Funktion**. Vordefiniert heißt, dass sie bereits Teil der Python-Umgebung ist und der {term}`Interpreter` weiß, wo er die Definition findet, die vorgibt, was getan werden muss, wenn `print()` aufgerufen wird. Die Elemente zwischen den runden Klammern werden {term}`Argument` oder {term}`Parameter` genannt. Welche Argumente einer Funktion übergeben werden können, erfahren Sie in der [Python-Dokumentation](https://docs.python.org/3/).[^fn3] Hier wird als Argument eine Variable übergeben, die als Wert eine Zeichenkette (*string*) enthält. Mittels `print()` wird diese Zeichenkette nun als Ergebnis ausgegeben und auf Ihrem Bildschirm dargestellt. Sie können als Argumente für die `print()`-Funktion aber auch direkt Werte verwenden.
# Die kürzeste Variante unseres Hallo-Welt-Programms sieht in Python dann beispielsweise wie folgt aus:

# In[ ]:


print("Hello, World!")


# In[ ]:


help(print)


# :::{index} Eingabe
# :name: eingabe
# :::
# 
# ## Eingabe
# 
# Lassen Sie uns das Hallo-Welt-Programm nun etwas interaktiver gestalten, indem es uns nach unserem Namen fragt und persönlich begrüßt.

# In[ ]:


# hello user program
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
# Neben verschiedenen Ausgabemöglichkeiten bietet Python auch einige **Eingabeoptionen**. Eine davon ist die [`input()`-Funktion](https://docs.python.org/3/library/functions.html#input) (siehe Zeile 2). Wird diese [Funktion](../ch02-programmablaeufe-strukturieren/04-funktionen.ipynb) im Programmdurchlauf aufgerufen, dann bleibt der Prozess solange angehalten bis die Nutzer:innen eine Eingabe über die Tastatur getätigt und mit der Return-Taste bestätigt haben. Die `input()`-Funktion nimmt den optionalen {term}`Parameter` *prompt* an, wodurch spezifiziert werden kann, welche Informationseingabe erwartet wird - im obigen Beispiel ein Name. Die Eingabe wird dann in der Variablen `name` gespeichert.
# 
# Als Ausgabe zeigt uns die `print()`-Funktion anschließend die "Summe" aus der "Addition" der in den Variablen `my_variable` und `name` gespeicherten Zeichenketten. Die Zusammenfügung von Strings durch das **+**-Zeichen wird auch {term}`Konkatenierung` oder {term}`Verkettung` genannt. Zeichenketten in Python sind prinzipiell unveränderbar ({term}`immutable`). Operationen, die eine Zeichenkette verändern sollen, geben daher stets eine *neue* Zeichenkette zurück. Wollten wir also, statt die zusammengefügte Zeichenkette per `print()` direkt auszugeben, stattdessen mit ihr weiterarbeiten, dann müssten wir sie einer neuen Variablen zuweisen oder die alte überschreiben.

# [^fn1]: Enthält eine Variable mehrere Wörter, ist es in Python Konvention, diese mit Unterstrichen zu trennen. Ihr Programm wird auch funktionieren, wenn Sie sich nicht daran halten; die Lesbarkeit des Code verbessert sich aber dadurch. Leerzeichen dürfen Sie zur Trennung jedoch nicht verwenden.
# 
# [^fn2]: Wenn Sie sich genauer dafür interessieren, was Datentypen und Variablen in Python sind, dann empfehlen wir Ihnen [diese Lektion](https://www.python-kurs.eu/python3_variablen.php) im Python-Kurs von Bernd Klein.
# 
# [^fn3]: Die Dokumentation sollte für die Recherche von Funktionen stets Ihre erste Anlaufstelle sein. Python bietet allerdings auch eine eingebaute Hilfe, mit der Sie die bereits erwähnten *docstrings* aufrufen können. Das bietet oft schon einen ersten Eindruck von den Funktionalitäten.
