(jupyter-book-nutzung)=
# Zur Nutzung dieses Jupyter Books

Gerne möchten wir Ihnen noch ein paar einführende Worte zur Nutzung dieses Jupyter Books mitgeben, um Ihnen den Einstieg so einfach wie möglich zu gestalten. 

## Wie ist das Jupyter Book aufgebaut?

Dieses Jupyter Book setzt sich aus einer Reihe von Textseiten (Markdown-Dateien) und Jupyter Notebooks zusammen, die Sie über das Kapitelmenü auf der linken Seite jeweils ansteuern können. Bei Jupyter Notebooks handelt es sich um ein Dateiformat (zu erkennen an der Endung `.ipynb`), das Text, Bilder, Programmcode und dessen Ausführung inklusive der Anzeige von Ergebnissen in einem einzelnen Dokument integriert. Das macht es zu einem hervorragenden Instrument zur Vermittlung von Programmierkenntnissen. 

```{figure} ../img/einfuehrung/contents.png
:width: 400px
:align: center
```

Die einzelnen Kapitel folgen in der Regel einem einheitlichen Aufbau: Zu Beginn werden die Lernziele festgelegt, so dass Sie am Ende für sich noch einmal prüfen können, ob Sie die aufgeworfenen Fragen für sich beantworten können. Den umfangreichsten Teil der Notebooks nimmt die Vermittlung der einzelnen Lehrinhalte anhand der Notebooks ein. Neben erläuternden Passagen finden Sie in den Unterkapiteln immer auch Codebeispiele zur Illustration. Unter "Contents" in der rechten Menüleiste erhalten Sie einen schnellen Überblick über die jeweiligen Abschnitte. Jedes Kapitel enthält zudem größere und kleinere Programmierprobleme, die Sie selbstständig lösen können und sollen. 

Bitte beachten Sie stets, dass die jeweiligen Kapitel mit ihren Codeblöcken **sequenziell** aufgebaut sind. Das heißt, Sie sollten bei der Bearbeitung der einzelnen Kapitel stets die Codeblöcke **nacheinander** ausführen, da ein späterer Codeabschnitt sich auf einen früheren beziehen kann. Das ist insbesondere dann relevant, wenn in einem ersten Codeblock *A* Werte zu Variablen zugewiesen werden, die in einem späteren Codeblock *B* verarbeitet werden sollen. Codeblock *B* kann diese Verarbeitung erst vornehmen, wenn Codeblock *A* zuvor ausgeführt und die Wertzuschreibung damit erfolgt ist. Gehen Sie die Notebooks mit den Codeblöcken also immer Schritt für Schritt durch.

## Wie funktioniert das Jupyter Book?

```{figure} ../img/einfuehrung/icons_binder-live-code.png
:figclass: margin
```

