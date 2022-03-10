#!/usr/bin/env python
# coding: utf-8

# # [Listen](https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists)
# 
# Im Alltag greifen wir häufig auf Sie zurück: ob zur Planung des Wocheneinkaufs, zur Erstellung von Gästelisten oder zur Organisation anstehender Aufgaben. Listen sind allgegenwärtig. 
# 
# Im Coding-Kontext gehören sie zu den sequenziellen beziehungsweise iterierbaren Datentypen, d.h., dass jedes einzelne Element für sich genommen adressierbar ist. Im ersten Kapitel haben Sie bereits mit Strings gearbeitet, die ganz ähnlich funktionieren. Als Datentyp bilden Listen eine Vielzahl von Werten in einer geordneten Sequenz ab. Das können entweder singuläre Elemente (auch *items* oder *Instanzen* genannt) oder wiederum Listen sein (sie lassen sich beliebig tief verschachteln). Auf diese Weise lassen sich Daten hierarchisch strukturieren. Wenn eine Liste einer Variablen zugewiesen wird spricht man auch von *list value*. Ein solcher *list value* sieht wie folgt aus:
# 
# `[1, 2, 3, 4]`
# 
# ## Listen erstellen
# 
# Analog zu Strings, die Sie an einfachen oder doppelten Anführungszeichen erkennen können, werden Anfang und Ende von Listen durch eckige Klammern angezeigt. Die einzelnen in der Liste enthaltenen Elemente bzw. *items* werden voneinander durch Kommata getrennt. Als Werte können beliebige Datentypen in den Listen gespeichert werden. Hier einige Beispiele:

# In[ ]:


# list containing integers 
[1, 2, 3, 4]

# list containing strings
["egg", "banana", "bread", "cheese"]

# list containing multiple datatypes
["string", 2, True, 2.76]

# assigning list of book titles
book_titles = ["Die Verwandlung", 
               "Die Pest", 
               "Eine Geschichte aus zwei Städten", 
               "Digital Humanities. Eine Einführung", 
               ["Harry Potter und der Stein der Weisen", 
                "Harry Potter und die Kammer des Schreckens", 
                "Harry Potter und der Gefangene von Askaban", 
                "..."]]
print(book_titles)


# Die Variable `book_titles` enthält neben Strings als Werten auch eine Liste und diese Liste wiederum enthält andere Werte vom Datentyp *string*. 
# 
# Ebenso ist es möglich, ähnlich wie bei der Arbeit mit Strings, mit leeren Listen zu arbeiten. Dazu weisen Sie einer Variablen schlicht die beiden Indikatoren `[` und `]` für Listenobjekte zu:

# In[ ]:


# assign empty list
some_list = []
print(some_list)


# ## Listen bearbeiten
# 
# Die Variable `some_list` enthält nun einen *list value*, der individuell mit Inhalt befüllt werden könnte. Das ist nützlich, wenn Sie Daten aus unterschiedlichen Quellen zusammenführen möchten. Dazu und für die Bearbeitung schon angereicherter Listen können folgende Methoden genutzt werden:
# - Konkatenierung mittels "+"-Operator
# - `append()`
# - `extend()`
# - `insert()`
# 
# 

# ## Konkatenierung
# 
# Verschiedene Listen können durch sehr einfache Weise mittels des "+"-Operators zusammengefügt werden. 

# In[ ]:


# assign values to new list
another_list = ["Stolz und Vorurteil", "Woyzeck"]

# concatenate two lists
book_titles = book_titles + another_list
print(book_titles)


# Die Ordnung der zusammengefügten Listenelemente ergibt sich aus der Formulierung der Konkatenierung. In diesem Fall werden die Instanzen aus `another_list` an die Instanzen in `book_titles` angehängt und die Variable `book_titles` wiederum mit dem aus der Konkatenierung resultierenden Listenobjekt überschrieben.

# ## `append()` und `extend()`
# Die Methoden `append()` und `extend()` funktionieren ähnlich. Mit ersterer wird ein hinzuzufügendes Element an das Ende der Liste angehängt. Letztere hängt alle Elemente eines iterierbaren Objekts an das Ende eines bestehenden Listenobjekts an.

# In[ ]:


# append list by user input
book_titles.append(input("Geben Sie einen Buchtitel ein, der einer bestehenden Liste hinzugefügt werden soll: "))
print(book_titles)


# In[ ]:


# extend list by iterable
some_list.extend("abcddfhjdxkd")
some_list.extend([1, 2, 3, 4])
print(some_list)


# Mit `extend()` können Sie also direkt mehrere Elemente hinzufügen. Der Effekt ist dabei ähnlich dem der einfachen "Addition".

