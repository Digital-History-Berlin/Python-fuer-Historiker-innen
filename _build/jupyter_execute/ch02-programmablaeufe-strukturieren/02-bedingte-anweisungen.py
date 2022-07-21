#!/usr/bin/env python
# coding: utf-8

# # Bedingte Anweisungen
# 
# :::{index} Bedingte Anweisungen
# :name: bedingte_anweisungen
# :::
# 
# :::{index} Booleans
# :name: booleans
# :::
# 
# ## [Boolesche Werte](https://www.w3schools.com/python/python_booleans.asp)
# Nachdem Sie in der letzten Einheit schon einige Datentypen kennengelernt haben (*int*, *float*, *string* usw.), fügen wir nun dieser Liste noch einen Weiteren hinzu: den Datentyp *Boolean*. Er kann lediglich zwei Werte annehmen: `True` oder `False`. Sie können damit also sog. Wahrheitswerte abbilden. Benannt wurde dieser Datentyp übrigens nach [George Boole](https://de.wikipedia.org/wiki/George_Boole), der mit der [Booleschen Algebra](https://de.wikipedia.org/wiki/Boolesche_Algebra) einen für die Computertechnik grundlegenden Zweig der Mathematik begründete.
# 
# In Python können wir boolesche Variablen durch die bekannte Form der Zuweisung deklarieren:

# In[ ]:


is_spam = True
print(is_spam)

is_spam = False
print(is_spam)


# In den meisten Fällen werden wir uns diesen Datentyp aber zu Nutze machen, um zu prüfen, ob {term}`logische Aussagen` richtig oder falsch sind ... und das werden wir sehr häufig prüfen wollen. Oft möchten wir z.B. wissen, ob eine bestimmte Zeichenkette in einem Text auftaucht, dazu können wir das Schlüsselwort `in` nutzen:

# In[ ]:


example_text = '''Die Editionswissenschaft erlebt nicht zuletzt wegen einer 
erfolgreichen Kombination von traditionellen Arbeitsweisen mit Methoden 
der Digital Humanities einen regelrechten Hype.'''

print("Editionswissenschaft" in example_text)
print("Text Mining" in example_text)


# Durch Ergänzung des Schlüsselworts `not` können Sie eine Abfrage auch negieren:

# In[ ]:


print("Editionswissenschaft" not in example_text)
print("Text Mining" not in example_text)


# :::{index} Vergleichsoperatoren
# :name: vergleichsoperatoren
# :::
# 
# ## Vergleichsoperatoren
# 
# Neben den Schlüsselwörtern `in` oder `not in` können Sie in Python auch klassische Vergleichsoperatoren zur Prüfung logischer Aussagen verwenden. Diese sind weitestgehend selbsterklärend und ergänzen die arithmetischen Operatoren, die Sie im letzten Kapitel kennengelernt haben. Gehen Sie die einzelnen Anweisungen durch und vollziehen Sie nach, was mit den Operatoren in den jeweilige Fällen geprüft wird. Tragen Sie - bevor Sie den Codeblock ausführen - in den Kommentarzeilen ein, welchen {term}`Wahrheitswert` die jeweiligen logischen Aussagen ergeben werden, also ob sie `True` oder `False` sind. Durch die Ausführung des Codeblocks können Sie dann prüfen, ob Sie richtig getippt haben:

# In[ ]:


# kleiner als; Notieren Sie sich vor der Ausführung des Codeblocks, 
# welchen Wahrheitswert Sie erwarten.
print(5 < 10)

# Länge 1 ist kleiner als Länge 2; Notieren Sie sich vor der Ausführung des Codeblocks, 
# welchen Wahrheitswert Sie erwarten.
print(len("Text Mining") < len("Editonswissenschaft"))

# größer als; Welchen Wahrheitswert erwarten Sie? 
print(5 > 10)

# kleiner als oder gleich; Notieren Sie sich vor der Ausführung des Codeblocks, 
# welchen Wahrheitswert Sie erwarten.
print(11 <= 10)

# größer als oder gleich; Notieren Sie sich vor der Ausführung des Codeblocks, 
# welchen Wahrheitswert Sie erwarten.
print(10 >= 10)

# identisch; Notieren Sie sich vor der Ausführung des Codeblocks, 
# welchen Wahrheitswert Sie erwarten.
print(5 == 5)

# identisch; Notieren Sie sich vor der Ausführung des Codeblocks, 
# welchen Wahrheitswert Sie erwarten.
print("42" == 42)


