#!/usr/bin/env python
# coding: utf-8

# # [Funktionen](https://www.python-kurs.eu/python3_funktionen.php)
# 
# :::{index} Funktionen
# :name: funktionen
# :::
# 
# ## Definition von Funktionen
# 
# Funktionen dienen dazu, Codeblöcke wiederverwendbar zu machen. Oft ist es erforderlich, bestimmte Aufgaben innerhalb eines Programms auch unabhängig von bestimmten Vorbedingungen (wie bei Schleifen) mehrfach auszuführen[^fn1]. Nehmen wir an, Sie möchten herausfinden, welche von zwei Zahlen größer ist als die andere:

# In[ ]:


number_a = 42
number_b = 23

if number_a > number_b:
    print("number_a ist größer als number_b")
elif number_a == number_b:
    print("number_a und number_b sind gleich groß")
else:
    print("number_b ist größer als number_a")


# Wenn Sie nun an einer anderen Stelle in Ihrem Programm wieder zwei Zahlen miteinander vergleichen möchten, könnten Sie natürlich den obigen Code kopieren und an anderer Stelle wieder einfügen. Das macht Ihr Programm jedoch nicht nur umfangreicher und damit schlechter lesbar, sondern auch anfälliger für Fehler und schwieriger zu warten, wenn Sie zu einem späteren Zeitpunkt Änderungen vornehmen wollen. Sie können obigen Code daher in einer *Funktion* kapseln:

# In[ ]:


def compare_numbers():
    number_a = 42
    number_b = 23

    if number_a > number_b:
        print("number_a ist größer als number_b")
    elif number_a == number_b:
        print("number_a und number_b sind gleich groß")
    else:
        print("number_b ist größer als number_a")

compare_numbers()
compare_numbers()


# ::::{margin}
# :::{admonition} Wichtig!
# :class: note
# Die Anweisungen in einer Funktion werden eingerückt.
# :::
# ::::
# 
# Wie Sie sehen können, werden Funktionen mit dem {term}`Schlüsselwort` `def` definiert. Hinter dem durch Sie vergebenen Namen der Funktion müssen außerdem immer zwei Runde Klammern folgen. Das Einrücken von Codeblöcken kennen Sie bereits von `if` und `while`.
# 
# In den Zeilen 12 und 13 sehen Sie, wie die Funktion jeweils einmal ausgeführt wird. Auch hier müssen auf den Namen der Funktion die runden Klammern folgen.

# ## Parameter
# 
# :::{index} single: Funktionen ; Parameter
# :name: funktionen_parameter
# :::
# 
# So wie wir unsere Funktion konzipiert haben vergleicht sie immer nur die Zahlen 42 und 23 miteinander -- das ist natürlich sehr unflexibel und wenig hilfreich. Wie gehen wir also vor, wenn Sie zwei *beliebige* Zahlen miteinander vergleichen wollen? Schauen Sie sich den nächsten Codeblock an. Fällt Ihnen etwas auf?

# In[ ]:


def compare_numbers(number_a, number_b):
    if number_a > number_b:
        print("number_a ist größer als number_b")
    elif number_a == number_b:
        print("number_a und number_b sind gleich groß")
    else:
        print("number_b ist größer als number_a")


# Hier haben wir die Zuweisungen der Variablen `number_a` und `number_b` entfernt und diese Variablen stattdessen in den Klammern hinter dem Funktionsnamen erstmals genannt. Damit werden diese Variablen zu den *Parametern* der Funktion. Das sind Argumente, die der Funktion bei ihrem Aufruf übergeben werden. Mit diesen Argumenten arbeitet die Funktion dann auf eine bestimmte Art und Weise. Bei den konkreten Variablen-Bezeichnungen handelt es sich zunächst einmal um Platzhalter, die dann beim Aufruf der Funktion durch konkrete Werte ersetzt werden. Wie die Funktion die konkreten Argumente erhält, sehen Sie nachfolgend:

# In[ ]:


compare_numbers(12, 15)
compare_numbers(16, 16)
compare_numbers(15, 12)


# Sowohl die Anzahl, als auch die Reihenfolge der Werte, die der Funktion als Parameter übergeben werden sind relevant. Beides ist bei der Definition der Funktion festgelegt. Folgende Aufrufe führen zu Fehlern:

# In[ ]:


compare_numbers(12)


# In[ ]:


compare_numbers(12, 15, 23)


# Grundsätzlich kennen Sie die Syntax von Funktionen bereits aus einer der letzten Lektion. `print()`, `replace()` oder `type()` ruft jeweils anderswo definierten Programmcode auf und nimmt bei diesem Aufruf eine bestimmte Anzahl von Parametern an (wie bei `print("Hallo")`; hier ist der String `"Hallo"` der übergebene Parameter).

