#!/usr/bin/env python
# coding: utf-8

# # Lösungen zu den Aufgaben aus dem Abschnitt Programmabläufe strukturieren
# 

# ## Lösung: Aufgabe Bedingte Anweisungen
# 
# Schreiben Sie ein kleines Programm, das eine:n Nutzer:in fragt, aus welchem Jahr die Magna Carta stammt. Abhängig von der Eingabe sollen verschiedene `print`-Kommandos ausgeführt werden: "Die Magna Carta stammt aus einem späteren Jahr.", "Die Vereinbarungen stammen aus einem früheren Jahr.", "Die Eingabe ist korrekt!". 
# Denken Sie dabei daran, dass Sie den Wert der `input`-Funktion in ein `integer` umwandeln müssen. Wie das geht, können Sie im ersten Übungsnotebook ggf. noch mal nachlesen.

# In[ ]:


# guessing game

# Initiale Nutzer:inneneingabe, da ein Zahlenwert weiterverarbeitet werden soll, 
# wird die Eingabe direkt in ein Integer umgewandelt
user_input = int(input("Aus welchem Jahr stammt die Magna Carta? (Geben Sie eine Jahreszahl ein.)"))

# Zuweisung der gesuchten korrekten Antwort zu einer Variablen
correct_answer = 1215

# Prüfung, ob die Nutzer:inneneingabe der gesuchten Antwort entspricht oder zu hoch
# bzw. zu niedrig ist
if user_input == correct_answer:
    print("Die Eingabe ist korrekt!")
elif user_input > correct_answer:
    print("Die Vereinbarungen stammen aus einem früheren Jahr.")
else:
    print("Die Magna Carta stammt aus einem späteren Jahr.")


# ## Lösung: Aufgaben While-Schleife
# 
# **Aufgabe 1** Schreiben Sie ein kurzes Programm, das prüft, ob ein durch ein:e Nutzer:in eingegebenes Wort in dem vorgegebenen ersten Absatz eines [Tagungsberichts](https://www.hsozkult.de/conferencereport/id/tagungsberichte-6455?title=digitale-metamorphose-digital-humanities-und-editionswissenschaft&recno=2313&page=116&q=&sort=&fq=&total=8538) vorkommt. Wenn das Wort vorkommt, dann soll eine entsprechende Bestätigung ausgegeben werden. Kommt das Wort nicht im Text vor, soll der:die Nutzer:in die Möglichkeit erhalten, erneut eine Eingabe zu tätigen. Möchte der:die Nutzer:in keine weitere Eingabe tätigen, dann soll das Programm eine Abschlussmeldung ausgeben und beendet werden. 

# In[ ]:


# data
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

# Start des Programms mit einer Nutzereingabe, die genutzt werden kann, um eine sichere Abbruchbedingung 
# für die while-Schleife zu formulieren; 
# lower() wird genutzt, um die Eingabe robuster zu machen (nicht mehr case sensitive)
user_input = input("Möchten Sie das Programm zur Vorkommens-Prüfung starten? (J=Ja, N=Nein)").lower()

# while-Schleife, um zu gewährleisten, dass das Programm so lange läuft, 
# wie ein*e Nutzer*in eine Eingabe tätigen möchte.
# Sobald user_input nicht mehr "j" entspricht, wird die Schleife abgebrochen 
# und das Programm springt in die letzte Zeile
while user_input == "j":
    
    # Nutzereingabe für das Wort, das geprüft werden soll
    word = input("Für welches Wort möchten Sie prüfen, ob es im Text enthalten ist? ")
    
    # Prüfung des Vorkommens mit entsprechender Mitteilung und Möglichkeit ein weiteres Wort zu suchen.
    if word in report:
        print("Jawohl, dieses Wort ist im Text enthalten.")
        user_input = input("Möchten Sie ein weiteres Wort suchen? (J=Ja, N=Nein)").lower()  
    else:
        print("Das Wort ist leider nicht im Text enthalten.")
        user_input = input("Möchten Sie ein weiteres Wort suchen? (J=Ja, N=Nein)").lower()
        
