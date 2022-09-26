import datetime
import calendar
import locale
from datetime import date
from datetime import timedelta
locale.setlocale(locale.LC_ALL, '')

days = range(7) # 1 bis 7
addDays = timedelta(days=1)
addWeek = timedelta(days=7)

tVorlageBegin= "|----"
tVorlageZF = "|<center>[[Vorlage:Hauptseite_Zitate_KW{0:02}_{1}|Zitat-{0:02}]]&nbsp;/&nbsp;[[Vorlage:Hauptseite_Fakten_KW{0:02}_{1}|Fakt-{0:02}]]</center>"
tVorlageTag = "|<center>[[Vorlage:Hauptseite_BTW_{0:02}_{1:02}_{2}|{0}.&nbsp;{2:%B}]]</center>"
tVorlageEnde = "|}"

date_year = input('Eingabe des Jahres: ')

dt_checkKW = date(int(date_year), 1, 1)
if dt_checkKW.weekday() == 3:
    weeks = range(1, 54) #1 bis 53
else:
    weeks = range(1, 53) #1 bis 52

def first_day_of_week(date):
	return date + datetime.timedelta(days = -date.weekday())

def print_day(date):
	myday=int(date.day)
	mymonth=int(date.month)
	myyear=int(date.year)
	print (tVorlageTag.format(myday,mymonth,date))

datumBegin=first_day_of_week(dt_checkKW)+addWeek

i=1
j=0
for i in weeks:
    print (tVorlageBegin)
    print (tVorlageZF.format(i,date_year))
    for j in days:
        print_day(datumBegin+timedelta(days=j))
    datumBegin=first_day_of_week(datumBegin+addWeek)

print (tVorlageEnde)
