import datetime
import calendar
import locale
from datetime import date
from datetime import timedelta
locale.setlocale(locale.LC_ALL, '')

days = range(7) # 1 bis 7
addDays = timedelta(days=1)
addWeek = timedelta(days=7)

tTable = '{|class="perrypedia_std_table" style="background:#CDCDC1;" '
tHeader = "! width=12,5% |<center>Montag</center>\n"
tHeader = tHeader + "! width=12,5% |<center>Dienstag</center>\n"
tHeader = tHeader + "! width=12,5% |<center>Mittwoch</center>\n"
tHeader = tHeader + "! width=12,5% |<center>Donnerstag</center>\n"
tHeader = tHeader + "! width=12,5% |<center>Freitag</center>\n"
tHeader = tHeader + "! width=12,5% |<center>Samstag</center>\n"
tHeader = tHeader + "! width=12,5% |<center>Sonntag</center>\n"

tVorlageBegin= "|----"
tVorlageZF = "|<center>[[Vorlage:Hauptseite_Zitate_KW{0:02}_{1}|Zitat-{0:02}]]&nbsp;/&nbsp;[[Vorlage:Hauptseite_Fakten_KW{0:02}_{1}|Fakt-{0:02}]]</center>"
tVorlageTag = "|<center>[[Vorlage:Hauptseite_BTW_{0:02}_{1:02}_{2}|{0}.&nbsp;{3:%B}]]</center>"
tVorlageEnde = "|}"

date_year = input('Eingabe des Jahres: ')
schaltjahr = calendar.isleap(int(date_year))

dt_checkKW = date(int(date_year), 1, 1)
if dt_checkKW.weekday() == 3:
	weeks = range(1, 54) #1 bis 53
	beginfd = 1
else:
	weeks = range(1, 53) #1 bis 52
	beginfd = 0
	
def writeheader(date):
	myyear=int(date.year)
	myyear=(2000-myyear)*-1
	print (tHeader.format(myyear))

def first_day_of_week(date):
	return date + datetime.timedelta(days = -date.weekday())

def print_day(date):
	myday=int(date.day)
	mymonth=int(date.month)
	myyear=int(date.year)
	print (tVorlageTag.format(myday,mymonth,myyear,date))

if beginfd == 0:
	datumBegin=first_day_of_week(dt_checkKW)+addWeek
if beginfd == 1:
	datumBegin=first_day_of_week(dt_checkKW)
	
print (tTable)
writeheader(dt_checkKW)
i=1
j=0
for i in weeks:
    print (tVorlageBegin)
    print (tVorlageZF.format(i,date_year))
    for j in days:
        print_day(datumBegin+timedelta(days=j))
    datumBegin=first_day_of_week(datumBegin+addWeek)

print (tVorlageEnde)
