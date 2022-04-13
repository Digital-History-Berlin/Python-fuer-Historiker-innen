#!/usr/bin/env python
# coding: utf-8

# # Hallo, Welt!
# Führen Sie den nachfolgenden Codeblock aus.

# In[ ]:


# hello world program

"""These few lines of code are 
used to display the text "Hello, World!"."""

my_variable = "Hello, World!" # assign value to variable
print(my_variable)


# Anhand des obigen, obligatorischen [Hallo-Welt-Programms](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program), das in keiner Programmier-Einführung fehlen darf, können wir schon einige grundlegende Funktionsweisen von Python ablesen und zugleich testen, ob die Programmierumgebung ordnungsgemäß funktioniert. Das Programm macht im Prinzip nichts anderes, als Ihnen die Zeichenkette "Hello, World!" auf dem Bildschirm auszugeben. 
# 

# **Funktionsweise**
# 
# Der Code wird vom Rechner Zeile für Zeile ausgeführt. Jede Zeile kann potentiell eine Anweisung (*statement*) enthalten, die dem Rechner sagt, was zu tun ist. Die Reihenfolge der einzelnen Anweisungen ist zentral. Es gibt einfache und komplexe Anweisungen, die Sie nach und nach in den nachfolgenden Abschnitten und Lektionen kennenlernen werden.
# 
# Neben den Anweisungen können Programmcodes **Kommentare** enthalten, wie in den Zeilen 1, 3 und 4 unseres Beispielcodes zu sehen. Kommentare können und sollten dazu genutzt werden, Code-Schnipsel hinsichtlich ihrer Funktionalität zu erläutern. Mit der Raute (#) kann ein einfacher einzeiliger Kommentar geschrieben werden. Sobald der Interpreter auf die Raute stößt, wird der Text nicht mehr als auszuführender Code interpretiert und von der Maschine ignoriert. Möchte man über mehrere Zeilen kommentieren, dann kann man entweder in jede Zeile eine Raute setzen oder man nutzt dreimal einfache (') beziehungsweise dreimal doppelte (") Anführungszeichen. Die letzte Variante wird üblicherweise für die Dokumentation genutzt. Als *docstrings* werden sie Ihnen in späteren Übungseinheiten wiederbegegnen, wenn **Funktionen** oder **Klassen** definiert und erklärt werden müssen. Die Kommentare dienen zur Kommunikation mit den Codeleser:innen.
# 
# (variablen-definieren)=
# ## Variablen definieren und ausgeben
#  
# Mit der Anweisung in Zeile 6 beginnt der eigentliche Programmcode. Zuerst wird einer **Variable** mit dem Namen "my_variable" ein **Wert** zugewiesen.[^fn1] Die Zuweisung des Werts zur Variablen wird durch das Gleichheitszeichen (=) indiziert. Es ist nicht mit dem mathematischen Gleichheitszeichen gleichzusetzen. Sie können sich eine Variable als eine Art Behälter (*container*) vorstellen, der für die Zeit des Programmdurchlaufs bestimmte Werte aufbewahrt und ansteuerbar macht. Anders als bei statisch typisierten Programmiersprachen wie [C](https://en.wikipedia.org/wiki/C_(programming_language)) oder [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) werden Variablen in Python dynamisch typisiert. Das heißt, Variablen müssen nicht ausdrücklich dahingehend deklariert werden, ob es sich etwa um ein [*string*](https://docs.python.org/3/library/stdtypes.html#textseq) (Zeichenkette) oder *integer* (Ganzzahl) handelt. Durch die doppelten ("Hello, World") oder einfachen ('Hello, World') Anführungszeichen wird in Python automatisch der Datentyp *string* ermittelt. Beide Varianten sind möglich, bleiben Sie innerhalb eines Programmierprojekts aber bitte immer einheitlich![^fn2] Konkret heißt das für unser Beispiel, dass wir in Zeile 6 den Wert "Hello, World!" vom Typ *string* der Variable "my_variable" zugewiesen haben. Solange wir die Variable während eines Programmdurchlaufs nicht mit einem anderen Wert überschreiben, rufen wir immer diese Zeichenkette auf, wenn wir die Variable benutzen.
# 
# Es gibt noch weitere Formen von Zuweisungen, die in unterschiedlichen Kontexten gebräuchlich sein können. Sie können beispielsweise mehrere Zuweisungen auf einen Schlag durchführen, wie im nachfolgenden Codeblock.