# ## `insert()`
# Dagegen fügt die `insert()`-Funktion ein hinzuzufügendes Element durch die Spezifizierung der Indexposition an eine beliebige Position in der Liste: 

# In[ ]:


# insert value at third position
book_titles.insert(2, input("Geben Sie einen Buchtitel ein, der einer bestehenden Liste hinzugefügt werden soll: "))
print(book_titles)


# 
# Wir übergeben der Funktion als Parameter zunächst die Zielposition innerhalb der Liste und dann den hinzuzufügenden Wert (hier durch eine Nutzer:inneneingabe, aber es kann natürlich auch direkt ein Wert oder eine Variable übergeben werden). Zu beachten ist, dass auch bei Listen die Zählung stets bei 0 beginnt. Die Indexposition 2 entspricht folglich dem dritten Wert innerhalb einer Liste. Dieses Schema dürfte Ihnen schon von den Zeichenketten bekannt sein.
# 
# ## Indizieren
# 
# Um nun auf die einzelnen Elemente zuzugreifen, können Sie folgerichtig ganz ähnliche Mechanismen wie bei der Arbeit mit Strings nutzen:
# 
# 

# In[ ]:


print(book_titles[0])

print(book_titles[3])

print("In der Coronakrise war \"" + book_titles[1] + "\" wieder auf der Bestsellerliste.")

print(f"{book_titles[-3]} und {book_titles[3]} kann ich wirklich empfehlen.")


# Auf die einzelnen Werte an den verschiedenen Positionen in der Liste greifen Sie also vermittels eckiger Klammern zu, die an die entsprechende Variable gehängt wird. Das kennen Sie schon von Strings. `book_titles[0]` repräsentiert in diesem Beispiel die Zeichenkette `"Die Verwandlung"`. Das ermöglicht es Ihnen, mit einzelnen Elementen weiterzuarbeiten, beispielsweise um sie gezielt in andere Zeichenketten einzusetzen. Wie bei Strings können Listen dabei sowohl von links nach rechts, als auch von rechts nach links gelesen werden.
# 
# Wie eingangs festgelegt enthält unsere Liste von Buchtiteln selbst wiederum eine Liste. Um auf die Werte in verschachtelten Instanzen zuzugreifen, können mehrere Indizes nacheinander genutzt werden. Der erste bezieht sich dann auf die Instanz in der "Mutterliste" und der zweite auf den Wert innerhalb dieses Listenelements:
# 
# 

# In[ ]:


print(f"{book_titles[-4][2]} ist von J.K. Rowling.")


# Die Angabe einer genauen Listenposition kann auch genutzt werden, um vorhandene Einträge zu überschreiben. So könnten wir etwa den nichtssagenden String `"..."` durch die Angabe des Titels zum vierten Harry-Potter-Band ersetzen:

# In[ ]:


book_titles[-4][3] = "Harry Potter und der Feuerkelch"
print(book_titles)


# Wenn Sie eine Indexposition adressieren die hingegen größer als die Länge der Liste ist, dann erhalten Sie einen `IndexError`, der Ihnen signalisiert, dass Sie über das Ziel hinaus geschossen sind.

# In[ ]:


book_titles[-4][4] = "test"


# Das weist bereits auf eine Schwierigkeit hin. Häufig kann es vorkommen, dass Sie mit unbekannten oder so umfangreichen Datensammlungen arbeiten, dass Sie gar nicht so genau ihre Ausmaße kennen.
# 
# ### Länge bestimmen
# 
# Das Ausmaß beziehungsweise die Länge einer Liste können Sie ganz einfach mit der Ihnen schon bekannten Methode `len()` ermitteln lassen. Probieren Sie es einmal mit der Ihnen bekannten Syntax aus:

# In[ ]:


# ermitteln Sie die Länge der Liste book_titles
len(book_titles)


# ## Listen nach Vorkommen von Elementen prüfen
# 
# Wenn Sie prüfen möchten, ob ein *item* in einer Liste enthalten ist, dann können Sie die Operatoren `in` und `not in` nutzen. Sie erhalten als Rückgabewert Boolesche Wahrheitswerte:

# In[ ]:


"Die Pest" in book_titles


# In[ ]:


"Kulturgeschichte" in book_titles


# Die Prüfung des Vorkommens können Sie mit der Formulierung von bedingten Anweisungen kombinieren. Schreiben Sie ein kurzes `If-Else-`Statement, das prüft, ob ein beliebiger Titel in der Liste `book_titles` vorhanden ist. Ist dies der Fall, soll eine entsprechende Mitteilung ausgegeben werden. Ist dies nicht der Fall, dann soll der Titel hinzugefügt werden.