# :::{index} Namensraum
# :name: namensraum
# :::
# 
# ## Namensräume
# 
# Bei der Arbeit mit Funktionen ist ein Konzept sehr wichtig: der sog. *Namensraum*. Namensräume bezeichnen Bereiche innerhalb Ihres Programms, in denen Variablen gültig sind. Das kennen Sie gewissermaßen auch aus alltäglichen Konzepten, wie Ihrem Familien- und Freundeskreis. Wenn Sie mit einer Ihnen nahestehenden Person über eine andere Person sprechen, reicht es oft, wenn Sie einfach einen Vornamen verwenden. Sie können Informationen reduzieren, weil Vieles bereits als bekannt vorausgesetzt werden kann. Flüchtigen Bekanntschaften gegenüber sind diese Informationen aber unter Umständen nicht bekannt und sie können mit einem einfachen Vornamen nichts anfangen. Ein anderes Beispiel sind Telefon- bzw. Handynummern, die innerhalb eines bestimmten Vorwahlbereichs Gültigkeit besitzen oder Matrikelnummern, die in Abhängigkeit von der jeweiligen Universität zu konkreten Personen verweisen, davon unabhängig aber keine Bedeutung haben.
# 
# Wie gestaltet sich das nun in unseren Programmcodes? Sehen Sie sich den nachfolgenden Code an. Welches Ergebnis erwarten Sie? Führen Sie den Code anschließend aus.

# In[ ]:


def my_function():
    my_number = 2

my_number = 5
my_function()
print(my_number)


# Obwohl die Variable `my_number` durch den Aufruf der Funktion augenscheinlich ihren Wert ändern sollte, behält sie ihren ursprünglichen Wert von 5 bei. Das liegt daran, dass Python immer nur die Variablen kennt, die innerhalb eines bestimmten Kontextes (oder Namensraums) definiert wurden. Dies wird noch offensichtlicher, wenn wir obiges Programm etwas anpassen:

# In[ ]:


def my_function():
    print(my_number)
    my_number = 2

my_number = 5
my_function()
print(my_number)


# Ein Fehler ist aufgetreten: Was ist passiert?
# 
# In Zeile 2 ist dem Python-Interpreter die Variable `my_number` noch gar nicht bekannt. Zwar wurde schon vor dem Aufruf der Funktion (also bevor der Fehler auftritt) eine Variable `my_number` definiert, das jedoch in einem anderen Namensraum, nicht innerhalb der Funktion. Wenn Sie die in Zeile 5 deklarierte `my_number` innerhalb der Funktion verwenden möchten, müssen Sie ihr die Variable wie oben beschrieben als Parameter übergeben.
# 
# Auch Funktionen, die von Funktionen aufgerufen werden haben dabei natürlich einen eigenen Namensraum:

# In[ ]:


def another_function():
    my_number = 10
    print(my_number)

def my_function():
    my_number = 2
    print(my_number)
    another_function()

my_number = 5
my_function()
print(my_number)


# Konnten Sie nachvollziehen, was hier passiert?

# In[ ]:


# your answer


# ## Ergebnisse weiterverarbeiten
# 
# Kehren wir nochmal zu unserem Ausgangsbeispiel zurück, bei dem zwei Zahlen miteinander verglichen werden:

# In[ ]:


def compare_numbers(number_a, number_b):
    if number_a > number_b:
        print("number_a ist größer als number_b")
    elif number_a == number_b:
        print("number_a und number_b sind gleich groß")
    else:
        print("number_b ist größer als number_a")


# Das Programm informiert uns zwar menschenlesbar über die Ausgabefunktionen, welches Ergebnis der Vergleich hat, automatisiert weiterverarbeiten lässt sich dieses jedoch noch nicht. Passen wir die Funktion so an, dass sie immer die größere der beiden Zahlen weiterverarbeitbar zurückgibt:

# In[ ]:


def compare_numbers(number_a, number_b):
    if number_a > number_b:
        return number_a
    elif number_a == number_b:
        return number_a
    else:
        return number_b


# Sobald der Python-Interpreter auf ein `return` trifft, wird die Funktion beendet und der Wert, den Sie nach `return` angeben, als Ergebnis zur Weiterverarbeitung übergeben. Wir können das Ergebnis entweder direkt in einer Variable speichern oder einer weiteren Funktion als Parameter übergeben:

# In[ ]:


max_number = compare_numbers(12, 5)
print(max_number)

print(compare_numbers(6, 15))


# **Erklären Sie kurz, was in der folgenden Codezeile passiert:**

# In[ ]:


print(compare_numbers(12, compare_numbers(50, 80)))


# *Ihre Erklärung*

# In[ ]:


# your answer


# Natürlich können wir auch Werte vom Typ Boolean zurückgeben, wenn wir eine Funktion schreiben wollen, die eine Aussage überprüfen soll:

# In[ ]:


def is_greater(number_a, number_b):
    if number_a > number_b:
        return True
    else:
        return False

print(is_greater(42, 21))
print(is_greater(23, 50))


# Damit kennen Sie nun einige Grundlagen zur Konzeption von Funktionen. Es gibt noch einige weitere Gestaltungsmöglichkeiten, z.B. die Angabe von Default-Werten, mit denen die Funktion arbeiten soll, wenn keine konkreten Parameter übergeben werden. Wenn Sie das Thema gerne vertiefen möchten, ist die  Website [Python3 - Tutorial: Funktionen](https://www.python-kurs.eu/python3_funktionen.php) zu empfehlen.

# [^fn1]: Für das Konzept der *Funktion* gibt es in unterschiedlichen Programmiersprachen unterschiedliche Bezeichnungen. Oft ist auch von *Methoden* oder *(Sub-)Routinen* die Rede. Allgemein bedeuten diese Begriffe aber das Gleiche.