# In[ ]:


# assign multiple variables at once
fruit, vegetable = "apple", "cucumber"
breakfast = lunch = "egg"

print(fruit)
print(vegetable)
print(breakfast)
print(lunch)


# In Zeile 2 haben wir platzsparend einerseits den Wert "apple" der Variable "fruit" zugewiesen, andererseits "cucumber" der Variable "vegetable". Beachten Sie die Reihenfolge der einzelnen Elemente. Dagegen wurde in Zeile 3 der Wert "egg" sowohl der Variable "lunch" als auch der Variable "breakfast" zugewiesen. 
# 
# Geprüft werden kann die richtige Zuweisung indem die in den Variablen gespeicherten Werte der Reihe nach ausgeben werden. Die runden Klammern hinter einem Wort, wie bei print(), zeigen an, dass es sich um einen Funktionsaufruf handelt. Die [**Print-Funktion**](https://docs.python.org/3/library/functions.html#print) ist eine vordefinierte **Ausgabe-Funktion**. Vordefiniert heißt, dass sie bereits Teil der Python-Umgebung ist und der Interpreter weiß, wo er die Definition findet, die vorgibt, was getan werden muss, wenn print() aufgerufen wird. Die Elemente zwischen den runden Klammern werden Argument oder Parameter genannt. Welche Argumente einer Funktion übergeben werden können, erfahren Sie in der [Python-Dokumentation](https://docs.python.org/3/).[^fn3] Hier wird als Argument eine Variable übergeben, die als Wert eine Zeichenkette (*string*) enthält. Mittels print() wird diese Zeichenkette nun als Ergebnis ausgegeben und auf Ihrem Bildschirm dargestellt. Sie können als Argumente für die Print-Funktion aber auch direkt Werte verwenden.
# Die kürzeste Variante unseres Hallo-Welt-Programms sieht in Python dann beispielsweise wie folgt aus:
# 
# 

# In[ ]:


print("Hello, World!")


# In[ ]:


help(print)


# ## Eingabe
# 
# Lassen Sie uns das Hallo-Welt-Programm nun etwas interaktiver gestalten, indem es uns nach unserem Namen fragt und persönlich begrüßt.

# In[ ]:


# hello user program
name = input("What's your name? (press ENTER when finished)")
print(my_variable[:7] + name)


