#!/usr/bin/env python
# coding: utf-8

# ## Schleifen
# 
# Nachdem wir gelernt haben, wie man ein Programm schreibt, das Anweisungen erst dann ausführt, wenn gewisse Bedingungen erfüllt sind (oder eben auch nicht), wollen wir uns nun anschauen, was wir tun müssen, wenn wir bestimmte Arbeitsschritte wiederholt ausführen möchten. Dazu können wir uns die Schleifen-Funktionen von Python zu Nutze machen. Hiervon gibt es im Wesentlichen zwei Typen, die wir sehr häufig verwenden werden: die `while`- und die `for`-Schleifen.
# 
# ### [while-Schleifen](https://www.python-kurs.eu/python3_schleifen.php)
# Schauen wir uns zunächst die `while`-Schleife an.
# 
# Mit einem `while`-Statement können wir einen Codeblock so lange ausführen wie die Bedingung der `while`-Anweisung den Wahrheitswert `True` ergibt. Strukturell sieht die `while`-Schleife den `if`-Statements sehr ähnlich: Wir benötigen ein Schlüsselwort und zwar das `while` und eine Bedingung, die einen Wahrheitswert ergibt, gefolgt von einem Doppelpunkt. In der nächsten Zeile schließt sich dann, mit einer Einrückung beginnend, ein Codeblock an, der in Abhängigkeit vom Wahrheitswert der `while`-Bedingung ausgeführt wird. `If` und `While` sehen demnach hinsichtlich ihres Aufbaus ähnlich aus, in Bezug auf ihr Verhalten unterscheiden sie sich allerdings deutlich.
# 
# Sehen wir uns dazu diese Schleife an:

# In[1]:


my_number = 1

while my_number < 10:
    print(my_number)
    print("my_number hat nicht den Wert 10")
    
    my_number += 1

print("my_number = {}".format(my_number))


# Die `while`-Schleife ist genau wie eine `if`-Abfrage aufgebaut. Die Zeile hinter dem Schlüsselbegriff `while` muss also entweder den Wert `True` oder `False` annehmen können. Das Programm kehrt jedoch nach jedem Durchlauf des eingerückten Codeblocks zum Kopf der Schleife (hier in Zeile 3) zurück und prüft ob die Abfrage immer noch `True` zurückgibt. Erst wenn dies nicht mehr der Fall ist, wird die Schleife beendet und das Programm springt zu Zeile 9.

# Aber Vorsicht! `While`-Schleifen können ganz schön tricky sein, wenn wir nicht dafür sorgen, dass der Wahrheitswert der `while`-Bedingung irgendwann auf `False` springt. Vier zentrale Eigenschaften zeichnen einen Algorithmus aus: *Allgemeingültigkeit*, *Finitheit*, *Eindeutigkeit* und *Variabilität*. Insbesondere das Kriterium der *Finitheit* müssen Sie bei Schleifen im Hinterkopf behalten. Wenn Sie eine Schleife ohne Abbruchbedingung definieren, wird Ihr Programm immer weiterlaufen; wie etwa im nachfolgenden Beispiel:
# 
# Führen Sie den Code nur aus, wenn Sie wissen, wie Sie eine Endlosschleife abbrechen können:
# 
# **Manueller Abbruch einer Endlosschleife:**
# 
# Jupyter Notebook über bpsw. Colab: Sie können das Programm durch einen Klick auf den Ausführbutton links oben im Codeblock oder in der Menüleiste durch Runtime->Interrupt execution abbrechen.
# 
# Jupyter Notebook über Anaconda Distribution: Stop-Symbol in der Werkzeugleiste.[1])

# In[2]:


# infinity loop
is_spam = True

while is_spam:
    print("Spam!")


# **Anmerkung:**
# 
# [1] Bei der Nutzung des Jupyter Notebooks über ein Terminal kann es zu Problemen beim Abbruch von Endlosschleifen kommen. Im Notfall können Sie im Terminal in diesen Fällen Strg+C zweimal eingeben. Aber Vorsicht: Nicht gespeicherte Änderungen gehen verloren und Sie müssen das Notebook neu starten.

