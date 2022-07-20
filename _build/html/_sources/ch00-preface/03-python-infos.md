(python-infos)=

# Wissenswertes zur Programmiersprache Python

```{figure} ../img/dh-robot.png
:figclass: margin
:width: 300px
```

2021 feierte die Programmiersprache Python ihren inzwischen 30. Geburtstag. Sie wurde 1991 vom Niederländer Guido van Rossum erstmals veröffentlicht, die konzeptionelle Entwicklung fand aber bereits Ende der 1980er Jahre statt. Seitdem hat sie so manche Entwicklungssprünge durchlaufen, zu erkennen etwa an den unterschiedlichen Versionsnummern: Vor etwa einem Jahrzehnt fand ein Wechsel von Python 2 zu 3 statt. Es kann daher sein, dass Sie im Laufe Ihrer Beschäftigung mit Python auf Einführungen oder Artikel stoßen, die sich auf Python 2 oder die Unterschiede zwischen 2.X und 3.X fokussieren. Unsere Empfehlung: Vernachlässigen Sie 2.X! Seit Anfang 2020 ist der Support für Python 2 eingestellt und es wird keine weiteren Versionen und Sicherheitsupdates mehr geben, dementsprechend basiert auch dieses Jupyter Book allein auf Python 3.

Bei Python handelt es sich um eine plattformunabhängige, sogenannte *general purpose* Programmiersprache, das heißt, sie ist für sehr viele unterschiedliche Anwendungsfälle einsetzbar. Das hat sie mit anderen Sprachen wie [JavaScript](https://de.wikipedia.org/wiki/JavaScript) oder [C++](https://de.wikipedia.org/wiki/C%2B%2B), die Ihnen vielleicht geläufig sind, gemein. Anders als aber beispielsweise C++, ist Python eine *interpretierte* Sprache. 

**Was hat es damit auf sich?**

Sie müssen wissen: Wenn Sie Code schreiben, dann muss dieser, um ausgeführt werden zu können, noch in Maschinensprache übersetzt werden. Das sind Anweisungen, die üblicherweise aus Nullen und Einsen, dem sogenannten Binärcode, bestehen. Für den Übersetzungsvorgang gibt es zwei Herangehensweisen: die **Kompilierung** und **Interpretation**. Die Kompilierung erfolgt auf Seiten der Programmierer:innen; der Maschinencode wird vor dem Ausführen quasi gespeichert und kann auf jedem anderen Rechner mit ähnlichem Prozessor ausgeführt werden. Demgegenüber erfolgt die Interpretation auf dem Rechner der Benutzer:innen; der Code wird immer dann in Maschinensprache übersetzt, wenn er ausgeführt werden soll.

```{figure} ../img/python-logo.png
:figclass: margin
:width: 150px
```

Zudem ist Python durch einen hohen Grad an Modularität gekennzeichnet. Der Programmcode kann leicht in kleinere Einheiten aufgeteilt werden, die einem sehr spezifischen Zweck dienen und dann in unterschiedlichen Kontexten eingebunden und somit wiederverwendet werden. Python kommt direkt mit einer sehr umfangreichen [Standardbibliothek](https://docs.python.org/3/library/) solcher Module daher, die größtenteils plattformunabhängig sind und für zahlreiche Anwendungsfälle bereits die passenden Lösungen bieten.

Falls Sie sich im Übrigen über den Namen gewundert haben sollten: Benannt wurde die Programmiersprache nicht etwa nach einer Schlange (obgleich sie sich auch im Logo wiederfindet), sondern nach einer Fernsehserie der britischen Komikergruppe Monty Python, von der Guido van Rossum ein großer Fan ist. In der [offiziellen Dokumentation](https://docs.python.org/3/) und in Beispielcode werden Sie häufig entsprechende Anspielungen finden. Achten Sie mal darauf!
