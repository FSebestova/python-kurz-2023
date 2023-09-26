print("dobrý"+" "+" den")
venecky = [1,2,1,2,6,3,2] #kazda zavorka ma jinej vyznam (v kazdym programovacim jazyce jinej) ... zhruba nejakej prehled .. kulata = volani funkce, hranata = seznamy a indexace, slozena = slovniky (budem delat pozdeji), f string

#spojování sekvencí
print(venecky +[1,2,1,2,6,3,2])

#slicing souvisí s indexováním v rámci sekvencí
jmeno = "Janka"
print(jmeno[1]) #pokud chci vypsat druhý znak ze jména
print(jmeno[0])
print(jmeno[-1]) #poslední prvek
print(jmeno[-2]) #předposlední prvek



venecky = [1,2,1,2,6,3,2]

#od pondělí do pátku
#sytax venecek [zacatek:konec+1]
print(venecky[0:5])

#od úterý do soboty
print(venecky[1:6])

#od úterý do konce týdne
print(venecky[1:])

#od začátku do čtvrtka
print(venecky[:4])

jmeno = "Andy Nováková"
print(jmeno[:4])
print(jmeno[5:])