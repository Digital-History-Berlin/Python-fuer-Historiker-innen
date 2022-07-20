(citation)=
# Code zitieren

Die Nachnutzung von Code ist auch in den digitalen Geschichts- und Geisteswissenschaften zu begrüßen. Um nicht zu plagiieren sollten aber auch hierbei grundlegende Zitierregeln beachtet werden, um die Standards der guten wissenschaftlichen Praxis einzuhalten. Dabei ist es gerade am Anfang nicht immer ganz einfach zu entscheiden, was *Common Knowledge* ist und was nicht und daher zitiert werden muss. Wenn eine bestimmte Aufgabe eigentlich nur auf eine Art und Weise gelöst werden kann und der entsprechende Code daher weit verbreitet ist, dann erübrigt sich wahrscheinlich die Zitationspflicht (das ist beispielsweise bei den Hello-World-Programmen in den unterschiedlichen Programmiersprachen der Fall). Wann immer aber direkt Code übernommen wird - quasi im Sinne eines Zitates - oder darauf aufgebaut wird, sollte eine Angabe gemacht werden.

Wir haben hier drei Szenarien identifiziert und unsere Empfehlungen zur Referenzierung aufgeführt:

1. Bibliotheken: Um die Nutzung und damit auch die Angabe von Programmierbibliotheken wie beispielsweise [Pandas](https://pandas.pydata.org/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) oder [SpaCy](https://spacy.io/) werden Sie nicht herum kommen und das wäre auch gar nicht wünschenswert, schließlich fließt viel Mühe und Arbeit in die Bereitstellung dieser Ressourcen, die den Programmieralltag bedeutend bereichern. In der Regel sollte die Nachweispflicht einerseits durch den Import in Ihren Skripten, andererseits durch die Bereitstellung der sog. *Requirements*, also der Angabe der verwendeten Bibliotheken inklusive Versionsnummer, erfüllt sein. 

    Beachten Sie aber immer, ob die jeweiligen Produzent:innen der Bibliotheken, Module oder anderweitigen Softwarepaketen zusätzliche Angaben wünschen. Insbesondere sollten Sie nach Lizenzen Ausschau halten, denn die geben vor, unter welchen Bedingungen der Code für die eigenen Projekte nachgenutzt werden kann. Oftmals wünschen die Autor:innen der Softwarepakete, dass ein bestimmtes Paper zitiert wird, wenn Sie deren Code für Ihre Forschungen genutzt haben und eine wissenschaftliche Publikation daraus entstanden ist. Hier finden Sie diese Vorgaben etwa zu [Pandas](https://pandas.pydata.org/about/citing.html) oder zu [Scikit-Learn](https://scikit-learn.org/stable/about.html#citing-scikit-learn). Die Softwarepakete könnten dann so zitiert werden:
    - Jeff Reback et. al., pandas-dev/pandas: Pandas 1.4.3 (v1.4.3), 2022. Zenodo. [https://doi.org/10.5281/zenodo.6702671](https://doi.org/10.5281/zenodo.6702671)
    - Fabian Pedregosa et. al., Scikit-learn: Machine Learning in Python, Journal of Machine Learning Research 12 (2011), S. 2825-2830.

2. Tutorials: Wenn Sie sich mit einer neuen Methode auseinandersetzen, dann ist es nicht unwahrscheinlich, dass Sie sich eine Reihe von Tutorials anschauen und Ihren Code am Ende vielleicht sogar auf einem der Tutorials aufbauen. Hier ist es dann wichtig zu unterscheiden, ob die Autor:innen im Prinzip die Dokumentation einer bestimmten Bibliothek etwas ausführlicher wiedergeben oder weit darüber hinausgehen und im Rahmen eines Workflows eigenständige Arbeitsschritte ausimplementieren. Sie gehen auf Nummer sicher, wenn Sie die verwendeten Tutorials angeben, auf denen Ihr Code beruht. Ein paar Beispiele:
    - Programming Historian: Charlie Harper: Visualizing Data with Bokeh and Pandas, in: Programming Historian (2018), letzte Aktualisierung: 1.10.2021. DOI: https://doi.org/10.46430/phen0081.
    - Towards Data Science: Michel Kana: Topic Modeling Tutorial with Latent Dirichlet Allocation (LDA). A practical guide with proven hands-on Python code. Find what people are tweeting about, in: Towards Data Science (2020). URL: https://towardsdatascience.com/topic-modeling-with-latent-dirichlet-allocation-by-example-3b22cd10c835 [letzter Aufruf: 19.07.2022].

3. Foren wie Stackoverflow: Die Zitation aus Foren ist für Geistes- und Geschichtswissenschaftler:innen sicherlich mit einigen Bauchschmerzen verbunden, handelt es sich doch in der Regel um Informationsangebote, die keinen wissenschaftlichen Standards entsprechen müssen und keine Klarnamenpflicht aufweisen. Das sind nur zwei Gründe, die es erschweren, die Seriosität des Angebots einzuschätzen. Gleichwohl bieten solche Foren sehr viel Hilfestellung: Wann immer Sie auf ein Problem stoßen und nicht weiter wissen - Irgendjemand wird dieses Problem auch schon gehabt und dort wahrscheinlich eine Antwort erhalten haben. Und sollten Sie dann Code aus entsprechenden Antworten übernehmen, auf den Sie nicht selbst gekommen sind, dann sollten Sie das transparent machen. Auch wenn es nicht die wissenschaftlichste Ressource ist, gehört sie doch oftmals zum Programmieralltag dazu. Angenommen, Sie hätten sich für die Lösung der Primzahlen-Aufgabe etwas Inspiration geholt, dann könnte ein Verweis auf einen Eintrag in einem Stackoverflow-Post wie folgt aussehen:  
    - Nach User: aatifh: Simple prime number generator in Python, in: Stackoverflow (2009), letzte Aktualisierung: 18.03.2009, URL: https://stackoverflow.com/a/568684 [letzter Aufruf: 19.07.2022].

Wie Sie es vom wissenschaftlichen Bibliographieren kennen, sollten Sie also nach Möglichkeit die folgenden Angaben machen:

- Name der Autor:innen
- Datum
- Titel des Beitrags oder Codes 
- ggf. Versionsnummer des Codes
- Publikationsorgan, URL, DOI

Manche Publikationsorgane schlagen Ihnen bereits Zitationsempfehlungen vor. Um die Webressourcen zu sichern, machen Sie gerne auch von der "Save Page Now"-Funktion der [Wayback Machine](https://archive.org/web/) des Internet Archive Gebrauch oder fertigen Sie eigene Screenshots als Nachweis für sich an. 

**Aber wo sollten Sie die Belege eigentlich angeben?**

Das kommt ganz auf den Kontext an. In jedem Fall sollten Sie die Referenzen direkt über die Kommentarfunktion in Ihren Code einfügen. So können Sie zu jederzeit nachvollziehen, an welchen Stellen Sie Code übernommen haben. Erscheint darüber hinaus eine Publikation, kann es erforderlich sein, im Rahmen des bibliographischen Apparats eine zusätzliche Rubrik für Source Code zu ergänzen.

Abschließend bleibt noch einmal zu betonen, dass es noch keine einheitlichen Empfehlungen gibt. Halten Sie bei wissenschaftlichen Arbeiten also immer noch mal Rücksprache mit Ihren Betreuer:innen, Herausgeber:innen oder Verlagen und fragen Sie, wie Sie mit der Nachnutzung von Code, der nicht im Rahmen von Programmbibliotheken publiziert wurde, umgehen sollen.

