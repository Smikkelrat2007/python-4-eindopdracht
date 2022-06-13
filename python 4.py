import os
import time
geselecteerdelijst = ""
lenscherm = 45

def printregel(input):
  print("|{:<43}|".format(input.strip('\n \r\t')))

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
  laatstelijn = ""
  doorgaan = True
  printtop()
  printregel("hoe moet je lijst heten??? (")
  printregel("gebruik wel een andere naam dan")
  printregel("een van de anderewoordenlijsten)")
  printbottom()
  naamlijst = input(' ')
  lijstvanwoordlijsten = open('lijstvanwoordlijsten', "r")
  for line in lijstvanwoordlijsten:
    laatstelijn = line
  lijstvanwoordlijsten.close()
  lijstvanwoordlijsten = open('lijstvanwoordlijsten', "a")
  if not laatstelijn == "":
    lijstvanwoordlijsten.write("\n")
  lijstvanwoordlijsten.write(naamlijst)
  lijstvanwoordlijsten.close()
  leegscherm()
  f = open(naamlijst, "a")
  printtop()
  printregel('wat is het woordje: ')
  printbottom()
  woordje = input("")
  printtop()
  printregel('wat is de betekenis: ')
  printbottom()
  betekenis = input("")
  f.write(woordje + " - " + betekenis)
  f.close()
  doorgaan = input('nog een woordje? y/n')
  while doorgaan != "n":
    leegscherm()
    f = open(naamlijst, "a")
    printtop()
    printregel('wat is het woordje: ')
    printbottom()
    woordje = input("")
    printtop()
    printregel('wat is de betekenis: ')
    printbottom()
    betekenis = input("")
    f.write("\n")
    f.write(woordje + " - " + betekenis)
    f.close()
    printtop()
    printregel('nog een woordje? y/n')
    printbottom()
    doorgaan = input()

def selecteereenwoordenlijst(geselecteerdelijst):
  collectlijst = []
  leegscherm()
  lijstvanwoordlijsten = open('lijstvanwoordlijsten')
  printtop()
  printregel("welk van deze lijsten wil je selecteren:")
  loopcount = 0
  for line in lijstvanwoordlijsten:
    printregel("")
    printregel(str(loopcount) + ". " + line)
    printregel("")
    loopcount += 1
    collectlijst.append(line.strip("\n "))
  if loopcount == 0:
    leegscherm()
    printtop()
    printregel("Oei, Het ziet er naar uit dat ")
    printregel("u nog geen lijsten heeft aangemaakt :(")
    printbottom()
    time.sleep(3)
  else:
    printbottom()
    geselecteerdelijst = collectlijst[int(input('').strip('\n '))]
  return geselecteerdelijst

def woordentoevoegenaaneenwoordenlijst(geselecteerdelijst):

  leegscherm()

  doorgaan = True
  if geselecteerdelijst == "":
    printtop()
    printregel('je moet wel een lijst geselecteerd hebben ')
    printregel('om een woordenlijst te bewerken')
    printbottom()
    doorgaan = False
    time.sleep(3)
  while doorgaan != "n":
    f = open(geselecteerdelijst, "a")
    leegscherm()
    printtop()
    printregel('wat is het woordje: ')
    printbottom()
    woordje = input("")
    printtop()
    printregel('wat is de betekenis: ')
    printbottom()
    betekenis = input("")
    f.write('\n')
    f.write(woordje + " - " + betekenis)
    f.close()
    printtop()
    printregel('nog een woordje? y/n')
    printbottom()
    doorgaan = input('')


def woordenlijstenoverhoren(geselecteerdelijst):
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
homevraag = "0"
while homevraag != "5":
  leegscherm()
  maine()
  homevraag = input('')
  if homevraag == '1':
    nieuwewoordenlijstmaken()
  if homevraag == '2':
    geselecteerdelijst = selecteereenwoordenlijst(geselecteerdelijst)
  if homevraag == '3':
    woordentoevoegenaaneenwoordenlijst(geselecteerdelijst)
  if homevraag == '4':
    woordenlijstenoverhoren(geselecteerdelijst)
leegscherm()
printtop()
printregel('eindopdracht gemaakt door Zeno Smit :)')
printregel('goedendag')
printbottom()
