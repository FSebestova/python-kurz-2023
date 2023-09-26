#Zadání cvičení: Využijte příklady z výkladu. Upravte je tak, aby
#- se program zeptal uživatele i na věk, a ověřil, že má alespoň 13 let. Pokud nemá alespoň 13 let, nezeptá se už na počet lístků a skončí (tj. nákup neproběhne).
#-bonus pro netrpělivé :slightly_smiling_face: viz výše + místo slevy 10% uplatní akci "při nákupu alespoň 3 lístků je jeden lístek zdarma"

nazev_hry = "Romeo a Julie"  #proměná
cena_listku = 150


vek_uzivatele = int(input("Věk uživatele: "))
if vek_uzivatele >= 13:
    pocet_listku = int(input("Zadejte počet lístků: "))
    celkova_cena = cena_listku * pocet_listku
    print(f"Cena {celkova_cena}")
    if pocet_listku > 2:
        nova_cena = celkova_cena - cena_listku
        print(f"Nová cena při nákupu alespoň 3 lístků {nova_cena}")
else:
    print("Nelze provést nákup")
    






