#!/usr/bin/env python
# coding: utf-8

# # [JSON](https://de.wikipedia.org/wiki/JavaScript_Object_Notation)
# 
# Einfache Textdateien, wie wir sie soeben eingelesen und geschrieben haben, sind für zahlreiche Anwendungsfälle schon sehr nützlich. Sie sind aber vergleichsweise unstrukturiert. Sehr oft wollen wir im Rahmen historischer Forschungsarbeiten aber mit eindeutig organsierten und strukturierten Informationen arbeiten. Wir können bei einem Korpus mit Briefen zum Beispiel folgende Informationen zu jedem Brief haben: Datum, Ort, Verfasser:in, Adressat:in, Brieftext sowie weiter Informationen. In einfachen Textdateien könnten wir nicht so ohne Weiteres auf diese Informationen zugreifen. Für solche Anwedungsszenarien gibt es allerdings eine Reihe von Dateiformaten, von denen wir im folgenden zwei genauer in den Blick nehmen werden.
# 
# JSON ist ein verbreites Dateiformat zur textbasierten Speicherung strukturierter Daten. Ursprünglich wurde es im Rahmen der Programmiersprache [*JavaScript*](https://de.wikipedia.org/wiki/JavaScript) (JSON ist ein Akronym für "JavaScript Object Notation") zum Austausch von Daten verwendet. Inzwischen ist das Format zu einem wichtigen Standard zur maschinenbasierten Kommunikation zwischen unterschiedlichen Plattformen geworden. Es ist unabhängig von bestimmten Programmiersprachen. Die Strukturierung von JSON-Dateien unterliegt nur [wenigen Regeln](https://www.json.org/json-en.html). Lesen Sie sich die Inhalte der verlinkten Seite in Ruhe durch.
# 
# ## Aufbau einer JSON-Datei
# 
# Betrachten wir einmal den Inhalt der Datei "library.json" in unserem Ordner "example_data". Es handelt sich hier nicht um einen ausführbaren Code:

# ```
# {
#     "label": "My Library",
#     "books available": true,
#     "owner": null,
#     "books": [
#         {
#             "title": "Der Prozess",
#             "author": "Franz Kafka",
#             "year": 1935,
#             "editions": [
#                 1935,
#                 1946,
#                 1963,
#                 1990,
#                 2011,
#                 2012
#             ]
#         },
#         {
#             "title": "Half of a Yellow Sun",
#             "author": "Chimamanda Ngozi Adichie",
#             "year": 2006,
#             "editions": [
#                 2006,
#                 2007,
#                 2017
#             ]
#         },
#         {
#             "title": "Network Effect",
#             "author": "Martha Wells",
#             "year": 2020,
#             "editions": [
#                 2020
#             ]
#         }
#     ]
# }
# ```

# Mit dem Wissen aus dem letzten Notebook wird Ihnen wahrscheinlich auffallen, dass der Inhalt der Datei wie eine Kombination aus Dictionaries und Listen aussieht. Tatsächlich sind die zugrundeliegenden Konzepte identisch. Einzig die Benennung ist etwas anders -- in JSON-Dateien heißen Dictionaries *Objekte*, Listen heißen *Arrays*. Ein weiterer feiner Unterschied ist die Verwendung von `null` für ein leeres Element in JSON. In Python verwenden Sie dagegen `None`, wenn eine Variable keinen Wert haben soll. Strings und Integers funktionieren, wie Sie es aus Python kennen.
# 
# Der Inhalt der JSON-Datei "library.json" besteht demnach aus einem Dictionary mit vier Schlüssel-Wert-Paaren ("label", "books available", "owner", "books"). In "books" ist eine Liste bzw. - im JSON-Sprech - ein Array gespeichert, das weitere Dictionaries respektive Objekte enthält. Jedes Dictionary / Objekt modelliert dabei ein einzelnes Buch.
# 
# Wenn Sie mit den hier verwendeten Begriffen Probleme haben, gehen Sie am besten nochmal die Abschnitte zu *Listen* und *Dictionaries* im letzten Kapitel durch.