# Kontraintuitiv sind auf den ersten Blick vielleicht nur die letzten beiden Abfragen, die prüfen, ob zwei Werte identisch sind. Hier müssen zwei Gleichheitszeichen (`==`) verwendet werden, da, wie Sie im [ersten Kapitel](variablen-definieren) gelernt haben, das einfache Gleichheitszeichen (`=`) bereits für die Zuweisung von Werten zu Variablen reserviert ist.
# 
# Der Operator zur Prüfung der Ungleichheit hingegen besteht aus einem Ausrufezeichen gefolgt von einem einzelnen Gleichheitszeichen:

# In[ ]:


print(5 != 5)


# :::{index} Bedingte Abfragen
# :name: bedingte_abfragen
# :::
# 
# :::{index} single: Bedingte Abfragen ; if
# :name: if_
# :::
# 
# :::{index} single: Bedingte Abfragen ; else
# :name: else_
# :::
# 
# ## [Bedingte Abfragen mit if, elif und else](https://www.python-kurs.eu/python3_bedingte_anweisungen.php)
# 
# Was können wir nun alles mit den Operatoren und den Datentypen, die wir bisher kennengelernt und in dieser Lektion noch kennenlernen werden, anstellen? 
# 
# Bisher haben wir unsere Programme vor allem als eine Abfolge von Instruktionen geschrieben:
# 
# :::{epigraph}
# *Weise einen Wert einer Variablen zu.* 
# 
# *Addiere mehrere Werte und weise die Summe einer Variablen zu.*
# 
# *Gib den Wert der Variablen aus ... usw.*
# :::
# 
# Wirklich interessant wird es, wenn wir unsere Programme so gestalten, dass bestimmte Schritte nur dann ausgeführt werden, wenn etwaige Vorbedingungen erfüllt sind. Solche logischen Verzweigungen können wir mithilfe der eben kennengelernten Operatoren und Wahrheitswerte und den sogenannten `if`-Abfragen definieren:

# In[ ]:


sub_string = input('''Geben Sie ein Wort ein, für das Sie prüfen wollen, 
ob es in unserem Beispieltext vorkommt: ''')

if sub_string in example_text:
    print(f"Die Zeichenkette '{sub_string}' ist Teil von example_text.")

else:
    print(f"Tut mir leid, die Zeichenkette '{sub_string}' ist nicht Teil von example_text.")

print("Das Programm ist beendet.")


# Wie Sie sehen, müssen Sie einfach nur die Abfrage, die Sie stellen wollen, hinter das Schlüsselwort `if` einfügen. Nach einem Doppelpunkt folgt der Teil des Programmcodes, der nur dann ausgeführt wird, wenn die Abfrage den Wert `True` ergibt, andernfalls wird ausgeführt, was wir unter `else` definiert haben. Die Angabe einer `else`-Anweisung ist optional. Wir könnten sie im konkreten Fall auch weglassen, dann würde das Programm, wenn die `if`-Abfrage nicht den Wert `True` ergibt, einfach zum abschließenden `print`-Statement springen:

# In[ ]:


sub_string = input('''Geben Sie ein Wort ein, für das Sie prüfen wollen, 
ob es in unserem Beispieltext vorkommt: ''')

if sub_string in example_text:
    print(f"Die Zeichenkette '{sub_string}' ist Teil von example_text.")

print("Das Programm ist beendet.")


# ::::{margin}
# :::{admonition} Wichtig!
# :class: note
# Nach dem Doppelpunkt einer `if`-Abfrage wird in der nächsten Zeile die Anweisung eingerückt.
# :::
# ::::
# 
# Mit `if`-Abfragen können wir also eine klassische Wenn-Dann-(Andernfalls-)Bedingung formalisieren:
# 
# :::{epigraph}
# *Wenn die Bedingung "sub_string ist in example_text" wahr ist, dann gib die Meldung aus, dass die Zeichenkette im Beispieltext enthalten ist. Optional: Wenn die Bedingung nicht erfüllt ist, dann gib eine Meldung aus, dass die Zeichenkette nicht im Beispieltext enthalten ist.* 
# :::
# 
# Beachten Sie dabei aber bitte die Einrückungen, beispielsweise in Zeile 4. Die Einrückungen dienen nicht nur einer besseren Lesbarkeit, sondern bedeuten für den Python-Interpreter, dass die `if`-Abfrage und der nachfolgende eingerückte Code zusammengehören. Der nicht mehr eingerückte Code in Zeile 6 gehört nicht mehr zur `if`-Abfrage und wird immer ausgeführt; unabhängig davon, ob diese wahr oder falsch ist.
# 
# Wenn Sie die Einrückung entfernen würden, ruft das den [Indentation-Fehler](indentationerror) hervor und Ihr Programm wird nicht ausgeführt: 