# **Was haben wir gemacht?**
# 
# Neben verschiedenen Ausgabemöglichkeiten bietet Python auch einige **Eingabeoptionen**. Eine davon ist die [**Input-Funktion**](https://docs.python.org/3/library/functions.html#input) (siehe Zeile 2). Wird diese [Funktion](../ch02-programmablaeufe-strukturieren/04-funktionen.ipynb) im Programmdurchlauf aufgerufen, dann bleibt der Prozess solange angehalten bis die Nutzer:innen eine Eingabe über die Tastatur getätigt und mit der Return-Taste bestätigt haben. Die Input-Funktion nimmt den optionalen Parameter *prompt* an, wodurch spezifiziert werden kann, welche Informationseingabe erwartet wird - im obigen Beispiel ein Name. Die Eingabe wird dann in der Variablen "name" gespeichert.
# 
#  **Wichtig:** Die Input-Funktion liefert immer einen String zurück!
# 
# Als Ausgabe zeigt uns die Print-Funktion anschließend die "Summe" aus der "Addition" der in den Variablen "my_variable" und "name" gespeicherten Zeichenketten. Die Zusammenfügung von Strings durch das **+**-Zeichen wird auch **Konkatenierung** oder **Verkettung** genannt. Zeichenketten in Python sind prinzipiell unveränderbar (*immutable*). Operationen, die eine Zeichenkette verändern sollen, geben daher stets eine *neue* Zeichenkette zurück. Wollten wir also, statt die zusammengefügte Zeichenkette per Print direkt auszugeben, stattdessen mit ihr weiterarbeiten, dann müssten wir sie einer neuen Variablen zuweisen oder die alte überschreiben.
# 
# ## Indizierung und Slicing
# 
# Allerdings benötigten wir für die Begrüßung nur einen Teil der "Hello, World!"-Zeichenkette. Als Zeichenkette gehören Strings zu den sequentiellen Datentypen, d.h. sie stellen eine geordnete Folge von Elementen dar, den einzelnen Zeichen (*characters*). Durch diese Ordnung und Rangfolge ist es möglich, jedes einzelne Element des Strings über **Indices** direkt anzusteuern, indem die gewünschte Indexposition durch eckige Klammern angegeben wird: das "e" beispielsweise durch den Ausdruck "my_variable[1]". 
# 
# Wundern Sie sich darüber, warum der zweite Buchstabe in der Zeichenkette an der Indexposition "1" steht? Schauen wir uns den String genauer an:
# 
# ![alt text](https://i.imgur.com/gGDkY0P.png)
# 
# Ein String ist von links nach rechts durchnummeriert. **Achtung:** Die Zählung beginnt allerdings bei 0! Zeichenketten können auch umgekehrt gelesen werden, also von rechts nach links. Dann fangen wir bei -1 an. Auf diese Weise ist jedes Zeichen direkt ansteuerbar - auch Satzzeichen oder Leerzeichen, sogenannte *whitespaces*. Für unsere interaktive Abwandlung des Hallo-Welt-Programms haben wir in der Ausgabefunktion nur einen ganz bestimmten Wertbereich ausgewählt und zwar "Hello, ". Diesen Wertebereich können wir durch Nutzung der Indexpositionen ausschneiden (*slicing*).
# 
# Wie bei der Indizierung benutzen wir für das **Slicing** eckige Klammern, statt einem Wert benötigen wir allerdings eine Start- und eine Endposition. Führen Sie die folgenden Slicing-Anweisungen aus und erklären Sie die Funktionsweise.
# 
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


# (aufgabe-skript-schreiben)=
# ## Aufgabe: Skript schreiben
# 
# Damit haben Sie schon einige erste Grundlagen kennengelernt, mit denen Sie ein kleines Skript schreiben können, das Informationen auf Basis einer Eingabe verarbeitet und wieder ausgibt.
# Wenden Sie das Gelernte an und schreiben Sie ein kurzes, kommentiertes Programm, das die bisher kennengelernten Funktionen beinhaltet und beliebig kombiniert. 

# In[ ]:


# insert your code


# [^fn1]: Enthält eine Variable mehrere Wörter ist es in Python Konvention, diese mit Unterstrichen zu trennen. Ihr Programm wird auch funktionieren, wenn Sie sich nicht daran halten; die Lesbarkeit des Code verbessert sich aber dadurch. Leerzeichen dürfen Sie zur Trennung jedoch nicht verwenden.
# 
# [^fn2]: Wenn Sie sich genauer dafür interessieren, was Datentypen und Variablen in Python sind, dann empfehlen wir Ihnen [diese Lektion](https://www.python-kurs.eu/python3_variablen.php) im Python-Kurs von Bernd Klein.
# 
# [^fn3]: Die Dokumentation sollte für die Recherche von Funktionen stets Ihre erste Anlaufstelle sein. Python bietet allerdings auch eine eingebaute Hilfe, mit der Sie die bereits erwähnten *docstrings* aufrufen können. Das bietet oft schon einen ersten Eindruck von den Funktionalitäten.
