#!/usr/bin/env python
# coding: utf-8

# # Fehlermeldungen
# 
# Es gibt viele Typen von Fehlern in Python und vielleicht sind Sie schon in den Notebooks auf einen gestoßen. Wie liest man solche Fehler und löst Sie auf? 
# Schauen wir uns das anhand dreier der häufigeren Fehlermeldungen an: `NameError`, `SyntaxError` und `IndentationError`.
# 
# ## NameError
# 
# Auf den `NameError` stößt man insbesondere dann, wenn man das Programmieren mit JupyterNotebooks lernt. Führen wir den folgenden Code aus und sehen uns die Fehlermeldung genauer an:

# In[ ]:


# error no. 1
print(not_defined_variable)


# Die nun im Ausgabebereich angezeigte Fehlermeldung zeigt Ihnen zunächst, welche Art von Fehler vorliegt. Über den langen Pfeil (---->) werden Sie darauf hingewiesen, wo im Code der Interpreter auf den Fehler gestoßen ist. Darunter finden Sie eine knappe Erläuterung des Fehlertyps.
# 
# Was Ihnen die Fehlermeldung nun sagt ist, dass Sie mit einer Variablen arbeiten, die bislang im Programmdurchlauf nicht definiert worden ist, d.h., es wurde ihr noch kein Wert zugewiesen, der Container ist also "leer". 
# 
# Auftreten kann der Fehler zum Beispiel dann, wenn Sie anfangen Ihr Notebook zu bearbeiten und es schließen, um es später weiter zu bearbeiten. Sie können unter Umständen beim nächsten Aufruf des Notebooks nicht unmittelbar dort weiter arbeiten, wo Sie aufgehört haben, wenn das, was Sie tun wollen in mehreren, aufeinander aufbauenden Codeblöcken über das Notebook verstreut ist. Der Computer ist gewissermaßen vergesslich: Beim Schließen des Notebooks wird der Speicher - oder das Gedächtnis -, in dem alle Wert-Variablen-Zuweisungen abgelegt sind, gelöscht. Beim nächsten Öffnen des Notebooks muss also der zusammenhängende Code erst wieder der Reihe nach ausgeführt werden.
# 
# ## SyntaxError
# 
# Ein anderer häufiger Fehlertyp ist der `SyntaxError`, der immer dann vorkommt, wenn wir keinen validen Python-Code schreiben, wie beispielsweise in diesem Codeblock:

# In[ ]:


# error no. 2
for element in "Textsequenz"
    print(element)


# Diese Fehlermeldung zeigt uns nicht nur an, in welcher Zeile der Interpreter auf fehlerhaften Code gestoßen ist, sondern auch an welcher Stelle etwas nicht so gelaufen ist, wie es der Interpreter erwarten würde. Was fehlt hier?
# 
# Was wir hier sehen ist eine `for`-Schleife, die in Python nach einem ganz bestimmten Muster aufgebaut ist und dazu dient, in kontrollierter Weise eine Anweisung oder eine Gruppe von Anweisungen auszuführen. Sie entspricht dem folgenden Prinzip:
# 
# `für jedes Element in einer Sequenz:
#         mach etwas (mit diesem Element)`
# 
# Mit der `for`-Schleife können Sie also jedes Element eines sequenziellen Objekts, wie beispielsweise eine Zeichenkette, über die Zuweisung zu einer Variablen bearbeiten oder als Bedingung für eine Anweisung nutzen. Im nächsten Kapitel beschäftigen Sie sich ausführlicher damit. Was hier wichtig ist: Die Schleife muss korrekt aufgebaut sein, um ausgeführt werden zu können. Was in unserem obigen Codeblock fehlt, ist der Doppelpunkt, der zur Einleitung einer `for`-Schleife zwingend dazu gehört. Fügen wir ihn hinzu, dann wird alles korrekt ausgeführt:
# 
# 

# In[ ]:


# error no. 2 solved
for element in "Textsequenz":
    print(element)


# ## IndentationError
# 
# Nach dem Doppelpunkt ist der Code in der Zeile darunter eingerückt. Das hatten wir bislang noch nicht, sollte aber unbedingt beachtet werden. 
# Viele bekannte Programmiersprachen wie C, C++ oder Java nutzen geschweifte Klammern ("{}"), um zusammenhängende Codeblöcke zu definieren. Python nutzt demgegenüber die Einrückung (*indentation*). Demnach beginnt ein Codeblock (also eine `for`-Schleife bspw.) mit einer Einrückung und endet mit der ersten nicht (oder weniger) eingerückten Zeile. Die Anzahl der Einrückungen je Codeblock-Ebene steht theoretisch den Nutzer:innen frei, um allerdings den gefürchteten `IndentationError` zu vermeiden, sollten wir stets die von Jupyter vorgegebene Variante nutzen, die Tabs entspricht (alternativ: 4 Whitespaces pro Einrückung).
# 
# Wenn Sie sich nicht an das Gebot der Einrückung halten, dann erhalten Sie die folgende Fehlermeldung:

# In[ ]:


# error no. 3
for element in "Textsequenz":
print(element)