# ## JSONs öffnen und speichern
# 
# Nun wollen wir ein Programm schreiben, mit dem wir die Datei "library.json" auslesen und um weitere Bücher erweitern können. Mit dem unten angeführten Code, den Sie bereits aus dem letzten Kapitel kennen, können Sie auch JSON-Dateien öffnen und bearbeiten. Allerdings können wir den Inhalt der Datei dann nur als String verarbeiten -- die Struktur aus Dictionaries und Listen geht verloren. Natürlich können wir auch ein Programm schreiben, dass an den richtigen Stellen die richtigen Klammern einfügt -- dies ist jedoch aufwändiger als den Inhalt der JSON-Datei in ein einzelnes Dictionary zu konvertieren. Hierzu stellt Python die Programmbibliothek `json` zur Verfügung. Um diese in Ihrem Programm verwenden zu können, muss diese zunächst importiert werden. Das geschieht, wenn Sie folgende Zeile ausführen:

# In[ ]:


import json


# Anschließend können wir den Inhalt der Datei mit der Funktion `load()` auslesen und als Dictionary in einer Variable speichern:

# In[ ]:


with open("example_data/library.json", "r") as json_file:
    library_content = json.load(json_file)

print(type(library_content))
print(library_content)


# Ab jetzt können wir die Daten weiterverarbeiten, wie im letzten Kapitel behandelt: Sie können damit wie mit jedem anderen Dictionary arbeiten. Mit folgendem Code können Sie etwa alle in der Bibliothek gespeicherten Buchtitel, Autor:innen und das Jahr der letzten Auflage auslesen:

# In[ ]:


book_list = library_content['books']

for book in book_list:
    print(f'''Das Buch '{book['title']}' von '{book['author']}' 
    wurde zuletzt im Jahr {book['editions'][-1]} aufgelegt.\n''')


# Änderungen an der *Datei* "library.json" können Sie ähnlich, wie im vorherigen Abschnitt beschrieben, vornehmen. Bereiten Sie zuerst die Dictionary-Variable vor, die den Inhalt der JSON-Datei speichert. Anschließend kann die Variable mit der Funktion `dump()` in eine JSON-Datei exportiert werden. Ähnlich wie die Funktion `write()`, die Sie weiter oben kennen gelernt haben, benötigt `dump()`, die Dictionary-Variable und ein Datei-Objekt als Parameter. Hier aktualisieren wir die fehlende Information unter "owner".

# In[ ]:


library_content['owner'] = "Max Mustermann"

with open("example_data/library_version_2.json", "w") as json_file:
    json.dump(library_content, json_file)


# Wenn Sie die JSON-Datei aus dem Ordner "example_data" heraus öffnen (zum Beispiel mittels Editor) werden Sie feststellen, dass der Inhalt nun in einer einzigen Zeile gespeichert ist. Insbesondere bei sehr großen JSON-Dateien lässt sich so Speicherplatz sparen. Zur Erinnerung: Zeilenumbrüche und Tabstobs werden durch "\\n" bzw. "\\t" repräsentiert; auch einzelne Zeichen verbrauchen Speicherkapazität. Oft müssen Sie bei der Arbeit mit JSON-Dateien aber auch in die Dateien reinschauen; hier helfen dann Zeilenumbrüche und Einrückungen. Sie können der Funktion `dump()` einen weiteren Parameter (`indent`) mit der Anzahl der Einrückungen nach einem Zeilenumbruch übergeben. Auf diese Weise wird die JSON-Datei lesbarer:

# In[ ]:


library_content['owner'] = "Maxine Musterfrau"

with open("example_data/library_version_2.json", "w") as json_file:
    json.dump(library_content, json_file, indent = 4)


# Wenn Sie die JSON-Datei nun noch einmal öffnen, dann sollte sie sich schon sehr viel übersichtlicher darstellen.

