#PROCVIČENÍ Z MINULA
jmena = ["martin", "michal", "marcel", "jana"]

print(jmena[2]) #vypiš marcela

#SLOVNIKY

knihy = ["Temna noc", 450, True, True]
knihy[0]= "Milosrdná vražda"

knihy2 = {
    "Nazev": "Ananas na pizzu patří",   #název atributu: hodnota
    "Cena": 0,
    "Skladem": True,
    "CZ": True
}

print(knihy2)
print(knihy2.keys()) #vypíše atributy
print(knihy2.values()) #vypíše hodnoty
print(knihy2["Nazev"]) #vypíše hodnotu atributu název
print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")
knihy2["Cena"]= 100
print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")
knihy2["Autor"] = "Františka Šebestová" #přidá atribut do původního seznamu

print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}, autor: {knihy2['Autor']}")

if "Autor" in knihy2:  #operátor in je v seznamu? ověření
    print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}, autor: {knihy2['Autor']}")
else:
    print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}")


#Cvičení1
vysvedceni = {
    "Matematika": 1,
    "Český jazyk": 2,
    "Dějepis": 2
}
print(f"Dějepis: {vysvedceni['Dějepis']}, Matematika: {vysvedceni['Matematika']}, Český jazyk: {vysvedceni['Český jazyk']}")

#Cvičení2
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] = 5781

print(sales)

#Cvičení3
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cislo_listku = int(input("Jaké je číslo Vašeho lístku: "))

if cislo_listku in tombola: 
    	print(f"Vyhráli jste {tombola[cislo_listku]}")
else:
     print(f"Bohužel nevyhráváš nic.")

#Cvičení4
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

host = str(input("Zadejte Vaše jméno: "))


if host in passwords:
     heslo = input("Jste na seznamu zadejte heslo: ")
     if heslo == passwords[host]:
          print(f"Můžete vstoupit")
     else:
            print(f"Špatné heslo")
          
else:
    print("Nejste na seznamu")


