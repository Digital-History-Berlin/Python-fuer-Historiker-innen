#!/usr/bin/env python
# coding: utf-8

# # Pseudocode
# 
# Pseudcode hilft beim Strukturieren von Programmabläufen und unterstützt das algorithmische Denken. Dabei werden Probleme eines Programms in einzelne Schritte zerlegt, danach werden die auf diese Weise identifizierten Teilschritte zunächst generalisiert ausformuliert und als einzelne Bausteine wieder zusammengestellt. Ein Pseudcode, um zunächst zu prüfen, ob in einem Text Vokale enthalten sind, um diese danach auszugeben, könnte etwa wie folgt aussehen: 
# 
#     TEXT =  "text"
# 
#     LOOP OVER TEXT
# 
#         IF ELEMENT IS VOWEL
#     
#             PRINT ELEMENT
# 
# Durch das Ausformulieren eines Programmablaufs in Pseudocode wird das Vorgehen klarer und mögliche Konzept, die zur Lösung einer Problemstellung in Frage kommen, können auf diese Weiser leichter verstanden werden. Pseudocode liefert damit eine Vorlage, die zur Orientierung beim Schreiben des eigentlichen Codes dient. Zugleich ist Pseudocode auf alle Programmiersprachen übertragbar. Nachfolgend findet sich eine weitere beispielhafte Problemstellung, die zunächst in Pseudocode übersetzt und dann in Pythoncode ausgeschrieben ist. 
# 
# Für die Zahlen zwischen 1 und 50 soll:
# 
# * FizzBuzz ausgegeben werden, wenn die Zahl durch 3 und 5 teilbar ist
# * Fizz ausgegeben werden, wenn die Zahl durch 3 teilbar ist
# * Buzz ausgegeben werden, wenn die Zahl durch 5 teilbar ist
# 
# In Pseudocode geschrieben, sieht das Programm beispielweise wie folgt aus:
# 
#     FOR i from 1 TO 50 DO
#         IF i is divisible by 3 AND i is divisible by 5 THEN
#             OUTPUT "FizzBuzz"
#         ELSE IF i is divisible by 3 THEN
#             OUTPUT "Fizz"
#         ELSE IF i is divisible by 5 THEN
#             OUTPUT "Buzz"
#         ELSE
#             OUTPUT i
# 
# In Python ausformuliert ergibt sich der folgende Code:

# In[ ]:


for i in range(1,50):
    
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        
    elif i % 3 == 0:
        print('Fizz')
        
    elif i % 5 == 0:
        print('Buzz')
        
    else:
        print(i)

