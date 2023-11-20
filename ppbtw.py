import datetime
import locale
from datetime import date
from datetime import timedelta

# Jahr festlegen
jahreingabe = input('Eingabe des Jahres: ')
jahr = date(int(jahreingabe), 1, 1)

tTable = '{|class="perrypedia_std_table" style="background:#CDCDC1;\n' 
tTable = tTable + "! width=16% |<center>Fakt/Zitat</center>\n"
tTable = tTable + "! width=12% |<center>Montag</center>\n"
tTable = tTable + "! width=12% |<center>Dienstag</center>\n"
tTable = tTable + "! width=12% |<center>Mittwoch</center>\n"
tTable = tTable + "! width=12% |<center>Donnerstag</center>\n"
tTable = tTable + "! width=12% |<center>Freitag</center>\n"
tTable = tTable + "! width=12% |<center>Samstag</center>\n"
tTable = tTable + "! width=12% |<center>Sonntag</center>"

tVorlageBegin= "|----"
tVorlageZF = "|<center>[[Vorlage:Hauptseite_Zitate_KW{0:02}_{1}|Zitat-{0:02}]]&nbsp;/&nbsp;[[Vorlage:Hauptseite_Fakten_KW{0:02}_{1}|Fakt-{0:02}]]</center>"
tVorlageTag = "|<center>[[Vorlage:Hauptseite_BTW_{0:02}_{1:02}_{2}|{0}.&nbsp;{3:%B}]]</center>"
tVorlageEnde = "|}"

def print_day(date):
	myday=int(date.day)
	mymonth=int(date.month)
	myyear=int(date.year)
	print (tVorlageTag.format(myday,mymonth,myyear,date))

# Erstes Datum des Jahres abrufen
erstes_datum = datetime.date(int(jahreingabe), 1, 1)
print (tTable)

# Schleife über die Wochen des Jahres
woche = 1
while True:
    # Startdatum und Enddatum der aktuellen Woche berechnen
    start_datum = erstes_datum + datetime.timedelta(weeks=woche-1)
    end_datum = erstes_datum + datetime.timedelta(weeks=woche) - datetime.timedelta(days=1)
    
    # Überprüfen, ob das Enddatum außerhalb des aktuellen Jahres liegt (KW53 abfangen)
    if end_datum.year > start_datum.year:
        break
    print(tVorlageBegin)
    print (tVorlageZF.format(woche,jahreingabe))
	
    for tag in range((end_datum - start_datum).days + 1):
        # Datum für den aktuellen Tag berechnen
        datum = start_datum + datetime.timedelta(days=tag)
	# Ausgabe des aktuellen Tages mit Perry-Format
        print_day(datum)
        
    woche += 1
    
print (tVorlageEnde)
