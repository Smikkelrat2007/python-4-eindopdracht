import os
import time
geselecteerdelijst = ""
lenscherm = 45

def print_regel(input):
  print("|{:<43}|".format(input.strip('\n \r\t')))

def print_top():
  print("="*lenscherm)

def print_bottom():
  print("=" * lenscherm)

def leegscherm():
  os.system('clear')

def print_mooi_uit(input):
  print_top()
  print_regel(input)
  print_bottom()

def menu():
  print_top()
  print_regel("1. nieuwe woordenlijst maken")
  print_regel("2. selecteer een lijst")
  print_regel("3. woorden toevoegen aan woordenlijst")
  print_regel("4. woordenlijst overhoren")
  print_regel("5. het progamma stoppen")
  print_bottom()

def nieuwe_woordenlijst_maken():
  leegscherm()
  print_top()
  print_regel("hoe moet je lijst heten??? (")
  print_regel("gebruik wel een andere naam dan")
  print_regel("een van de anderewoordenlijsten)")
  print_bottom()
  naamlijst = input()

  lijst_van_woordlijsten = open('lijstvanwoordlijsten', "a")
  lijst_van_woordlijsten.write("\n")
  lijst_van_woordlijsten.write(naamlijst)
  lijst_van_woordlijsten.close()
  leegscherm()
  f = open(naamlijst, "a")
  print_mooi_uit('wat is het woordje: ')
  woordje = input("")
  print_mooi_uit('wat is de betekenis: ')
  betekenis = input("")
  f.write(woordje + " - " + betekenis)
  f.close()
  print_mooi_uit("nog een woordje? y/n")
  while (doorgaan := input('')) != "n":
    leegscherm()
    f = open(naamlijst, "a")
    print_mooi_uit("wat is het woordje: ")
    woordje = input("")
    print_mooi_uit("wat is de betekenis: ")
    betekenis = input("")

    print_mooi_uit("nog een woordje? y/n")

    f.write("\n")
    f.write(woordje + " - " + betekenis)
    f.close()

def selecteer_een_woordenlijst(geselecteerdelijst):
  collectlijst = []
  leegscherm()
  lijstvanwoordlijsten = open('lijstvanwoordlijsten')
  print_top()
  print_regel("welk van deze lijsten wil je selecteren:")
  loopcount = 0
  for line in lijstvanwoordlijsten:
    if line.strip("\t\r\n") == "":
      pass
    else:
      print_regel("")
      print_regel(str(loopcount) + ". " + line)
      print_regel("")
      loopcount += 1
      collectlijst.append(line.strip("\n "))
  if loopcount == 0:
    leegscherm()
    print_top()
    print_regel("Oei, Het ziet er naar uit dat ")
    print_regel("u nog geen lijsten heeft aangemaakt :(")
    print_bottom()
    time.sleep(3)
  else:
    print_bottom()
    geselecteerdelijst = collectlijst[int(input('').strip('\n '))]
  return geselecteerdelijst

def woorden_toevoegen_aan_een_woordenlijst(geselecteerdelijst):

  leegscherm()


  if geselecteerdelijst == "":
    print_top()
    print_regel('je moet wel een lijst geselecteerd hebben ')
    print_regel('om een woordenlijst te bewerken')
    print_bottom()
    doorgaan2 = "n"
    time.sleep(3)
  else:
    print_mooi_uit('wil je beginnen? y/n')
    while (doorgaan2 := input("")) != "n":
      f = open(geselecteerdelijst, "a")
      leegscherm()
      print_mooi_uit("wat is het woordje: ")
      woordje = input("")
      print_mooi_uit("wat is de betekenis: ")
      betekenis = input("")
      f.write('\n')
      f.write(woordje + " - " + betekenis)
      f.close()

def woordenlijsten_overhoren(geselecteerdelijst):
  f = ""
  loop = True
  leegscherm()
  if geselecteerdelijst == "":
    print_top()
    print_regel('je moet wel een lijst geselecteerd hebben ')
    print_regel('om een woordenlijst te bewerken')
    print_bottom()
    time.sleep(3)
    loop = "n"
  while loop != "n":
    leegscherm()
    print_mooi_uit("we gaan beginnen met de lijst overhoren")
    f = open(geselecteerdelijst)
    bestandsdata = f.read().split("\n")
    for i in range(len(bestandsdata)):
      b = bestandsdata[i]
      split = b.split(" - ")
      for i in range(2):
        bestandsdatawoord = split[0]
        bestandsdatabetekenis = split[1]
      print_mooi_uit((print_ff := "wat betekent: "+ bestandsdatawoord))
      g = input()
      if g == bestandsdatabetekenis:
        goedfout = 'goed'
      else:
        goedfout = 'fout'
      print_mooi_uit((print_ff := 'dat was'+ goedfout))
    if input('wil je het nog een keer doen? y/n') == 'n':
      loop = "n"
    f.close()
def main(geselecteerdelijst):
  menu()
  while (homevraag := input("")) != "5":
    leegscherm()
    if homevraag == '1':
      nieuwe_woordenlijst_maken()
    if homevraag == '2':
      geselecteerdelijst = selecteer_een_woordenlijst(geselecteerdelijst)
    if homevraag == '3':
      woorden_toevoegen_aan_een_woordenlijst(geselecteerdelijst)
    if homevraag == '4':
      woordenlijsten_overhoren(geselecteerdelijst)
    leegscherm()
    menu()

main(geselecteerdelijst)
print_top()
print_regel('eindopdracht gemaakt door Zeno Smit :)')
print_regel('goedendag')
print_bottom()
