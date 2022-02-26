#!/usr/bin/env python
# coding: utf-8

# # Arbeiten mit atomaren Daten

# ## Grundlegendes
# 
# [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) ist eine plattformunabhängige, sogenannte "general purpose" Programmiersprache, d.h. sie ist für sehr viele unterschiedliche Anwendungsfälle einsetzbar. Sie wurde von dem Niederländer [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) entwickelt und erstmals 1991 veröffentlicht. Die Sprache ist nicht etwa benannt nach einer Schlange, sondern nach einer Fernsehserie der britischen Komikergruppe [Monty Python](https://en.wikipedia.org/wiki/Monty_Python), von der van Rossum ein großer Fan ist. Sie können in der Dokumentation und in Beispielcode häufig Anspielungen finden.
# 
# ## Python-Versionen
# 
# Vor etwa einem Jahrzehnt fand ein Wechsel von Python 2.x zu 3.x statt. Es kann sein, dass man auf seiner Suche nach Verständnis dieses neuen Feldes auf Einführungen stößt, die sich auf 2.x oder die Unterschiede zwischen 2.x und 3.x fokussieren. Unsere Empfehlung: Vernachlässigen Sie 2.x! Guido van Rossum, der Entwickler von Python, machte deutlich, dass es von 2.x keine weiteren Versionen mehr geben wird.[1] Wir wollen uns in dieser Übung also allein auf Python 3.x konzentrieren!

# ## Zentrale Ressourcen 
# 
# Die [umfangreiche Dokumentation](https://docs.python.org/3/) bietet neben Anspielungen auf Monty Python hilfreiche Tutorials, ein Glossar und vor allem die Spezifikationen der einzelnen Bibliotheken beziehungsweise *libraries*.[2] Sie werden immer wieder auf sie zurückgreifen. 
#  
# Eine weitere wichtige Ressource, die Sie immer wieder aufsuchen werden, gleich ob Sie gerade anfangen, zu programmieren oder schon länger dabei sind, ist: [Stackoverflow](https://stackoverflow.com/). Sie werden gerade in den ersten Wochen und Monaten auf kaum ein Problem stoßen, auf das nicht zu irgendeinem Zeitpunkt in der Vergangenheit jemand vor Ihnen gestoßen ist. Lernen Sie voneinander! Wir Historiker\*innen sitzen zwar gerne alleine am Schreibtisch, aber wenn es ums Coden geht, dann dürfen, ja *sollten* wir miteinander arbeiten. **Aber wichtig:** Auch beim Schreiben von Programmcode sollte man Zitierregeln beachten und angeben, wenn man einige Zeilen Code von jemand anderem übernommen hat.

# ## Tutorials
# 
# Das *World Wide Web* ist voll mit vielen nützlichen Tutorials. Auch auf YouTube finden Sie viele empfehlenswerte Kanäle mit gut nachvollziehbaren Erklärungen, die Ihnen den Einstieg erleichtern und auch spezielle Programmbibliotheken praxisorientiert erläutern. Der Großteil der verfügbaren Angebote ist aber nicht unbedingt auf geisteswissenschaftliche Bedürfnisse zugeschnitten. Wir haben hier daher einige Empfehlungen für Sie zusammengetragen, die Ihnen im weiteren Verlauf nützlich sein können:
# 
# - Ein freies Lehrbuch ist zum Beispiel ["A Byte of Python"](https://python.swaroopch.com/index.html). Hier werden keine Vorkenntnisse benötigt. Es stellt sicherlich auch eine gute Ergänzung für diesen Kurs dar.
# 
# - Sehr gut geeignet für Einsteiger\*innen mit geisteswissenschaftlichen Forschungsinteressen ist ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) von Al Sweigart.
# 
# - Folgert Karsdorp hat eine [interaktive Einführung](https://www.karsdorp.io/python-course/) speziell für Geisteswissenschaftler\*innen erstellt, die ebenfalls sehr einsteigerfreundlich ist. Hier finden Sie weitere Jupyter-Notebooks, die Sie begleitend zu dieser Übung bearbeiten können, wenn Sie noch mehr coden wollen. Zudem finden Sie einige Themenblöcke, die wir im Rahmen dieser Übung nicht anschneiden können.
# 
# - Paul Vierthaler hat auf seinem YouTube-Kanal Tutorials für seinen [Kurs zur Textanalyse](https://www.youtube.com/playlist?list=PL6kqrM2i6BPIpEF5yHPNkYhjHm-FYWh17) zur Verfügung gestellt.
# 
# - Auch auf [The Programming Historian](https://programminghistorian.org/en/lessons/?topic=python) finden Sie zahlreiche Python-Lektionen für spezifische geisteswissenschaftliche Anwendungsszenarien.
# 
# - [Corey Schafer](https://www.youtube.com/user/schafer5/videos) bietet auf seinem YouTube-Kanal etliche Tutorials rundum Pythongrundlagen, Softwareentwicklung, aber auch Data Science. Dieser Kanal könnte für Sie vor allem im Anschluss an diesen Kurs interessant sein.
# 

# ## Lernziele
# 
# Was Sie am Ende dieser Lektion beantworten können sollen:
# 
# -  Was sind Variabeln?
# -  Was sind Werte?
# -  Wie weist man einen Wert einer Variabeln zu?
# -  Was sind Datentypen?
# -  Was sind Kommentare?
# -  Welche arithmetischen Operatoren gibt es?
# -  Was sind *integers*?
# -  Was sind *floats*?
# -  Was sind *strings*?
# -  Wie können Informationen ein- und ausgegeben werden?
# -  Wie können wir Strings manipulieren?
# -  Wie kann der Computer als Taschenrechner verwendet werden?

# Speziell für diese Übungseinheit empfehlen wir Ihnen die folgenden Ressourcen:
# 
# - Wie funktionieren Jupyter Notebooks? 
#  - [Jupyter-Notebook-Dokumentation](https://jupyter-notebook.readthedocs.io/en/stable/)
#  - [Einführung von Quinn Dombrowski et al. auf The Programming Historian](https://programminghistorian.org/en/lessons/jupyter-notebooks)
#  - [YouTube-Tutorial von Michael Fudge (Kurzüberblick: 7 Minuten)](https://www.youtube.com/watch?v=jZ952vChhuI)
#  - [YouTube-Tutorial von Corey Schafer (ausführlich: 30 Minuten)](https://www.youtube.com/watch?v=HW29067qVWk)
# 
# - Grundlagen Python:
#  - [Hacking the Humanities](https://www.youtube.com/playlist?list=PL6kqrM2i6BPIpEF5yHPNkYhjHm-FYWh17) Episoden 1-5

# ## Let's code
# 
# Hinweis: Führen Sie Beispiel-Codeblöcke bitte stets aus. Sie können jederzeit weitere Text- oder Codeblöcke in dieses Notebook einfügen, um Informationen zu ergänzen oder frei zu coden.

# **Anmerkungen:** 
# 
# [1] Guido van Rossum, Why you should switch to Python 3, YouTube-Video: https://www.youtube.com/watch?v=bp3mCgrdMxU&feature=youtu.be&t=4m38s 
# 
# [2] Eine *library* ist eine modulare Sammlung von Funktionen und Methoden, die Ihnen den Programmier-Alltag erleichtert, da sie Ihnen viele Zeilen Code erspart. Sie werden im Laufe des Semesters feststellen, dass es durchaus sinnvoll ist, sich genau anzuschauen, was Ihnen da konkret für Arbeit abgenommen wird. 