print("Das Programm ist jetzt beendet. Vielen Dank fürs Mitmachen!")


# **Aufgabe 2 "Same but different":** Schreiben Sie ein kurzes Programm, das eine Benutzer\*in angeben lässt, in welchem Jahr die Französische Revolution begann. Das Programm soll dabei erst beendet werden, wenn das richtige Jahr angegeben wurde. Wurde ein falsches Jahr angegeben, soll der Nutzer\*in mitgeteilt werden, ob die Angabe zu groß, oder zu klein war. Testen Sie Ihr Programm mit unterschiedlichen Eingaben um herauszufinden, ob es funktioniert.

# In[ ]:


# Initiale Nutzer:inneneingabe, da ein Zahlenwert weiterverarbeitet werden soll, 
# wird die Eingabe direkt in ein Integer umgewandelt
user_input = int(input("In welchem Jahr begann die Französische Revolution? "))

# Zuweisung der gesuchten korrekten Antwort zu einer Variablen
correct_date = 1789

# while-Schleife, um zu gewährleisten, dass das Programm so lange läuft, wie die Nutzer:inneneingabe nicht 
# der gesuchten Anwort entspricht.
while user_input != correct_date:
    
    # Prüfung, ob die Nutzer:inneneingabe zu groß ist mit Option, einen neuen Tipp abzugeben
    if user_input > correct_date:
        user_input = int(input("Die Angabe war leider zu spät. Versuchen Sie es noch mal: "))
    else:
        user_input = int(input("Die Angabe war leider zu früh. Versuchen Sie es noch mal: ")) 

# Wurde das korrekte Jahr eingegeben, dann ist die Bedingung der While-Schleife nicht mehr erfüllt
# und sie wird beendet, damit ist dann auch unser Programm am Ende angelangt.
print("Das ist korrekt.")


# ## Lösung: Aufgabe Primzahlen ausgeben
# 
# **Knobelaufgabe für Zahlenbegeisterte** 
# 
# Wenden Sie das Gelernte an, indem Sie ein Programm schreiben, das mit `print()` alle [Primzahlen](https://de.wikipedia.org/wiki/Primzahl) zwischen 3 und 200 ausgibt. Zur Erinnerung: Primzahlen sind natürliche Zahlen, die nur durch 1 und durch sich selbst, nicht aber durch andere Zahlen kleiner als sie selbst teilbar sind. Falls Ihnen der Anfang schwer fällt, schauen Sie sich nochmal die Rechenoperatoren aus dem letzten Notebook an. Gegebenenfalls hilft es auch, wenn Sie sich ein Blatt Papier nehmen und in natürlicher Sprache eine auf Stichworten basierende Schritt-für-Schritt-Anleitung schreiben. Diese können Sie dann in Programmcode übersetzen. (Musterlösung folgt nach Abgabefrist)

# In[ ]:


# Wir legen einen Schalter fest, um eine boolesche Bedingung zu prüfen
is_prime = False

# Erste for-Schleife: Wir gehen alle Zahlen von 3 bis 200 durch und prüfen jedes Mal, 
# ob es sich um eine Primzahl handelt.
for number in range(3, 201):
    # Zweite for-Schleife: Für jede Zahl prüfen wir, ob sie sich durch eine Zahl kleiner 
    # als sie selbst teilen lässt.
    for divisor in range(2, number):
        # Wenn eine Zahl durch eine andere teilbar ist, ist der Rest der Division 0.
        # Wenn dieser Fall eintritt, kann es sich nicht um eine Primzahl handeln.
        if number % divisor == 0:
            is_prime = False
            break
        else:
            # An dieser Stelle dürfen wir die Schleife noch nicht abbrechen. 
            # Evtl. ist die zu prüfenden
            # Zahl i ja noch durch eine größere Zahl als der aktuelle Wert von j teilbar.
            is_prime = True
    
    # Erst wenn wir i durch alle Zahlen kleiner als sich selbst geteilt haben 
    # und bei jeder Division ein Rest übrig geblieben ist, 
    # können wir sicher sein, dass es sich um eine Primzahl handelt.
    if is_prime:
        print(number)