# ## JSON in der Digital History: IIIF
# 
# Ein zunehmend wichtig werdender Datenstandard im Cultural-Heritage-Bereich ist das [*International Image Interoperability Framework (IIIF)*](https://iiif.io/) (Aussprache: Triple-I-F). Es wurde ursprünglich von verschiedenen GLAM-Einrichtung (Galleries, Libraries, Archives, Museums) entwickelt. Ziel war es, ein standardisiertes Framework für ein Datenmodell zu schaffen, um bildbasiertes Kulturgut interoperabel, also unabhängig von den sich unterscheidenden Standards unterschiedlicher Kultureinrichtungen, online präsentieren und austauschen zu können. Dabei sollten nicht nur Metadaten zur Beschreibung des Kontextes der einzelnen Kulturgutobjekte gespeichert werden können, sondern insbesondere bei Werken, die aus mehreren Bilddateien bestehen, logische Zusammenhänge zwischen den Einzelbildern für das Gesamtwerk erhalten werden. Die Anwendungsmöglichkeiten von IIIF sind sehr vielfältig; [zahlreiche Einrichtungen und Projekte](https://github.com/IIIF/awesome-iiif) greifen mittlerweile darauf zurück.
# 
# Sie müssen sich für diese Einführung nicht intensiv in IIIF einarbeiten. In der folgenden Übungsaufgabe werden wir uns ausschließlich auf die [Presentation API](http://ronallo.com/iiif-workshop/presentation/) konzentrieren. In aller Kürze beschrieben definiert die *Presentation API* einen Standard zur Strukturierung einer JSON-Datei um die Zusammenhänge eines bildbasierten Werkes beschreiben zu können ([Vollständige Dokumentation der *Presentation API*](https://iiif.io/api/presentation/3.0/)). Eine solche Datei wird *Manifest* genannt.
# 
# In der folgenden Aufgabe werden wir mit mittelalterlichen Handschriften arbeiten. Eine einzelne Handschrift kann als ein einzelnes, bildbasiertes Werk verstanden werden. Beachten Sie dabei, dass es hier um das tatsächliche Buch, das in irgendeiner Bibliothek liegt, geht -- nicht um den Text der Handschrift oder um Faksimiles. Eine Handschrift kann somit durch ein IIIF-Manifest repräsentiert werden. Betrachten wir z.B. das Manuskript "Grandes Chroniques de France"; Sie finden es im Ordner im Pfad "example_data/iiif-manifests" unter "BnF. Departement des Manuscrits. Français 2608.json". Wir müssen an dieser Stelle nicht auf jedes Detail genau eingehen. Metadaten der Handschrift sind in der Liste "metadata" gespeichert. Hier finden Sie z.B. den Titel, die Datierung oder die Sprache, in der der Text verfasst ist. Das Manifest enthält außerdem die Links zu den Bilddateien der Scans der einzelnen Seiten. Diese sind im Manifest in der Liste "canvases" gespeichert (die ein Dictionary in der Liste "sequences" ist). Jede Seite der Handschrift wird dabei durch ein "canvas"-Dictionary repräsentiert. Um den Link zur Bilddatei der jeweiligen Seite zu finden, suchen Sie in der Liste "images" nach dem Schlüssel "@id".[^fn1] Der Link zur Bilddatei der ersten Seite der "Grandes Chroniques de France" ist z.B. [https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/f1/full/full/0/native.jpg](https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/f1/full/full/0/native.jpg). Schauen Sie sich die JSON-Datei gut an und vollziehen Sie ihren Aufbau nach.
# 
# Hier ein Auszug der ersten 130 Zeilen der JSON-Datei, die insgesamt mehr als 30.000 Zeilen umfasst.

# In[ ]:


'''
{
    "@id": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/manifest.json",
    "label": "BnF. Département des Manuscrits. Français 2608",
    "attribution": "Bibliothèque nationale de France",
    "license": "https://gallica.bnf.fr/html/und/conditions-dutilisation-des-contenus-de-gallica",
    "logo": "https://gallica.bnf.fr/mbImage/logos/logo-bnf.png",
    "related": "https://gallica.bnf.fr/ark:/12148/btv1b8451604g",
    "seeAlso": [
        "http://oai.bnf.fr/oai2/OAIHandler?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:bnf.fr:gallica/ark:/12148/btv1b8451604g"
    ],
    "description": "Grandes Chroniques de France",
    "metadata": [
        {
            "label": "Repository",
            "value": ""
        },
        {
            "label": "Digitised by",
            "value": "Bibliothèque nationale de France"
        },
        {
            "label": "Source Images",
            "value": "https://gallica.bnf.fr/ark:/12148/btv1b8451604g"
        },
        {
            "label": "Metadata Source",
            "value": "http://oai.bnf.fr/oai2/OAIHandler?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:bnf.fr:gallica/ark:/12148/btv1b8451604g"
        },
        {
            "label": "Shelfmark",
            "value": "Bibliothèque nationale de France. Département des Manuscrits. Français 2608"
        },
        {
            "label": "Title",
            "value": "Grandes Chroniques de France"
        },
        {
            "label": "Date",
            "value": "1390-1405"
        },
        {
            "label": "Language",
            "value": [
                {
                    "@value": "français"
                },
                {
                    "@value": "latin"
                }
            ]
        },
        {
            "label": "Format",
            "value": "Paris. - Écriture bâtarde. Un copiste. Hastes montantes avec parfois grotesques dans la marge supérieure. - Décoration: Selon A. Hedeman, le ms. aurait été exécuté sur le modèle du ms. de Charles V, le ms. BnF Français 2813. Il se distingue cependant de son modèle pour suivre le découpage en chapitres d’une autre copie royale, le ms. BnF, Français 10135. Une vingtaine de miniatures se retrouvent par ailleurs dans deux mss contemporains, les mss Vienne, ÖNB, Cod. 2564 et Lyon, BM, ms. 880. Reflétant l’évolution de la situation politique, l’ensemble du cycle d’enluminures offre une « vision atténuée du conflit franco-anglais » (Rioust – Karaskova 2015, p. 12) : la plupart des peintures traitant de la suprématie française sur les Anglais ont été omises, sans doute parce que la France a entrepris des négociations de paix avec l’Angleterre dans les années 1390. Les Anglais mis en scène par l’artiste n’apparaissent plus à leur désavantage : f. 481v : siège de Reims (1359/1360) ; f. 483v : traité de Brétigny (8 mai 1360) ; f. 521v : couronnement de Richard II, futur gendre de Charles VI (cf. Hedeman, The royal Image…, p. 140). Bien que le ms. ait été commandé pour Charles VI, le ms. ne contient aucune représentation de son sacre, reflet des absences du roi (Rioust – Karaskova 2015, p. 11). Les différentes chroniques sont généralement introduites par un portrait du roi couronné. On note qu’aucune illustration ni initiale ornée n’annoncent l’avènement du règne de Philippe de Valois, marqué par l’extinction de la dynastie des Capétiens directs. Bien que la décoration marginale indique une provenance parisienne, le style des illustrations est caractéristique de l’enluminure pragoise des années1390 et peut être attribué à un maître bohémien venu travailler à Paris (Paris 1400…, cat. 168, p. 272-273 ; Rioust – Karaskova 2015, p. 16-18). Les petits fleurons qui partent de chaque angle des peintures se retrouvent dans plusieurs manuscrits commandités par Wenceslas IV de Bohême ou son entourage: la Bible dite de Wenceslas (Vienne, ÖNB, Cod. 2759-64), le Livre d'heures du Narodni Muzeum (Prague, Narodni Muzeum, KNM VH 36), le Psautier de Raudnitz (Prague, cathédrale Saint vit, Cim. 7), la Bible ms. M. 833 de la Pierpont Morgan Library (New York), la Bulle d'Or de Vienne (Vienne, ÖNB, Cod. 338), la Bible de Konrad von Vechta (Anvers, Museum Plantin-Moretus, Cod. MS 15.1-15.2), copiés dans les premières années du XVe siècle (Rioust – Karaskova 2015, p. 16-18). Une peinture frontispice (175 x 160 mm) au f. 2v ; 75 peintures de petit format. F. 1 : moine présentant la chronique à saint Louis et saint Denis, symbolisant l’un, un modèle de bon gouvernement pour ses successeurs, l’autre, le protecteur du royaume mais aussi de la santé royale dans l’épreuve de la maladie de Charles VI. Bien que le roi ne soit pas représenté, sa personne est évoquée à travers les armes portées par deux cerfs ailés, son emblème favori dans les deux dernières décennies du XIVe siècle. F. 2v. Peinture frontispice compartimentée en quatre scènes : débarquement des Grecs à Troie ; siège de Troie ; couronnement de Pharamond ; bataille entre les Francs et les Romains, symbolisant la chute de l’empire et la suprématie de la royauté française, mettant en lumière l’ancienneté et la noblesse des Francs et leur suprématie sur l’empire (cf. M.-H. Tesnière, dans Trésors de la Bibliothèque nationale…, cat. 33). Légendes des illustrations : voir Hedeman, The Royal Image…, p. 239-240, et la base Mandragore : www. Mandragore.bnf.fr Décoration secondaire :Encadrements de baguettes avec rinceaux de vignettes et dragon (f. 1). Dans la marge inférieure du f. 1 deux cerfs ailés supportent les armoiries royales. Au f. 2v, armoiries de Jean du Mas.Initiales ornées de vignettes (5 lignes) au début du prologue et des différentes parties du texte (début des Chroniques, des différents livres des Chroniques des règnes de Charlemagne et de Philippe Auguste, des chapitres ornés d’une peinture).Lettres filigranées (2 lignes) au début des autres chapitres et des tables des chapitres. Lettres filigranées (1 ligne) au début des têtes de chapitres indiqués dans les tables et au sein du texte. - Parchemin. - 544 ff. précédés de trois feuillets de garde en parchemin (A, B, C) ; suivis d’un feuillet de garde en parchemin. - 350 x 255 mm (justification : 235/240 x 175 mm). - 46 cahiers : 112 (f. 1-12) ; 212 (f. 13-24) ; 312 (f. 25-34) ; 412 (f. 35-48) ; 512 (f. 49-60) ; 612 (f. 61-72) ; 712 (f. 73-84) ; 812 (f. 85-96) ; 912 (f. 97-108) ; 1012 (f. 109-120) ; 1112 (f. 121-132) ; 1212 (f. 133-144) ; 1312 (f. 145-156) ; 1412 (f. 157-168) ; 1512 (f. 169-180) ; 1612 (f. 181-192) ; 1712 (f. 193-204) ; 1812 (f. 205-216) ; 1912 (f. 217-228) ; 2012 (f. 229-240) ; 2112 (f. 241-252) ; 2212 (f. 253-264) ; 2312 (f. 265-276) ; 2412 (f. 277-288) ; 2512 (f. 289-300) ; 2612 (f. 301-311, incluant un feuillet 304bis) ; 2712 (f. 312-323) ; 2812 (f. 324-335) ; 2912 (f. 336-347 ; les f. 339 et 344, mal reliés, sont à inverser) ; 3012 (f. 348-359) ; 3112 (f. 360-371) ; 3212 (f. 372-383) ; 3312 (f. 384-395) ; 3412 (f. 396-407) ; 3512 (f. 408-419 ; f. 413-414 mal reliés et à inverser) ; 3612 (f. 420-431) ; 3712 (f. 432-442, incluant un feuillet 432bis) ; 3812 (f. 443-454) ; 3912 (f. 455-466) ; 4012 (f. 467-478) ; 4112 (f. 479-490) ; 4212 (f. 491-502) ; 4312 (f. 503-514) ; 4412 (f. 515-526) ; 4512 (f. 527-538) ; 466 (f. 539-544). Réclames, signatures apparentes de cahiers à l’encre brune et rouge. Deux colonnes par page.Foliotation contemporaine du manuscrit en chiffres romains rubriqués. Titres courants rubriqués dans la marge supérieure ; certains titres ne correspondent pas à la geste indiquée : f. 308-311v, le récit du règne de Louis VIII a pour titre : « Du roy Philippe Dieudonné ». Foliotation moderne : omission des f. 304bis, 432bis. Feuillets mal reliés dans les cahiers 29 et 35. Incipit du volume, des tables des chapitres et des différentes gestes, titres des chapitres avec leur numérotation rubriqués. Lettres en attente pour les lettres filigranées et certaines initiales ornées.Traces de restauration ancienne. Tables des chapitres jusqu’à la chronique du règne de Louis VIII (f. 308). Annotations marginales contemporaines du manuscrit : f. 501r-v. Annotations marginales postérieures (XIXe s.) : f. 94, 166, 338v, 339v. - Réglure à l’encre. - Reliure en maroquin brun avec armes royales sur les plats (Ancien Régime), à triple filet doré. Tranche dorée. Dos au chiffre royal (Ancien Régime, avant 1792). Titre en capitales dorées : « CHRONIQUE. DE FRANCE / APPELLEES. DE S. DENYS. / FINISSANT . A CHARL. VI. ». - F. 1 et 543v : estampille de la « Bibliothecae Regiae » (Ancien régime, avant 1725), correspondant au modèle Josserand-Bruno, type A, n° 1"
        },
        {
            "label": "Relation",
            "value": "Notice du catalogue : http://archivesetmanuscrits.bnf.fr/ark:/12148/cc779857"
        },
        {
            "label": "Type",
            "value": "Manuscrit"
        },
        {
            "label": "Place",
            "value": "Lieu de copie : Paris"
        }
    ],
    "sequences": [
        {
            "canvases": [
                {
                    "@id": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/canvas/f1",
                    "label": "plat supérieur",
                    "height": 6275,
                    "width": 4555,
                    "images": [
                        {
                            "motivation": "sc:painting",
                            "on": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/canvas/f1",
                            "resource": {
                                "format": "image/jpeg",
                                "service": {
                                    "profile": "http://library.stanford.edu/iiif/image-api/1.1/compliance.html#level2",
                                    "@context": "http://iiif.io/api/image/1/context.json",
                                    "@id": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/f1"
                                },
                                "height": 6275,
                                "width": 4555,
                                "@id": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/f1/full/full/0/native.jpg",
                                "@type": "dctypes:Image"
                            },
                            "@type": "oa:Annotation"
                        }
                    ],
                    "thumbnail": {
                        "@id": "https://gallica.bnf.fr/ark:/12148/btv1b8451604g/f1.thumbnail"
                    },
                    "@type": "sc:Canvas"
                },
                {
                    "@id": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/canvas/f2",
                    "label": "contreplat sup.",
                    "height": 6217,
                    "width": 4584,
                    "images": [
                        {
                            "motivation": "sc:painting",
                            "on": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/canvas/f2",
                            "resource": {
                                "format": "image/jpeg",
                                "service": {
                                    "profile": "http://library.stanford.edu/iiif/image-api/1.1/compliance.html#level2",
                                    "@context": "http://iiif.io/api/image/1/context.json",
                                    "@id": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/f2"
                                },
                                "height": 6217,
                                "width": 4584,
                                "@id": "https://gallica.bnf.fr/iiif/ark:/12148/btv1b8451604g/f2/full/full/0/native.jpg",
                                "@type": "dctypes:Image"
                            },
                            "@type": "oa:Annotation"
                        }
                    ],
                    "thumbnail": {
                        "@id": "https://gallica.bnf.fr/ark:/12148/btv1b8451604g/f2.thumbnail"
                    },
                    "@type": "sc:Canvas"
                },
'''