# **Wenden wir das Gelernte wieder an.**
# 
# **Aufgabe 1:** Schreiben Sie ein kurzes Programm, das prüft, ob ein durch ein\*e Nutzer\*in eingegebenes Wort in dem vorgegebenen ersten Absatz eines [Tagungsberichts](https://www.hsozkult.de/conferencereport/id/tagungsberichte-6455?title=digitale-metamorphose-digital-humanities-und-editionswissenschaft&recno=2313&page=116&q=&sort=&fq=&total=8538) vorkommt. Wenn das Wort vorkommt, dann soll eine entsprechende Bestätigung ausgegeben werden. Kommt das Wort nicht im Text vor, soll der\*die Nutzer\*in die Möglichkeit erhalten, erneut eine Eingabe zu tätigen. Möchte der\*die Nutzer\*in keine weitere Eingabe tätigen, dann soll das Programm eine Abschlussmeldung ausgeben und beendet werden. 

# In[ ]:


report = "Die Editionswissenschaft erlebt nicht zuletzt wegen einer erfolgreichen Kombination von traditionellen Arbeitsweisen mit Methoden der Digital Humanities einen regelrechten Hype. Digitale Methoden drängen sich besonders an den Stellen auf, wo sie eine Überwindung der Beschränkungen des analogen Drucks versprechen. Zugleich zeichnet sich ab, dass mit einem Wechsel zu digitalen Editionsformen nicht nur neue Werkzeuge genutzt werden, sondern dass sich prinzipielle strukturelle Änderungen ergeben: so können analoge Editionen angereichert werden oder Editionen können als Hybrid durch eine gleichwertige digitale und analoge Version repräsentiert werden. Editoren werden angesichts dieser neuen Möglichkeiten vor neue Herausforderungen gestellt. Gleiches gilt für Infrastrukturen, die die Produkte der Editionswissenschaft publizieren und langfristig verfügbar machen sollen. Grundlegende Fragen der Qualitätsmessung und -bewertung, der Arbeitsorganisation, Vernetzung und Distribution müssen bei der digitalen Editionswissenschaft anders bzw. neu gestellt und bewertet werden. Die vom Forschungsverbund Marbach Weimar Wolfenbüttel veranstaltete Tagung “Digitale Metamorphose: Digital Humanities und Editionswissenschaft” betrachtete diese neuen Möglichkeiten kritisch und ging dabei auch der Frage nach, welche Grenzen und Gefahren es jenseits der offensichtlichen Vorteile für die Editionswissenschaft gibt."

# your code


# **Aufgabe 2 "Same but different":** Schreiben Sie ein kurzes Programm, das eine Benutzer\*in angeben lässt, in welchem Jahr die Französische Revolution begann. Das Programm soll dabei erst beendet werden, wenn das richtige Jahr angegeben wurde. Wurde ein falsches Jahr angegeben, soll der Nutzer\*in mitgeteilt werden, ob die Angabe zu groß, oder zu klein war. Testen Sie Ihr Programm mit unterschiedlichen Eingaben um herauszufinden, ob es funktioniert.

# In[ ]:


user_input = int(input("In welchem Jahr begann die Französische Revolution? "))

# your code


# ### [for-Schleifen](https://www.python-kurs.eu/python3_for-schleife.php)
# `while`-Schleifen setzen Sie also ein, wenn Sie einen Codeblock so lange wiederholt ausführen wollen, wie eine Bedingung erfüllt ist. Was aber, wenn Sie bereits wissen, dass ein Codeblock nur eine bestimmte Anzahl von Malen wiederholt werden soll? In diesem Fall können Sie auf die `for`-Schleife zurückgreifen (im Deutschen gelegentlich auch als *Zählschleife* bezeichnet):

# In[ ]:


for number in range(1, 11):
    print("number hat den Wert {}".format(number))

print("number = {}".format(number))


