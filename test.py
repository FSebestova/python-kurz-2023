print("Vítejte v kurzu Pythonu") # řetězec, string

nazev_hry = "Romeo a Julie"  #proměná
cena_listku = 150
pocet_listku = int(input("Zadejte počet lístků: ")) #int = číslo , input = text

celkova_cena = cena_listku * pocet_listku

#pokud je počet lístků alespoň 3 dostane zákazník slevu 10%

if pocet_listku >= 3:
    zlevnena_cena = celkova_cena * 0.90
    print(f"Zlevněná cena {zlevnena_cena} z původní ceny {celkova_cena}")
else:
    print(f"Celkova cena je {celkova_cena}")



# print(f"Zlevněná cena {zlevnena_cena} z původní ceny {celkova_cena}") # f notace = print() umi pracovat jenom s retezci. My jsme ale chteli vytisknout nejaky text a do toho pridat i nasi promnennou, cena_listku, ktera neni recezec ale cislo. Pouzitim f jsme to cislo “integrovali” do retezce