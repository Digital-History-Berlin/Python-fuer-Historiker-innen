#!/usr/bin/env python
# coding: utf-8

# # Numerische Datentypen
# 
# Sie haben sich bereits eingehend mit dem Datentyp *string* auseinandergesetzt, aber Python bietet natürlich auch eine Reihe von [numerischen Datentypen](https://docs.python.org/3/library/stdtypes.html#typesnumeric), die wir auch als überwiegend mit textuellen Daten arbeitende Geisteswissenschaftler:innen kennenlernen sollten. Dabei können wir zugleich eine nützliche Funktion erlernen, die wir benötigen, wenn wir Daten sammeln, mit unbekannten Datenbanken arbeiten oder uns einfach so nicht mehr sicher sind, um welchen Datentyp es sich bei einer Variable handelt. Durch den Aufruf der Funktion `type()` können wir die Information einfach in Python erfragen.

# In[ ]:


# identify the datatype
text = "some text"
type(text)


# ## Ganzzahlen
# 
# Bei *integers* handelt es sich um ganze Zahlen.

# In[ ]:


# identify the datatype
x = 2
type(x)


# ## Gleitkommazahlen
# 
# Bei *float* handelt es sich um Gleitkomma- beziehungsweise Dezimalzahlen. 

# In[ ]:


# identify the datatype
y = 5.0
type(y)


# Beachten Sie, dass in Python Dezimalzahlen mit einem Punkt und nicht mit einem Komma geschrieben werden.
# 
# Dezimalzahlen weisen nicht selten zahlreiche Nachkommastellen auf. Es kann dann gewünscht sein, diese durch Rundung zu verringern. Das können Sie mit der Funktion [`round()`](https://docs.python.org/3/library/functions.html#round) erledigen. Sie nimmt als erstes Argument den jeweiligen Wert, der gerundet werden soll, und optional als zweites Argument die Anzahl der gewünschten Nachkommastellen.
# 
# **Zwei Beispiele:**

# In[ ]:


# example 1: round decimal
round(5.7823432, 2)


# In[ ]:


# example 2: round decimal
round(5.7823432)


# **Was ist beim zweiten Beispiel passiert? Prüfen Sie ggf. den Datentyp.** 

# In[ ]:


# your answer


# ## Komplexe Zahlen
# 
# Ein besonderer numerischer Datentyp sind die [komplexen Zahlen](https://en.wikipedia.org/wiki/Complex_number). Da dieser Datentyp in Szenarien, mit denen Historiker:innen programmatisch arbeiten, selten vorkommt, soll er an dieser Stelle nicht weiter erläutert werden -- dennoch sollter dieser zumindest kurz erwähnt werden.

# In[ ]:


# identify the datatype
z = 1 + 2j
type(z)


# (datentyp-aendern)=
# ## Datentyp ändern
# 
# Wir hatten darauf hingewiesen, dass Variablen in Python dynamisch typisiert werden, also dass automatisch ermittelt wird, ob es sich bei einem Wert um eine komplexe Zahl, ein Integer oder einen String handelt. Es kann aber vorkommen, dass wir bewusst den Datentyp ändern wollen. Einen solchen Fall haben wir mit der `input()`-Funktion kennengelernt. Sie erinnern sich: Die Eingabe wird immer als String gespeichert. Vielleicht möchten wir aber gerne mit Zahlen als Nutzer:inneneingaben arbeiten, dann können wir den String explizit umwandeln.
# 
# **Zum Beispiel:**

# In[ ]:


# normal input
age = input("How old are you? ")
print(f"Die Eingabe ist vom Typ {type(age)}.")


# In[ ]:


# convert input
age_int = int(input("How old are you? "))
print(f"Die Eingabe ist vom Typ {type(age_int)}.")


# Mit der konvertierten Eingabe können nun auch bedarfsweise mathematische Berechnung angestellt werden. Konvertierungsfunktionen gibt es unter anderem für die komplexen Zahlen ([`complex()`](https://docs.python.org/3/library/functions.html#complex)), Strings ([`str()`](https://docs.python.org/3/library/functions.html#func-str)), Integers ([`int()`](https://docs.python.org/3/library/functions.html#int)) und Gleitkommazahlen ([`float()`](https://docs.python.org/3/library/functions.html#float)).

# ## Arithmetische Operatoren
# 
# Python kann ganz einfach genutzt werden, um einfache und auch komplexere mathematische Berechnungen zu lösen. Sie können die Programmierumgebung gewissermaßen wie einen Taschenrechner benutzen oder kleine Programme schreiben, die Ihnen wiederkehrende Aufgaben, wie beispielsweise Prozentrechnung, abnehmen. 
# 
# Probieren Sie zunächst die nachfolgenden Berechnungen aus und erklären Sie, wofür die mathematischen Symbole (Operatoren) stehen. Sie werden feststellen, dass wir einige der Operatoren auch bei der Arbeit mit Zeichenketten genutzt haben.

# In[ ]:


2 + 3


# In[ ]:


2 + -3


# In[ ]:


2 - 3


# **Wofür stehen die Operatoren + und - in diesen Beispielen?**

# In[1]:


# your answer


# In[ ]:


2 * 3


# In[ ]:


(2 + 200) * 3


# In[ ]:


2 ** 10


# In[ ]:


24 ** 45


# **Wofür stehen die Operatoren * und \*\* in diesen Beispielen?** 

# In[ ]:


# your answer


# In[ ]:


10 / 2


# In[ ]:


10 / 3


# In[ ]:


10 // 2


# In[ ]:


10 // 3


# **Wodurch unterscheiden sich die Berechnungen mit / und //?**

# In[ ]:


# your answer


# In[ ]:


10 % 3


# In[ ]:


10 % 5


# In[ ]:


10 % 4


# **Erklären Sie die Funktionsweise des sog. Modulo-Operators:** 

# In[ ]:


# your answer


# In[ ]:


"5" + "13"


# In[ ]:


"5" * 13


# In[ ]:


int("5") + int("13")


# In[ ]:


float("5") * 13


# In[ ]:


str(30) * 2


# **Erklären Sie, was in den einzelnen Codezeilen passiert ist:** 

# In[ ]:


# your answer


# ## Aufgabe: Der Computer als Taschenrechner
# 
# Zum Abschluss dieser Lektion sollen Sie ein kleines Skript schreiben, das eine einfache mathematische Rechnung enthält. In welcher Form Sie diese integrieren bleibt Ihnen überlassen. Ihr Programmcode sollte zudem mindestens eine Eingabe-Funktion sowie eine formatierte Ausgabe enthalten. Beziehen Sie außerdem nach eigenem Ermessen aus allen Lektionsinhalten Komponenten in Ihr Skript ein.
# 
# **Ihre Lösung könnte zum Beispiel aussehen wie dieser einfache Prozentrechner:**

# In[ ]:


# percentage calculator
print("Mit diesem Rechner erfahren Sie, wie viel Sie sparen können und wie hoch der Kaufbetrag ist.")

# input
base = float(input("Geben Sie den Grundwert ein (Euro): "))
percentage = int(input("Geben Sie den Rabatt ein (%): "))

# calculate the percentage value and the remaining purchase amount
value = (base/100) * percentage
netto = base - value

# output
print(f"Sie sparen {value} Euro und müssen noch {netto} Euro bezahlen.")


# **Ihr Skript-Beispiel für die Lektion "Atomare Datentypen":**

# In[ ]:


# your code