# Die Syntax ist hier etwas anders als bei `if` und `while`. Mit `number` wird eine Zählvariable definiert (die auch einen anderen Namen als `number` haben kann). Nach jedem Durchlauf der Schleife (also immer, wenn der eingerückte Codeblock einmal ausgeführt worden ist), wird diese Zählvariable automatisch um 1 erhöht. Hinter `in` wird ein Wertebereich angegeben. In diesem Fall handelt es sich um einen Wertebereich, der durch die Funktion `range()` definiert wird, Sie könnten dort aber auch beispielsweise eine Variable ansprechen, in der ein sequenzielles Objekt wie eine Zeichenkette oder Liste abgespeichert ist. Solange jedenfalls die Zählvariable einen Wert innerhalb dieses Wertebereichs hat, wird die Schleife wiederholt. Natürlichsprachlich könnten Sie Zeile 1 lesen als "Wiederhole folgenden Codeblock solange `number` kleiner als 11 ist. Erhöhe bei jedem Durchlauf `number` um 1."

# Mit der Funktion `range()` können Sie auch angeben, in welchen Schritten die `for`-Schleife den Wertebereich durchlaufen soll. Wollen Sie `number` etwa nicht um 1 sondern um 2 erhöhen, können Sie das wie folgt angeben:

# In[ ]:


for number in range(1, 11, 2):
    print("number hat den Wert {}".format(number))

print("number = {}".format(number))


# Bei der Definition einer `for`-Schleife müssen Sie noch nicht die genaue Anzahl der Durchläufe der Schleife kennen. Sie müssen nur wissen, *dass* es eine bestimmte Anzahl von Durchläufen geben soll und Sie müssen wissen *woher* diese Anzahl kommt. Schauen Sie sich hierzu folgendes Beispiel an:

# In[ ]:


max_number = int(input("Geben Sie eine natürliche Zahl ein: "))

for number in range(1, max_number+1):
    print("number hat den Wert {}".format(number))

print("number = {}".format(number))


# Beachten Sie, dass Sie eine `for`-Schleife auch problemlos mit einer `while`-Schleife implementieren können. Das erste Codebeispiel zur `for`-Schleife ist identisch mit dem ersten Codebeispiel der `while`-Schleife etwas weiter oben. Wo möglich, sollten Sie jedoch `for`-Schleifen einsetzen. Dadurch wird Ihr Code nicht nur kürzer, sondern auch leichter verständlich. Wie Sie später sehen werden, lassen sich `for`-Schleifen in vielen Fällen außerdem wesentlich flexibler einsetzen.

# Gelegentlich kann es sein, dass Sie eine Schleife abbrechen möchten, obwohl ihre eigene Abbruchbedingung noch nicht erfüllt ist, etwa wenn Sie in unserem Beispiel verhindern wollen, dass es zur Überlastung des Systems durch eine zu hohe Usereingabe kommt. Nehmen wir dazu noch mal unser letztes Programm, fügen aber die Bedingung hinzu, dass die Schleife abbrechen soll, sobald `number` den Wert 21 annimmt. Hierfür benötigen Sie das Schlüsselwort `break`:

# In[ ]:


max_number = int(input("Geben Sie eine natürliche Zahl größer 21 ein: "))

for number in range(1, max_number+1):
    print(number)
    print("number hat nicht den Wert {}".format(max_number))
    if number == 21:
        break

print("number = {}".format(number))


# Generell erschweren Sprünge im Programm, wie man sie durch `break` umsetzen kann, jedoch die Lesbarkeit Ihres Codes. Versuchen Sie dessen Einsatz zu vermeiden, indem Sie die Abbruchbedingungen Ihrer Schleifen möglichst allgemein formulieren. Manchmal ist eine Lösung, wie die obige, jedoch einfacher und zielführender.

# **Knobelaufgabe für Zahlenbegeisterte:** Wenden Sie das Gelernte an, indem Sie ein Programm schreiben, das mit `print()` alle [Primzahlen](https://de.wikipedia.org/wiki/Primzahl) zwischen 3 und 200 ausgibt. Zur Erinnerung: Primzahlen sind natürliche Zahlen, die nur durch 1 und durch sich selbst, nicht aber durch andere Zahlen kleiner als sie selbst teilbar sind. Falls Ihnen der Anfang schwer fällt, schauen Sie sich nochmal die Rechenoperatoren aus dem letzten Notebook an. Gegebenenfalls hilft es auch, wenn Sie sich ein Blatt Papier nehmen und in natürlicher Sprache eine auf Stichworten basierende Schritt-für-Schritt-Anleitung schreiben. Diese können Sie dann in Programmcode übersetzen. (Musterlösung folgt nach Abgabefrist)

# In[ ]:


# your code