# 
# Angenommen, Sie wollen nun die Scans aller Seiten der Handschrift herunterladen. In diesem Fall können Sie natürlich auch die Handschrift im [Viewer der französischen Nationalbibliothek](https://gallica.bnf.fr/ark:/12148/btv1b8451604g) aufrufen und die Digitalisate dort herunterladen. Wollen Sie das jedoch für mehrere Dutzend oder gar Hundert Handschriften tun, bieten Ihnen die IIIF-Manifeste eine Möglichkeit den Download automatisiert durchzuführen.

# ## Aufgabe: JSON-Daten verarbeiten
# Schreiben Sie ein Programm zur Vorbereitung eines automatischen Downloads aller Bilddateien der Scans einer Reihe von vorgegebenen mittelalterlichen Handschriften. Die IIIF-Manifeste der einzelnen Handschriften finden Sie in im Ordner data/iiif-manifests. Ihr Programm sollte die folgenden Aufgaben durchführen:
# * Die Links zu den Bilddateien der Scans sollten in einer Textdatei (.txt) gespeichert werden. Nach jedem Link soll ein Zeilenumbruch erfolgen. Die Links werden also zeilenweise in der Datei aufgelistet.
# * Es soll für jede Handschrift jeweils eine eigene Textdatei erstellt werden, die die Links zu ihren Scans enthält.
# * Der Name jeder Textdatei soll der Titel der jeweiligen Handschrift sein (also z.B. "Grandes Chroniques de France.txt").
# * *Optional: Extrahieren Sie nur die Links aus den IIIF-Manifesten, deren Handschriften irgendwann zwischen den Jahren 1300 und 1400 datiert sind.*

