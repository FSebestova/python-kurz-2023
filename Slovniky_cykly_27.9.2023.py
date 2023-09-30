# seznam = [100,200,300,400]
# soucet = 0 #výchozí hodnota

# for polozka in seznam: #prochází jednu položku po druhé
#     soucet += polozka #aktualizace te hodnoty: soucet = soucet + polozka

#     print(soucet)


sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

pocet_prodanych_kusu = 0

for klic in sales:
    print(klic) #vypíše jen klíče
    print(sales[klic])  #řádek 22 je elegantnější způsob zápisu pro toto

for klic, hodnota in sales.items():  #vytáhne jednotlivé položky, items zajistí že dostanu tu dvojici klíč a hodnota
    print(f"nazev: {klic}, pocet prodanych kusu: {hodnota}")


for value in sales.values(): #vypíše jen hodnoty "value"
    print(value) 

for klic, hodnota in sales.items():  #spočítá celkový počet všech prodaných kusů
    pocet_prodanych_kusu += hodnota
    print(pocet_prodanych_kusu)

