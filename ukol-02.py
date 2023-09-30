sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}


soucastka = input("Kód součástky: ")

if soucastka in sklad:
    mnozstvi = int(input("Zadejte požadované množství:"))
    if mnozstvi <= sklad[soucastka]:   #vypíše vypíše pouze hodnotu
      print(f"Požadované množství je skladem")
      nove_mnozstvi = sklad[soucastka] - mnozstvi
      a = {soucastka: nove_mnozstvi} #nově definovaná upravená hodnota a klíč ve slovníku 
      sklad.update(a)
      print(f"Nově skladem: {sklad[soucastka]}")
    else:
        sklad.pop(soucastka)  #odebrání hodnoty ze slovníku
        print("Lze prodat jen omezené množství")

else:
    print("Součástka není skladem")



