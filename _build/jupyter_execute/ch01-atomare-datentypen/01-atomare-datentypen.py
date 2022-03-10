#!/usr/bin/env python
# coding: utf-8

# # Arbeiten mit atomaren Datentypen

# ## Ressourcen 
# 
# Die [umfangreiche Dokumentation](https://docs.python.org/3/) zu Python bietet hilfreiche Tutorials, ein Glossar und vor allem die Spezifikationen der einzelnen Bibliotheken beziehungsweise *libraries*.[^fn1] Sie werden immer wieder auf sie zurückgreifen. 
#  
# Eine weitere wichtige Ressource, die Sie immer wieder aufsuchen werden, gleich ob Sie gerade anfangen, zu programmieren oder schon länger dabei sind, ist: [Stackoverflow](https://stackoverflow.com/). Sie werden gerade in den ersten Wochen und Monaten auf kaum ein Problem stoßen, auf das nicht zu irgendeinem Zeitpunkt in der Vergangenheit jemand vor Ihnen gestoßen ist. Lernen Sie voneinander! Wir Historiker:innen sitzen zwar gerne alleine am Schreibtisch, aber wenn es ums Coden geht, dann dürfen, ja *sollten* wir miteinander arbeiten. **Aber wichtig:** Auch beim Schreiben von Programmcode sollte man Zitierregeln beachten und angeben, wenn man einige Zeilen Code von jemand anderem übernommen hat.

# ## Tutorials
# 
# Das *World Wide Web* ist voll mit vielen nützlichen Tutorials. Auch auf YouTube finden Sie viele empfehlenswerte Kanäle mit gut nachvollziehbaren Erklärungen, die Ihnen den Einstieg erleichtern und auch spezielle Programmbibliotheken praxisorientiert erläutern. Der Großteil der verfügbaren Angebote ist aber nicht unbedingt auf geisteswissenschaftliche Bedürfnisse zugeschnitten. Wir haben hier daher einige Empfehlungen für Sie zusammengetragen, die Ihnen im weiteren Verlauf nützlich sein können:
# 
# - Ein freies Lehrbuch ist zum Beispiel ["A Byte of Python"](https://python.swaroopch.com/index.html). Hier werden keine Vorkenntnisse benötigt. Es stellt sicherlich auch eine gute Ergänzung für diesen Kurs dar.
# 
# - Sehr gut geeignet für Einsteiger:innen mit geisteswissenschaftlichen Forschungsinteressen ist ["Automate the Boring Stuff with Python"](https://automatetheboringstuff.com/) von Al Sweigart.
# 
# - Folgert Karsdorp hat eine [interaktive Einführung](https://www.karsdorp.io/python-course/) speziell für Geisteswissenschaftler:innen erstellt, die ebenfalls sehr einsteigerfreundlich ist. Hier finden Sie weitere Jupyter-Notebooks, die Sie begleitend zu dieser Übung bearbeiten können, wenn Sie noch mehr coden wollen. Zudem finden Sie einige Themenblöcke, die wir im Rahmen dieser Übung nicht anschneiden können.
# 
# - Paul Vierthaler hat auf seinem YouTube-Kanal Tutorials für seinen [Kurs zur Textanalyse](https://www.youtube.com/playlist?list=PL6kqrM2i6BPIpEF5yHPNkYhjHm-FYWh17) zur Verfügung gestellt.
# 
# - Auch auf [The Programming Historian](https://programminghistorian.org/en/lessons/?topic=python) finden Sie zahlreiche Python-Lektionen für spezifische geisteswissenschaftliche Anwendungsszenarien.
# 
# - [Corey Schafer](https://www.youtube.com/user/schafer5/videos) bietet auf seinem YouTube-Kanal etliche Tutorials rundum Pythongrundlagen, Softwareentwicklung, aber auch Data Science. Dieser Kanal könnte für Sie vor allem im Anschluss an diesen Kurs interessant sein.
# 
# - Auf der Seite [PythonHumanities.com](https://pythonhumanities.com/) stellt William Mattingly ebenfalls zahlreiche Videos mit Bezug Python und Digital Humanities frei zur Verfügung.
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
# -  Wie lese ich Fehlermeldungen?

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

# :::{note}
# Führen Sie Beispiel-Codeblöcke bitte stets aus. Wenn Sie das Notebook über Binder nutzen, führen Sie bitte die Beispiel-Codeblöcke stets aus. Sie können jederzeit weitere Text- oder Codeblöcke einfügen, um Informationen zu ergänzen oder frei zu coden.
# :::

# ## Let´s code

# 
# [^fn1]: Eine *library* ist eine modulare Sammlung von Funktionen und Methoden, die Ihnen den Programmier-Alltag erleichtert, da sie Ihnen viele Zeilen Code erspart. Sie werden feststellen, dass es durchaus sinnvoll ist, sich genau anzuschauen, was Ihnen da konkret für Arbeit abgenommen wird. 