# In[ ]:


sub_string = input('''Geben Sie ein Wort ein, für das Sie prüfen wollen, 
ob es in unserem Beispieltext vorkommt: ''')

if sub_string in example_text:
print(f"Die Zeichenkette '{sub_string}' ist Teil von example_text.")
else:
    print(f"Tut mir leid, die Zeichenkette '{sub_string}' ist nicht Teil von example_text.")

print("Das Programm ist beendet.")


# Das gilt es also zu vermeiden. Achten Sie also immer darauf, auf welcher Ebene, die durch Einrückung eröffnet wird, im Code etwas ausgeführt werden soll. Hier noch mal zur Illustration. Schauen Sie sich den Codeblock in Ruhe an:

# In[ ]:


"""Die oberste Ebene ist immer die Ebene ohne Einrückung. 
Wir könnten Sie das EG unseres Codes nennen oder Ebene 0."""

sub_string = input('''Geben Sie ein Wort ein, für das Sie prüfen wollen, 
ob es in unserem Beispieltext vorkommt: ''')

# immer noch Ebene 0
if sub_string in example_text:

    # Ebene 1
    print(f"Die Zeichenkette '{sub_string}' ist Teil von example_text.")
    print("Wir könnten hier jetzt komplexe Berechnungen anstellen oder eine weitere Bedingung prüfen.")

    if len(sub_string) < len(example_text):
        # Ebene 2
        print(f"Zum Beispiel, ob die Zeichenkette '{sub_string}' kürzer ist als example_text - ist sie.")

    else:
        # Ebene 2
        print(f"Zum Beispiel, ob die Zeichenkette '{sub_string}' kürzer ist als example_text - ist sie nicht.")
        
else:
    # Ebene 1
    print(f"Tut mir leid, die Zeichenkette '{sub_string}' ist nicht Teil von example_text.")

# wieder Ebene 0
print("Das Programm ist beendet.")


# Der Code auf einer Ebene wird solange als zusammengehörig erkannt bis wieder auf die nächsthöhere Ebene oder Ebene 0 gesprungen wird. Die Zeilen 10 bis 20 sind ein zusammenhängender Codeblock (mit Untereinheiten), der nur ausgeführt wird, wenn die `if`-Bedingung in Zeile 8 erfüllt ist. Zeile 24 befindet sich zwar auf derselben Ebene, ist aber gebunden an Zeile 22 und stellt daher einen separaten Codeteil dar.
# 
# Der Code in Zeile 27 gehört nicht mehr zur `if`-`else`-Abfrage und wird immer ausgeführt (solange kein Fehler im Code auftritt) -- unabhängig davon, ob die Auswertung der Bedingungen wahr oder falsch ist. 
# 
# :::{index} single: Bedingte Abfragen ; elif
# :name: elif_
# :::
# 
# ## Else-if: elif
# 
# Außerdem haben Sie die Möglichkeit, mehrere `if`-Abfragen in einem Block zusammenzufassen. So können wir zum Beispiel eine dritte Option zu unserer Abfrage hinzufügen, die den Fall behandelt, in dem beide Zeichenketten identisch sind. Verwenden Sie hierfür das Schlüsselwort `elif` (kurz für "else if"). Die Syntax von `elif` ist identisch zu der von `if`.

# In[ ]:


sub_string = example_text

if sub_string in example_text:
    print(f"Die Zeichenkette '{sub_string}' ist Teil von example_text.")
elif sub_string == example_text:
    print(f"Die Zeichenkette '{sub_string}' ist mit example_text identisch.")
else:
    print(f"Tut mir leid, die Zeichenkette '{sub_string}' ist nicht Teil von example_text.")


# Das ist aber offensichtlich nicht das Ergebnis, das wir eigentlich erreichen wollten. Im Fall des obigen Codeblocks ist `sub_string` ja nicht nur ein Teil von `example_text`; die beiden Zeichenketten sind identisch. Trotzdem wird nur Zeile 4, nicht Zeile 6 ausgeführt. Das liegt daran, dass der Python-Interpreter den Code von oben nach unten durchgeht und ausführt. Zeile 3, die erste `if`-Abfrage, gibt bereits `True` als Ergebnis zurück; daher wird der entsprechende Block direkt ausgeführt und nicht mehr geprüft, ob andere Alternativen besser passen. Wir müssen daher `if`-Blöcke mit mehreren `elif`s so konstruieren, dass *spezifische* Aussagen abgefragt werden, bevor *allgemeine* Aussagen geprüft werden ("ist gleich" ist spezifischer als "ist ein Teil von"). Die Lösung ist daher relativ simpel; wir müssen nur Zeile 3 und 5 miteinander vertauschen:

