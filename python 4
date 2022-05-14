import os
import time
global lijstvanwoordlijsten
geselecteerdelijstinlijst = []
geselecteerdelijst = ""
lenscherm = 45

def printregel(input):
  b = input
  print("|{:<43}|".format(b.strip('\n \r\t')))

def printtop():
  print("="*lenscherm)

def printbottom():
  print("=" * lenscherm)

def leegscherm():
  os.system('cls||clear')

def maine():
  printtop()
  printregel("1. nieuwe woordenlijst maken")
  printregel("2. selecteer een lijst")
  printregel("3. woorden toevoegen aan woordenlijst")
  printregel("4. woordenlijst overhoren")
  printregel("5. het progamma stoppen")
  printbottom()

def nieuwewoordenlijstmaken():
  leegscherm()
  global woordje
  global betekenis
  global naamlijst
  doorgaan = True
  printtop()
  printregel("hoe moet je lijst heten??? (")
  printregel("gebruik wel een andere naam dan")
  printregel("een van de anderewoordenlijsten)")
  printbottom()
  naamlijst = input(' ')
  lijstvanwoordlijsten = open('lijstvanwoordlijsten', "a")
  lijstvanwoordlijsten.write("\n")
  lijstvanwoordlijsten.write(naamlijst)
  lijstvanwoordlijsten.close()
  while doorgaan:
    f = open(naamlijst, "a")
    printtop()
    woordje = input('wat is het woordje: ')
    betekenis = input('wat is de betekenis: ')
    printbottom()
    f.write(woordje + " - " + betekenis)
    f.write("\n")
    f.close()
    if input('nog een woordje? y/n') == "y":
      doorgaan = True
    else:
      doorgaan = False

def selecteereenwoordenlijst():
  leegscherm()
  global w
  global a
  global n
  global nint
  global lijstvanwoordlijsten
  global geselecteerdelijst
  global geselecteerdelijstnummer
  global geselecteerdelijstinlijst

  geselecteerdelijstinlijst = []
  w = open('lijstvanwoordlijsten')
  for line in w:
    geselecteerdelijstinlijst.append(line)
  printtop()
  printregel("welk van deze lijsten wil je selecteren:")
  for i in range(len(geselecteerdelijstinlijst)):
    n = i
    nint = str(n)
    a = nint + ". " + geselecteerdelijstinlijst[i]
    printregel("")
    printregel(a)
    printregel("")
  printbottom()
  geselecteerdelijstnummer = input('')
  geselecteerdeint = int(geselecteerdelijstnummer)
  geselecteerdelijst  =  geselecteerdelijstinlijst[geselecteerdeint]
  geselecteerdelijst = geselecteerdelijst.strip('\n')

def woordentoevoegenaaneenwoordenlijst():
  leegscherm()
  global geselecteerdelijst
  doorgaan = True
  if geselecteerdelijst == "":
    printtop()
    printregel('je moet wel een lijst geselecteerd hebben ')
    printregel('om een woordenlijst te bewerken')
    printbottom()
    doorgaan = False
    time.sleep(3)
  while doorgaan:
    f = open(geselecteerdelijst, "a")
    printtop()
    woordje = input(printregel('wat is het woordje dat je wil toevoegen'))
    betekenis = input(printregel('wat is de betekenis die je wil toevoegen'))
    printbottom()
    f.write('\n')
    f.write(woordje + " - " + betekenis)
    f.close()
    if input('nog een woordje? Y/N') == "N" or "n":
      doorgaan = False
    else:
      doorgaan = True

def woordenlijstenoverhoren():
  global geselecteerdelijst
  global goedfout
  global g
  global b
  global bestandsdata
  global split
  global bestandsdatawoord
  global bestandsdatabetekenis
  global goedfout
  global f
  f = ""
  loop = True
  leegscherm()
  if geselecteerdelijst == "":
    printtop()
    printregel('je moet wel een lijst geselecteerd hebben ')
    printregel('om een woordenlijst te bewerken')
    printbottom()
    loop = False
    time.sleep(3)
  while loop:
    leegscherm()
    printtop()
    printregel("we gaan beginnen met de lijst overhoren")
    printbottom()
    printtop()
    loop = True
    f = open(geselecteerdelijst)
    bestandsdata = f.read().split("\n")
    for i in range(len(bestandsdata)):
      b = bestandsdata[i]
      split = b.split(" - ")
      for i in range(2):
        bestandsdatawoord = split[0]
        bestandsdatabetekenis = split[1]
      g = input(printregel("wat betekent: "+ bestandsdatawoord))
      if g == bestandsdatabetekenis:
        goedfout = 'goed'
      else:
        goedfout = 'fout'
      print('dat was', goedfout)

    if input('wil je het nog een keer doen? y/n') == 'n':
      loop = False
    else:
      loop = True



    f.close()
doorgaan = True
while doorgaan:
  leegscherm()
  maine()
  homevraag = input('')
  if homevraag == '1':
    nieuwewoordenlijstmaken()
  if homevraag == '2':
    selecteereenwoordenlijst()
  if homevraag == '3':
    woordentoevoegenaaneenwoordenlijst()
  if homevraag == '4':
    woordenlijstenoverhoren()
  if homevraag == '5':
    doorgaan = False
leegscherm()
printtop()
printregel('eindopdracht gemaakt door Zeno Smit :)')
printregel('goedendag')
printbottom()