# In[ ]:


# your code


# Um zu ermitteln, an welcher Stelle ein Wert in einer Liste erstmals vorkommt, kann die `index()`-Funktion verwendet werden. 

# In[ ]:


book_titles.index("Die Pest")


# Da die Indizierung stets bei `0` beginnt, signalisiert Ihnen der Rückgabewert `1`, dass der Titel "Die Pest" sich an der zweiten Position in der Liste befindet. 
# 
# Optional kann der Funktion eine Start- und Endposition wie beim Slicing übergeben werden, um ggf. einen bestimmten Bereich zu definieren, in dem der Wert gefunden werden soll.
# 
# Mit der Methode `count()` kann außerdem ermittelt werden, wie oft ein Element in einer Liste vorhanden ist. Als Rückgabewert erhalten wir ein *integer*. Wir demonstrieren das hier anhand der weiter oben im Notebook definierten Liste `some_list`:

# In[ ]:


# count occurence of item "d" in some_list
some_list.count("d")


# Das Zeichen "d" kommt als *item* also insgesamt viermal in der Liste `some_list` vor.

# ## Ausschneiden (Slicing)
# 
# Nicht nur der Zugriff auf Instanzen in Listen funktioniert auf dieselbe Weise wie bei Zeichenketten. Auch das Slicing, das Sie bei Strings bereits kennengelernt und angewendet haben, kann hier angewendet werden. Während Sie bei Strings dadurch einen Substring gewinnen, erhalten Sie bei Listen eine Subliste. Hierbei geben Sie wieder mindestens den Anfangs- und Startwert an sowie optional den Step.
# 
# Probieren Sie es einmal anhand von `book_titles` aus:

# In[ ]:


# Schneiden Sie eine beliebige Subliste aus

# Schneiden Sie Band 2 bis 4 der Harry-Potter-Reihe aus

# Schneiden Sie jede zweite Instanz aus


# Sie können Slices auch verwenden um größere Teile von Listen mit neuen Daten zu überschreiben.

# In[ ]:


# Ersetzen Sie die Titel zwei bis vier in book_titles durch neue Titel


# ## Elemente entfernen: `remove()`, `pop()`, `clear()` und `del`
# 
# Freilich gibt es auch verschiedene Möglichkeiten um Instanzen aus Listen zu entfernen. 
# 
# Mit der Methode `remove()` wird das *erste* Element in einer Liste entfernt, das mit dem der Methode übergebenen Parameter identisch ist:
# 

# In[ ]:


some_list.remove("d")
print(some_list.count("d"))


# Per *default* entfernt `pop()` das letzte *item* einer Liste. Durch Angabe einer Indexposition können aber auch gezielt Elemente aus der Liste herausgelöst werden. 

# In[ ]:


print(some_list)

# remove last item
some_list.pop()
print(some_list)

# remove third item
some_list.pop(2)
print(some_list)

# remove first item
first_item = some_list.pop(0)
print(first_item)


# Zwar wird mit `pop()` die gewünschte Instanz aus der Liste entfernt, doch bietet die Funktion zusätzlich die Möglichkeit, mit der aus der Liste herausgelösten Instanz weiterzuarbeiten. 
# 
# Mit `clear()` werden alle Elemente einer Liste gelöscht:

# In[ ]:


some_list.clear()
print(some_list)


# Das Resultat ist eine leere Liste, mit der bei Bedarf weiter gearbeitet werden kann.
# 
# Das `del`-Statement verbindet einige dieser Funktionen und geht zum Teil noch darüber hinaus. Erklären Sie im vorgesehenen Kommentarbereich, was die nachfolgenden Anweisungen machen:

# In[ ]:


# assign list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#
del numbers[3]
print(numbers)


# In[ ]:


#
del numbers[2:5]
print(numbers)


# In[ ]:


# 
del numbers[:]
print(numbers)


# In[ ]:


#
del numbers
print(numbers)


# (aufgabe-text-preprocessing)=
# ## Aufgabe: Text Preprocessing
# 
# In unserer ersten Zwischenaufgabe werden wir versuchen, einen Text mit Hilfe der Strukturierungsmöglichkeiten von Listen zu segmentieren, d.h., wir wollen ihn in kleinere Teilbereiche zerlegen. Dabei arbeiten wir diesmal nicht auf Zeichen-, sondern auf Wortebene.
# 
# Dazu müssen wir eine weitere, zentrale Operation kennenlernen, die auf Zeichenketten angewendet werden kann: die `split()`-Funktion. Mit dieser Methode können Sie eine Zeichenkette durch die Angabe eines Separators teilen. Das kann ein Zeichen oder eine Zeichenfolge sein. Per default werden Strings anhand der *whitespaces*, also der Leerzeichen zerteilt. Optional kann angegeben werden, wie oft eine Zeichenkette anhand des Separators maximal zerteilt werden soll. 