# In[ ]:


sub_string = example_text

if sub_string == example_text:
    print(f"Die Zeichenkette '{sub_string}' ist mit example_text identisch.")
elif sub_string in example_text:
    print(f"Die Zeichenkette '{sub_string}' ist Teil von example_text.")
else:
    print(f"Die Zeichenkette '{sub_string}' ist nicht Teil von example_text.")


# Sie können beliebig viele `elif`-Abfragen hinzufügen, dabei ist aber grundsätzlich die Reihenfolge "`if` ..., `elif` ..., `elif` ..., `elif` ..., [...], `else`" zu berücksichtigen. 

# :::{index} single: Bedingte Abfragen ; Bedingungen verknüpfen
# :name: bedingungen_verknüpfen
# :::
# 
# ## Bedingungen verknüpfen
# 
# Sie können in Ihren `if`-Blöcken auch mehrere Bedingungen gleichzeitig abfragen. Diese müssen Sie mit den Schlüsselwörtern `and` oder `or` miteinander verknüpfen. Diese entsprechen dem logischen UND bzw. ODER. Wie sich die Kombination von *wahren* (w) und *falschen* (f) Aussagen mit UND bzw. ODER auf den {term}`Wahrheitswert` der Gesamtaussage auswirkt, zeigt folgende Tabelle:
# 
# | Aussage_1 | Aussage_2 | and | or |
# |:----------|-----------|-----|---:|
# | w | w | w | w  |
# | w | f | f | w  |
# | f | w | f | w  |
# | f | f | f | f  |
# 
# Hier zwei Beispiele: Überlegen Sie bevor Sie den Code ausführen, ob die Bedingungen erfüllt sind oder nicht. Stimmt die Ausgabe mit Ihrer Vermutung überein?

# In[ ]:


dh_definition = '''Das interdisziplinär ausgerichtete Fach Digital Humanities 
                   (‚digitale Geisteswissenschaften‘) umfasst die systematische Nutzung 
                   computergestützter Verfahren und digitaler Ressourcen in den 
                   Geistes- und Kulturwissenschaften sowie die Reflexion über deren Anwendung.'''
                   
sub_string = "Editionswissenschaft"

if sub_string in example_text and sub_string in dh_definition:
    print("Die Aussage ist wahr.")
else:
    print("Die Aussage ist falsch.")


# In[ ]:


sub_string = "Editionswissenschaft"

if sub_string in example_text or sub_string in dh_definition:
    print("Die Aussage ist wahr.")
else:
    print("Die Aussage ist falsch.")


# Durch Klammern können Sie verknüpfte Abfragen auch schachteln. Dann werden zuerst die {term}`Rückgabewerte` der Abfragen in den Klammern zurückgegeben und erst anschließend mit anderen Abfragen verknüpft. Beachten Sie den Unterschied zwischen folgenden beiden Programmen:

# In[ ]:


bool_1 = False
bool_2 = True
bool_3 = True

if bool_1 and bool_2 or bool_3:
    print("Die Aussage ist wahr.")

print("Das Programm ist beendet.")


# In[ ]:


bool_1 = False
bool_2 = True
bool_3 = True

if bool_1 and (bool_2 or bool_3):
    print("Die Aussage ist wahr.")

print("Das Programm ist beendet.")


# *Was fällt Ihnen auf? Tragen Sie es hier ein:*

# In[ ]:


# your answer


# Wir können also mit Python Programme schreiben, die auf Basis der Auswertung von Aussagen entscheiden, ob eine Anweisung ausgeführt oder übersprungen wird oder Programme, die eine von mehreren Anweisungen zur Ausführung auswählen, je nachdem, welche Bedingungen erfüllt wurden.

# ## Aufgabe: Bedingte Anweisungen
# 
# Schreiben Sie ein kleines Programm, das eine:n Nutzer:in fragt, aus welchem Jahr die [Magna Carta](https://de.wikipedia.org/wiki/Magna_Carta) stammt. Abhängig von der Eingabe sollen verschiedene `print`-Kommandos ausgeführt werden: "Die Magna Carta stammt aus einem späteren Jahr.", "Die Vereinbarungen stammen aus einem früheren Jahr.", "Die Eingabe ist korrekt!". 
# Denken Sie dabei daran, dass Sie den Wert der `input`-Funktion in ein `integer` umwandeln müssen. Wie das geht, können Sie im [ersten Kapitel](datentyp-aendern) noch mal nachlesen.

# In[ ]:


# your code