# In[ ]:


folder_path = ".example_data/iiif-manifests/"
manifests = [
      "BnF. Departement des Manuscrits. Francais 2170.json",
      "BnF. Departement des Manuscrits. Francais 2187.json",
      "BnF. Departement des Manuscrits. Francais 1950.json",
      "BnF. Departement des Manuscrits. Francais 2196.json",
      "BnF. Departement des Manuscrits. Francais 2228.json",
      "BnF. Departement des Manuscrits. Francais 2608.json"       
]

# Ihr Code


# In[ ]:


# hidden cell creates content for using with Thebe Live-Code
# >>>change paths, when Jupyter Book is published<<<

import requests
import os

data_folder = 'example_data'

try:
    os.mkdir(data_folder)
except:
    pass

iiif_folder = 'example_data/iiif-manifests'

try:
    os.mkdir(iiif_folder)
except:
    pass  
  
file_list_1 = [('adliger_vergleich.txt', 'https://raw.githubusercontent.com/martindroege/jb-example-data/main/adliger_vergleich.txt'),
             ('books.csv', 'https://raw.githubusercontent.com/martindroege/jb-example-data/main/books.csv'),
             ('library.json', 'https://raw.githubusercontent.com/martindroege/jb-example-data/main/library.json')]

for file_name, url in file_list_1:
    response = requests.get(url)

    with open(f'example_data/{file_name}', 'w', encoding='UTF8') as f:
        f.write(response.text)
        
file_list_2 = [1950, 2228, 2608, 2170, 2187, 2196]
base_url = 'https://raw.githubusercontent.com/martindroege/jb-example-data/main/iiif-manifests/BnF.%20Departement%20des%20Manuscrits.%20Francais%20'
base_file_name = 'BnF. Departement des Manuscrits. Francais '

for i in file_list_2:
    response = requests.get(f'{base_url}{str(i)}.json')

    with open(f'{iiif_folder}/{base_file_name}{str(i)}.json', 'w', encoding='UTF8') as f:
        f.write(response.text)


# [^fn1]: "images" muss eine Liste sein, da ein IIIF-"canvas" auch aus mehreren Bilddateien bestehen kann. So kann etwa im Manifest abgebildet werden, dass zu einer Seite einer Handschrift nur Fragmente existieren; jedes Fragment kann durch eine eigene Bilddatei dargestellt werden. Das nur als kleines Beispiel für die Flexibilität von IIIF.
