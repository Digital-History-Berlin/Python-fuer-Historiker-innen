#!/usr/bin/env python
# coding: utf-8

# # [Tupel](https://docs.python.org/3.7/tutorial/datastructures.html#tuples-and-sequences)
# 
# :::{index} Tupel
# :name: tupel
# ::: 
# 
# Tupel sind enge Verwandte von Listen. Aber während Sie Listen im Zuge eines Programmdurchlaufs beliebig manipulieren können, ist dies bei Tupeln nicht der Fall. Bei beiden Datenstrukturen haben Sie lesenden Zugriff, aber nur bei Listen auch einen schreibenden. Abgesehen davon können Sie mit Tupeln die meisten Operationen ausführen, die auch mit Strings und Listen funktionieren. Die Nutzung von Tupeln ist dann vorteilhaft, wenn Sie mit Daten arbeiten, die nicht veränderbar sein sollen. Sie können unveränderbare Daten sowohl in Listen einbauen als auch umgekehrt bearbeitbare Listen in Tupel.
# 
# ## Tupel erstellen
# 
# Zugreifen können Sie auf die einzelnen Elemente wie gewohnt:
# 
# 

# In[ ]:


# assigning tuple of tuples
some_tuple = (("Apfel", "Banane"), ("Milch", "Käse"))
another_tuple = ("Brot", "Baguette", some_tuple)

print(some_tuple[0])
print(some_tuple[1][1])
print(another_tuple[2][1][0])


# Dass es sich um ein Tupel handelt, wird vom Interpreter anhand der runden Klammern `()` erkannt.
# 
# Folgendes gilt es zu beachten:
# Leere Tupel erstellen Sie durch aufeinanderfolgende runde Klammern. 

# In[ ]:


# empty tuple

some_data = ()


# Wenn Sie ein Tupel erstellen wollen, das lediglich einen Wert enthält, dann müssen Sie eine besondere Syntax beachten:

# In[ ]:


one_value_tuple = (1,)


# Damit der Interpreter erkennt, dass es sich um ein Tupel handelt, muss dem Element ein Komma angehängt werden. Warum das so ist, erhellt sich, wenn wir uns anschauen, wie Tupel erstellt werden können. Sie können einerseits Tupel durch die runden Klammern einer Variablen zuweisen, Sie können die Klammern aber auch einfach weglassen und die einzelnen Werte nur durch Kommata getrennt anführen:

# In[ ]:


a = ("Rosa Parks", "Daisy Bates", "Angela Davis", "Wangari Maathai")
print(type(a))

b = "Harriet Tubman", "Althea Gibson", "Marsha P. Johnson", "Mae Jemison"
print(type(b))

c = "Gwendolyn Brooks"
print(type(c))

d = "bell hooks",
print(type(d))


# **Erklären Sie für die Variablen `c` und `d` den Unterschied. Warum ist das angehängte Komma notwendig?** 
# 
# *Ihre Antwort*

# In[ ]:


# your answer


# Auch wenn die runden Klammern für Tupel also optional sind, empfiehlt es sich, mit ihnen zu arbeiten, um Ihren Code explizit und leicht verständlich zu halten.

# ## Aufgabe: Interaktives Programm gestalten
# 
# Schreiben Sie ein kleines interaktives Programm, das eine Liste von Namen erstellt, solange der:die Nutzer:in einen Eintrag hinzufügen möchte. Die Namen sollen als Tupel strukturiert sein und jeweils Vor- und Nachnamen enthalten. Zum Abschluss des Programms soll dem:der Nutzer:in die Liste bestehend aus Tupeln ausgegeben werden.

# In[ ]:


# your code