Um den vorgegebenen aber auch selbst konzpierten Code auszuführen, haben wir zwei Optionen eingebunden, die es Ihnen ermöglichen, die Notebooks **vollständig online** zu bearbeiten. Sie müssen sich also nicht um die Installation von Python und entsprechender Zusatzsoftware kümmern (falls Sie das trotzdem gerne möchten und noch nicht so genau wissen, worauf zu achten ist, schauen Sie einmal **[hier](installationsempfehlungen)**). Konkret stehen Ihnen zur Nutzung [Binder](https://mybinder.org/) und *Live Code* zur Verfügung, die Sie über das Raketensymbol im Navigationsmenü des jeweiligen Kapitels auswählen können.

```{figure} ../img/einfuehrung/binder-info.png
:width: 400px
:align: center
```

Durch Klicken auf “Binder” wird nach einem kurzen Ladevorgang das vollständige GitHub-Repositorium des Jupyter Books in einer externen Umgebung geöffnet. Über den "File Browser" können die Notebooks der unterschiedlichen Kapitel aufgerufen, interaktiv bearbeitet und ausgeführt werden. Sie erkennen die einzelnen Kapitel an der Ordner- und Dateibenennung. Die Nutzung von Binder ermöglicht es, weitere Text- oder Codeblöcke in die Notebooks einzufügen (etwa um eigene Notizen und Beobachtungen zu dokumentieren oder weiteren Code zu produzieren). Nutzen Sie dazu einfach die entsprechenden Funktionen in der Menüleiste des Notebooks. Das Play-Icon sorgt beispielsweise dafür, dass ein Codeblock ausgeführt wird und das Plus-Symbol fügt eine Codezelle zum Notebook hinzu. 

```{figure} ../img/einfuehrung/live-code.png
:width: 400px
:align: center
```

Wenn Sie lieber in der Umgebung des Jupyter Books bleiben möchten, bietet sich die Nutzung von "Live Code" an. Im Hintergrund lädt das an Binder anschließende Projekt Thebe das aktuell vorliegende Kapitel und sorgt dafür, dass die Codeinhalte direkt ausführbar und bearbeitbar sind. Dazu werden zu den entsprechenden Zellen verschiedene Button ergänzt. Den Code in den Zellen können Sie nach Belieben verändern und den Output inspizieren. Der Vorteil ist, dass Sie nicht auf eine externe Seite weitergeleitet werden. Sie können allerdings keine neuen Code- oder Textblöcke in das Notebook einfügen, sondern eben nur bestehende Codeabschnitte bearbeiten. Probieren Sie gerne beide Varianten aus und entscheiden Sie für sich, womit Sie am komfortabelsten arbeiten können. Für welche der Varianten Sie sich auch entscheiden: Sie benötigen zur Bearbeitung des Jupyter Books lediglich einen Browser sowie eine stehende Internetverbindung. 

```{figure} ../img/einfuehrung/icons_download.png
:figclass: margin
```

Natürlich können Sie die Notebooks aber auch lokal mit Ihrer persönlichen Programmierumgebung auf Ihrem Rechner bearbeiten. Über den Downloadbutton können die einzelnen Notebooks als `.ipynb`-Datei heruntergeladen werden. Auch die Möglichkeit eines PDF-Exports steht zur Verfügung, ist für die interaktive Arbeit mit dem Jupyter Book aber weniger gut geeignet.

## Wo finden Sie zusätzliche Materialien?

Für einige Kapitel und Aufgaben werden zusätzliche Materialien wie konkrete Quellen benötigt. **[Hier](/ch-daten/part01-python-basics-daten.ipynb)** finden Sie die entsprechenden Datensätze hinterlegt.

Nachdem Sie die einzelnen Programmieraufgaben durchgearbeitet haben, möchten Sie vielleicht in Erfahrung bringen, ob Ihr Lösungsweg in die richtige Richtung geht: **[Hier](/ch-loesungen/part01-python-basics-loesungen.ipynb)** haben wir einige Musterlösungen gesammelt, mit denen Sie Ihren eigenen Code vergleichen können. Wichtig ist: Es gibt *nicht* den einen richtigen Weg, ein Programmierproblem zu lösen. Wenn Sie mögen, können Sie uns also Ihre Lösung als weiteres Codebeispiel zur Verfügung stellen, von dem wiederum andere lernen können. 

Zusätzlich werden unter **[Ressourcen](ressourcen)** stets weitere Materialien zu den jeweiligen Einheiten vorgeschlagen, die Sie ergänzend zu den Erläuterungen und Programmierbeispielen für die Bearbeitung der Aufgaben heranziehen können, dabei haben wir einen Mix aus text- und videobasierten Angeboten zusammengetragen. Die Ressourcenliste wird regelmäßig erweitert. Gerne nehmen wir Vorschläge von Ihnen auf.

## Wie können Sie uns Ihr Feedback mitteilen?

```{figure} ../img/einfuehrung/icons_git.png
:figclass: margin
```

Wenn Sie mit diesem Jupyter Book gearbeitet haben, freuen wir uns über Ihr Feedback. Schreiben Sie uns gerne eine E-Mail an digitalhistory@hu-berlin.de oder hinterlassen Sie einfach Ihre Kommentare und Anregungen über die Issue-Funktion direkt in den jeweiligen Kapiteln des Jupyter Books.