# In[ ]:


report = '''Die Editionswissenschaft erlebt nicht zuletzt wegen einer 
            erfolgreichen Kombination von traditionellen Arbeitsweisen 
            mit Methoden der Digital Humanities einen regelrechten Hype. 
            Digitale Methoden drängen sich besonders an den Stellen auf, 
            wo sie eine Überwindung der Beschränkungen des analogen Drucks versprechen. 
            Zugleich zeichnet sich ab, dass mit einem Wechsel zu digitalen Editionsformen 
            nicht nur neue Werkzeuge genutzt werden, sondern dass sich prinzipielle 
            strukturelle Änderungen ergeben: so können analoge Editionen angereichert 
            werden oder Editionen können als Hybrid durch eine gleichwertige digitale und 
            analoge Version repräsentiert werden. Editoren werden angesichts dieser neuen
            Möglichkeiten vor neue Herausforderungen gestellt. Gleiches gilt für Infrastrukturen, 
            die die Produkte der Editionswissenschaft publizieren und langfristig 
            verfügbar machen sollen. Grundlegende Fragen der Qualitätsmessung 
            und -bewertung, der Arbeitsorganisation, Vernetzung und Distribution 
            müssen bei der digitalen Editionswissenschaft anders bzw. neu gestellt 
            und bewertet werden. Die vom Forschungsverbund Marbach Weimar Wolfenbüttel 
            veranstaltete Tagung “Digitale Metamorphose: Digital Humanities und Editionswissenschaft” 
            betrachtete diese neuen Möglichkeiten kritisch und ging dabei auch der Frage nach, 
            welche Grenzen und Gefahren es jenseits der offensichtlichen Vorteile für 
            die Editionswissenschaft gibt.'''


# In[ ]:


# split text into list of words
tokenized_report = report.split()
print(tokenized_report)


# Mit der Split-Funktion können textuelle Daten auf eine sehr simple Weise *tokenisiert* werden. Das sogenannte [*tokenizing*](https://de.wikipedia.org/wiki/Tokenisierung) von Textdaten ist ein grundlegender Arbeitsschritt im Bereich der Textanalyse beziehungsweise allgemeiner gesprochen auf dem Feld [*Natural Language Processing*](https://en.wikipedia.org/wiki/Natural_language_processing). NLP (wie die häufig anzutreffende Abkürzung lautet) ist ein Forschungsfeld, in dem sich intensiv mit der computationellen Verarbeitung von natürlichsprachlichen Daten auseinandergesetzt wird. 
# Eine Zeichenkette wird dabei in kleinere Einheiten, die sogenannten *Tokens* zerlegt, die dann verschiedentlich weiterarbeitet werden können. Oft werden einfache Wörter als Token operationalisiert, aber auch Mehrwort-Einheiten oder gebräuchliche Phrasen können zu Untersuchungselementen werden. Die Tokenisierung ist ein sehr komplexer Vorgang. Für den konkreten Fall genügt aber zunächst die Zerlegung des Textes in Tokens anhand von Leerzeichen.

# **Aufgabenstellung:**
# 
# 1. Suchen Sie sich einen Beispieltext aus, den Sie im Rahmen dieser Übungseinheit basal verarbeiten und analysieren wollen. Weisen Sie diesen einer Variablen zu.
# 
# 2. Definieren Sie zwei Funktionen:
# - `tokenize_text()` soll folgende Operationen beinhalten: 
#   - Entfernung von Interpunktionszeichen
#   - Lowercasing aller Großbuchstaben
#   - Tokenisierung der Textdaten anhand von Whitespaces
# - `segment_text()` soll die tokenisierten Textdaten zu Segmenten in folgender Art weiterverarbeiten:
#   - Segmente sollten nicht länger als 10 Wörter sein
#   - Der Text soll am Ende zeilenweise (`\n`) als zusammenhängende Zeichenkette ausgegeben werden.
# 
# **Hinweise:**
# - Ihre Funktionen sollten auf beliebige Texte anwendbar sein
# - Nutzen Sie bedingte Anweisungen und Schleifen
# - Machen Sie Gebrauch von den Listenfunktionen, Ranges und Konkatenierungs- oder auch von Formatierungsmöglichkeiten bei Zeichenketten

# In[ ]:


# your code

