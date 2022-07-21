#!/usr/bin/env python
# coding: utf-8

# # Programmabläufe strukturieren
# 
# Nachdem Sie nun bereits einige Grundlagen zur Programmierung in Python kennengelernt haben, werden wir diese nun ausbauen. Bisher hatten unsere Programme den folgenden Aufbau:
# 
# *Anweisung 1*
# 
# *Anweisung 2*
# 
# *Anweisung 3*
# 
# *usw.*
# 
# also in tatsächlichem Code gesprochen:

# In[ ]:


# percentage calculator
print('''Mit diesem Rechner erfahren Sie, 
wie viel Sie sparen können und wie hoch der Kaufbetrag ist.''')

# input
base = float(input("Geben Sie den Grundwert ein (Euro): "))
percentage = int(input("Geben Sie den Rabatt ein (%): "))

# calculate the percentage value and the remaining purchase amount
value = (base/100) * percentage
netto = base - value

# output
print(f"Sie sparen {value} Euro und müssen noch {netto} Euro bezahlen.")


# Den obigen Codeblock kennen Sie ja bereits aus einer der Aufgaben aus der [ersten Lektion](aufgabe-computer-als-taschenrechner).
# 
# In dieser Einheit lernen Sie nun einige grundlegende Befehle kennen, mit denen Sie den Ablauf Ihrer Programme strukturieren können: Bedingte Anweisungen, Schleifen und Funktionen. 
# 
# Hintergrund: Oft wollen Sie Teile Ihres Programms nur dann ausführen lassen, wenn bestimmte Rahmenbedingungen herrschen -- bspw. wenn eine Variable einen bestimmten Wert hat. So könnten Sie die Berechnung im obigen Beispiel etwa von einem bestimmten Grundwert abhängig machen (das ist natürlich nur ein fiktives Szenario). An anderer Stelle sollen Teile Ihres Codes wiederholt ausgeführt werden, allerdings ohne, dass Sie die Anweisungen immer wieder mühevoll ausschreiben müssen. Das ist zum Beispiel relevant, wenn wir mehrere Dateien wie Textquellen verarbeiten wollen. Aber dazu erfahren Sie in [späteren Kapiteln](../ch04-dateien-verarbeiten/01-dateien-verarbeiten.ipynb) mehr.
# 
# In dieser Lektion lernen wir erst einmal die Konzepte der bedingten Anweisungen, Schleifen und Funktionen kennen.

# ## Lernziele
# 
# Was Sie am Ende der Lektion beantworten können sollen:
# * Was sind Bedingte Anweisungen und wie lassen sie sich implementieren?
# * Was sind *booleans*?
# * Was sind Schleifen?
# * Was sind Funktionen?
# * Was ist Pseudocode?
